def print_board(board):
    for row in board:
        print(" | ".join(row))

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    
    return None

def is_draw(board):
    for row in board:
        if '_' in row:
            return False
    return True

def tic_tac_toe():
    board = [['_' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, 2): "))
            
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != '_':
                print("Invalid move. Try again.")
                continue
            
            board[row][col] = current_player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            1
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Please enter valid integers for row and column.")

if __name__ == "__main__":
    tic_tac_toe()
