def check_winner(board, current_player):
    for i in range(3):
        if all(board[i][j] == current_player for j in range(3)) or all(board[j][i] == current_player for j in range(3)):
            return True
    if all(board[i][i] == current_player for i in range(3)) or all(board[2-i][i] == current_player for i in range(3)):
        return True
    return False
    
def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def show_board(board):
    for row in board:
        print(" | ".join(row))
        print('-'*9)
    print("\n")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ('X', 'O')
    positions_played = set()
    current_player = players[0]

    while True:
        try:
            print(f"{current_player}'s Turn")
            row = int(input("Enter the position for row (0, 1 or 2): "))
            col = int(input("Enter the position for column (0, 1 or 2): "))
            print("\n")
            
            if -1 < row < 3 and -1 < col < 3:
                if board[row][col] == " ":
                    board[row][col] = current_player
                    show_board(board)
                    positions_played.add((row, col))

                    if check_winner(board, current_player):
                        print(f"{current_player} won")
                        break
                
                    if board_full(board):
                        print("It's a tie.")
                        break

                    current_player = players[1] if current_player == players[0] else players[0]

                else:
                    print("Position already played!")
                    
            else:
                print("\nEnter valid number! \n")

        except Exception as e:
            print("Error occurred!, ", e)

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        play_again = input("Want to play again? (y or n): ")
        if play_again.lower() != 'y':
            break