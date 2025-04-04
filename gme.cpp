#include <iostream>
#include <vector>
#include <set>

using namespace std;

#define N 8  // Adjust based on grid size

struct Position {
    int row, col;
};

bool isSafe(vector<vector<int>>& board, vector<vector<int>>& colors, int row, int col, set<int>& usedColors, vector<bool>& colorHasQueen) {
    // Check row and column
    for (int i = 0; i < N; i++) {
        if (board[row][i] == 1 || board[i][col] == 1) {
            return false;
        }
    }
    
    // Check diagonals
    for (int i = -N; i < N; i++) {
        if (row + i >= 0 && row + i < N && col + i >= 0 && col + i < N && board[row + i][col + i] == 1)
            return false;
        if (row + i >= 0 && row + i < N && col - i >= 0 && col - i < N && board[row + i][col - i] == 1)
            return false;
    }
    
    // Ensure each color gets exactly one queen
    int color = colors[row][col];
    if (colorHasQueen[color]) {
        return false;
    }
    
    return true;
}

bool solveQueens(vector<vector<int>>& board, vector<vector<int>>& colors, vector<Position>& positions, int index, set<int>& usedColors, vector<bool>& colorHasQueen) {
    if (index >= positions.size()) return true;  // All positions checked
    
    int row = positions[index].row;
    int col = positions[index].col;
    int color = colors[row][col];
    
    if (isSafe(board, colors, row, col, usedColors, colorHasQueen)) {
        board[row][col] = 1;
        colorHasQueen[color] = true;
        
        if (solveQueens(board, colors, positions, index + 1, usedColors, colorHasQueen)) return true;
        
        board[row][col] = 0;  // Backtrack
        colorHasQueen[color] = false;
    }
    
    return false;
}

int main() {
    vector<vector<int>> colors = {
        {0, 0, 0, 0, 0, 0, 0, 1},
        {0, 2, 3, 0, 0, 0, 0, 1},
        {0, 2, 3, 3, 0, 0, 0, 1},
        {0, 0, 0, 0, 0, 0, 0, 1},
        {0, 0, 4, 4, 4, 5, 5, 1},
        {0, 0, 4, 4, 4, 5, 5, 5},
        {0, 0, 6, 6, 4, 7, 7, 7},
        {6, 6, 6, 6, 4, 4, 7, 7}
    };
    
    vector<vector<int>> board(N, vector<int>(N, 0));
    set<int> usedColors;
    vector<bool> colorHasQueen(8, false);  // Track whether each color has a queen
    vector<Position> positions;
    
    // Collect all possible positions for placing queens
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            positions.push_back({i, j});
        }
    }
    
    if (solveQueens(board, colors, positions, 0, usedColors, colorHasQueen)) {
        for (const auto& row : board) {
            for (int cell : row) {
                cout << cell << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution found." << endl;
    }
    
    return 0;
}