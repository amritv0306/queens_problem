def filter_single_color_blocks(colors):
    N = len(colors)  # Grid size
    M = len(colors[0])  # Grid width
    
    # Initialize final answer and visited matrix
    final_ans = [["_"] * M for _ in range(N)]  # Start with all _
    visited = [[0] * M for _ in range(N)]
    
    # Check columns for colors that appear only in one column
    color_column_count = {}  # Track color appearances per column
    for col in range(M):
        for row in range(N):
            color = colors[row][col]
            if color not in color_column_count:
                color_column_count[color] = set()
            color_column_count[color].add(col)
    
    for color, cols in color_column_count.items():
        if len(cols) == 1:  # If a color appears in exactly one column
            target_col = list(cols)[0]
            for row in range(N):
                if colors[row][target_col] != color:
                    final_ans[row][target_col] = "0"
                    visited[row][target_col] = 1
    
    # Check rows for colors that appear only in one row
    color_row_count = {}  # Track color appearances per row
    for row in range(N):
        for col in range(M):
            color = colors[row][col]
            if color not in color_row_count:
                color_row_count[color] = set()
            color_row_count[color].add(row)
    
    for color, rows in color_row_count.items():
        if len(rows) == 1:  # If a color appears in exactly one row
            target_row = list(rows)[0]
            for col in range(M):
                if colors[target_row][col] != color:
                    final_ans[target_row][col] = "0"
                    visited[target_row][col] = 1
    
    return final_ans, visited

def mark_adjacent_blocks(final_ans, colors):
    N, M = len(colors), len(colors[0])
    color_positions = {}
    
    # Store positions of each color
    for i in range(N):
        for j in range(M):
            color = colors[i][j]
            if color not in color_positions:
                color_positions[color] = []
            color_positions[color].append((i, j))
    
    # Check for colors with exactly 2 blocks in a single row or column
    for color, positions in color_positions.items():
        if len(positions) == 2:
            (r1, c1), (r2, c2) = positions
            if r1 == r2 or c1 == c2:  # Same row or same column
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Adjacent positions
                    nr1, nc1 = r1 + dr, c1 + dc
                    nr2, nc2 = r2 + dr, c2 + dc
                    if 0 <= nr1 < N and 0 <= nc1 < M:
                        final_ans[nr1][nc1] = "0"
                    if 0 <= nr2 < N and 0 <= nc2 < M:
                        final_ans[nr2][nc2] = "0"
    
    return final_ans


# Example usage:
colors = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 2, 3, 0, 0, 0, 0, 1],
    [0, 2, 3, 3, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 4, 4, 4, 5, 5, 1],
    [0, 0, 4, 4, 4, 5, 5, 5],
    [0, 0, 6, 6, 4, 7, 7, 7],
    [6, 6, 6, 6, 4, 4, 7, 7]
]

final_ans, visited = filter_single_color_blocks(colors)
final_ans = mark_adjacent_blocks(final_ans, colors)


print("Final Answer Matrix:")
for row in final_ans:
    print(" ".join(row))

print("\nVisited Matrix:")
for row in visited:
    print(row)
