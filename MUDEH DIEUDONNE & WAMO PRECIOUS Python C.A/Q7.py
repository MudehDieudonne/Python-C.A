def is_attacking(row1, col1, row2, col2):
    """Check if queen at (row1, col1) is attacking queen at (row2, col2)"""
    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)

def n_queens(n):
    """Find all solutions to the N queens problem"""
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def place_queens(row):
        if row == n:
            # We have placed a queen in each row, so we have a solution
            solutions.append([' '.join(row) for row in board])
            return

        for col in range(n):
            if all(not is_attacking(row, col, row2, col2) for row2 in range(row) for col2 in range(n)):
                # Place a queen at (row, col)
                board[row][col] = 'Q'

                # Try placing queens in the remaining rows
                place_queens(row + 1)

                # Remove the queen from (row, col)
                board[row][col] = '.'

    place_queens(0)
    return solutions

# Find all solutions to the 4 queens problem
solutions = n_queens(4)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()

# Find all solutions to the 6 queens problem
solutions = n_queens(6)
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()