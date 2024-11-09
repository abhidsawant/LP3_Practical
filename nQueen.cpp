#include <iostream>
#include <vector>

using namespace std;

// Function to check if a queen can be placed at board[row][col]
bool isSafe(const vector<vector<int>>& board, int row, int col, int n) {
    // Check the column for any queen
    for (int i = 0; i < row; i++)
        if (board[i][col] == 1)
            return false;

    // Check the upper left diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j] == 1)
            return false;

    // Check the upper right diagonal
    for (int i = row, j = col; i >= 0 && j < n; i--, j++)
        if (board[i][j] == 1)
            return false;

    return true;
}

// Recursive function to solve the N-Queens problem
bool solveNQueens(vector<vector<int>>& board, int row, int n) {
    if (row == n)  // All queens are placed
        return true;

    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1;  // Place the queen

            if (solveNQueens(board, row + 1, n))  // Recursively place rest of queens
                return true;

            board[row][col] = 0;  // Backtrack if placing queen here doesn't lead to a solution
        }
    }

    return false;  // No safe place found for this row
}

// Function to initialize the board with the first queen placed
void placeFirstQueen(vector<vector<int>>& board, int row, int col, int n) {
    board[row][col] = 1;  // Place the first queen at the given position
}

// Function to display the N-Queens board
void displayBoard(const vector<vector<int>>& board, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << (board[i][j] ? "Q " : ". ");
        }
        cout << endl;
    }
}

int main() {
    int n;
    int initialRow, initialCol;

    cout << "Enter the size of the board (N): ";
    cin >> n;
    cout << "Enter the row and column of the first Queen (0-indexed): ";
    cin >> initialRow >> initialCol;

    // Initialize the board with zeros
    vector<vector<int>> board(n, vector<int>(n, 0));

    // Place the first queen at the specified position
    placeFirstQueen(board, initialRow, initialCol, n);

    // Start placing remaining queens from the next row
    if (solveNQueens(board, initialRow + 1, n)) {
        cout << "N-Queens solution:\n";
        displayBoard(board, n);
    } else {
        cout << "No solution exists for the given configuration.\n";
    }

    return 0;
}
