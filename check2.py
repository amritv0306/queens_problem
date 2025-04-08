# N = 8
# color_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 2, 3, 0, 0, 0, 0, 1],
#     [0, 2, 3, 3, 0, 0, 0, 1],
#     [0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 4, 4, 4, 5, 5, 1],
#     [0, 0, 4, 4, 4, 5, 5, 5],
#     [0, 0, 6, 6, 4, 7, 7, 7],
#     [6, 6, 6, 6, 4, 4, 7, 7]
# ]
# N = 9
# color_grid = [
#     [0, 1, 2, 2, 2, 3, 3, 3, 3],
#     [0, 1, 2, 2, 2, 2, 3, 3, 3],
#     [0, 1, 2, 1, 2, 2, 2, 2, 3],
#     [0, 1, 1, 1, 1, 2, 3, 3, 3],
#     [0, 4, 4, 1, 5, 6, 3, 3, 3],
#     [0, 0, 4, 4, 4, 6, 3, 3, 3],
#     [7, 7, 4, 4, 4, 6, 3, 6, 3],
#     [7, 7, 4, 4, 4, 6, 6, 6, 6],
#     [7, 7, 7, 7, 7, 7, 7, 6, 8]
# ]
N = 8
# color_grid = [
#     [0, 0, 0, 0, 1, 2, 2, 2],
#     [3, 2, 2, 4, 1, 2, 2, 2],
#     [3, 2, 2, 4, 5, 5, 5, 2],
#     [3, 2, 2, 4, 2, 6, 2, 2],
#     [3, 2, 2, 4, 2, 6, 2, 2],
#     [3, 2, 7, 7, 2, 2, 2, 2],
#     [3, 2, 2, 2, 2, 2, 2, 2],
#     [2, 2, 2, 2, 2, 2, 2, 2]
# ]
# color_grid = [
#     [0, 0, 0, 1, 1, 2, 2, 2],
#     [1, 0, 1, 1, 1, 1, 2, 1],
#     [1, 0, 1, 1, 3, 1, 2, 1],
#     [1, 1, 1, 3, 3, 1, 1, 1],
#     [1, 1, 3, 3, 4, 4, 1, 1],
#     [1, 1, 5, 4, 4, 6, 1, 1],
#     [1, 5, 5, 7, 4, 6, 6, 1],
#     [5, 5, 7, 7, 7, 7, 6, 6] 
# ]
color_grid = [
    [0, 0, 1, 1, 1, 2, 2, 2],
    [3, 0, 1, 1, 2, 2, 4, 2],
    [3, 0, 0, 1, 1, 4, 4, 4],
    [3, 3, 5, 5, 1, 6, 4, 6],
    [3, 3, 3, 5, 1, 6, 6, 6],
    [3, 3, 3, 5, 5, 7, 7, 6],
    [3, 3, 3, 3, 3, 3, 7, 6],
    [3, 3, 3, 3, 3, 3, 7, 7]
]

# used sets to track occupied columns, colors, and immediate diagonals
occupied_cols = set()
occupied_colors = set()
immediate_diagonals = set()

# this is the Solution board (i've initialized with -1 means no queen placed)
queens = [-1] * N

def print_solution():
    board = [['x' for _ in range(N)] for _ in range(N)]
    for r in range(N):
        board[r][queens[r]] = 'Q'
    
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(row, col):
    color = color_grid[row][col]
    
    # checking column constraint
    if col in occupied_cols:
        return False
    
    # checking color constraint
    if color in occupied_colors:
        return False
    
    # checking immediate diagonal constraint
    if (row - 1, col - 1) in immediate_diagonals or (row - 1, col + 1) in immediate_diagonals:
        return False
    
    return True

def place_queen(row):
    if row == N:
        print_solution()
        return True  # stoping condition
    
    for col in range(N):
        if is_safe(row, col):
            # placing queen
            queens[row] = col
            occupied_cols.add(col)
            occupied_colors.add(color_grid[row][col])
            immediate_diagonals.add((row, col))
            
            # Recursive calling
            if place_queen(row + 1):
                return True
            
            # Backtracking
            queens[row] = -1
            occupied_cols.remove(col)
            occupied_colors.remove(color_grid[row][col])
            immediate_diagonals.remove((row, col))
    
    return False


# starting backtracking from row 0
place_queen(0)
