def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def is_safe(board, row, col):
    n = len(board)
    
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens(board, row):
    n = len(board)
    
    # If all queens are placed
    if row == n:
        return True

    # Try all columns for this row
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_n_queens(board, row + 1):
                return True
            board[row][col] = 0
    
    return False

def main():
    n = int(input("Enter the number of queens (n): "))
    board = [[0] * n for _ in range(n)]
    
    for first_col in range(n):
        board[0][first_col] = 1
        if solve_n_queens(board, 1):
            print_board(board)
            break
        board[0][first_col] = 0

if __name__ == "__main__":
    main()
