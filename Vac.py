import os
import time

def print_board(board, rows, cols, vacuum_pos):
    """
    Prints the board as a grid with colors and larger blocks to mimic visual boxes:
    - Red for dirty positions ('D')
    - Green for clean positions ('C')
    - Blue for the vacuum's current position ('V')
    """
    color_vacuum = "\033[44m"  # Blue background
    color_clean = "\033[42m"   # Green background
    color_dirty = "\033[41m"   # Red background
    reset_color = "\033[0m"    # Reset color

    for r in range(rows):
        row = ""
        for c in range(cols):
            pos = (r, c)
            if pos == vacuum_pos:
                row += f"{color_vacuum}   V   {reset_color}"  # Vacuum position
            elif board[pos] == '0':
                row += f"{color_clean}   C   {reset_color}"  # Clean position
            else:
                row += f"{color_dirty}   D   {reset_color}"  # Dirty position
        print(row)

def vacuum_world():
    # Get board size
    rows = int(input("Enter number of rows in the board: "))
    cols = int(input("Enter number of columns in the board: "))

    # Initialize the board with all clean cells ('0')
    board = {}
    for r in range(rows):
        for c in range(cols):
            board[(r, c)] = '0'  # Initially all positions are clean

    # Input the number of dirty cells
    num_dirty_cells = int(input("Enter number of dirty cells: "))
    num_dirty_cells = min(num_dirty_cells, rows * cols)  # Limit to available cells

    for _ in range(num_dirty_cells):
        while True:
            r = int(input(f"Enter row for dirty cell (0-{rows-1}): "))
            c = int(input(f"Enter column for dirty cell (0-{cols-1}): "))
            if board[(r, c)] == '0':  # Only allow marking a clean cell as dirty
                board[(r, c)] = '1'  # Mark the cell as dirty ('1')
                break
            else:
                print("Cell is already dirty. Choose another cell.")

    # Get the initial position (vacuum's position)
    start_row = int(input("Enter starting row position of the vacuum: "))
    start_col = int(input("Enter starting column position of the vacuum: "))
    current_pos = (start_row, start_col)

    # Get the desired final position
    final_row = int(input("Enter desired final row position of the vacuum: "))
    final_col = int(input("Enter desired final column position of the vacuum: "))
    final_pos = (final_row, final_col)

    # Initialize cost and vacuum's initial state
    cost = 0

    print("Initial Board:")
    print_board(board, rows, cols, current_pos)

    # Perform systematic traversal to clean all dirty cells
    while any(cell == '1' for cell in board.values()):  # Continue until all cells are clean
        for r in range(rows):
            for c in range(cols):
                current_pos = (r, c)
                if board[current_pos] == '1':  # If dirty
                    print(f"Position {current_pos} is Dirty.")
                    board[current_pos] = '0'  # Clean the position
                    cost += 1  # Increment cleaning cost
                    print(f"Cleaned position {current_pos}. Cost: {cost}")

                # Increment movement cost (except for the first cell)
                cost += 1

                # Clear screen, print board, and add a gap
                os.system('cls' if os.name == 'nt' else 'clear')
                print_board(board, rows, cols, current_pos)
                time.sleep(0.5)  # Pause for half a second

    # Move to the desired final position
    if current_pos != final_pos:
        print(f"Moving to final position {final_pos}.")
        cost += abs(final_pos[0] - current_pos[0]) + abs(final_pos[1] - current_pos[1])
        current_pos = final_pos

    # Display final state and cost
    print("Final Board:")
    print_board(board, rows, cols, current_pos)
    print(f"Final position: {current_pos}")
    print(f"Total Performance Measurement (cost): {cost}")

# Run the vacuum world simulation
vacuum_world()
