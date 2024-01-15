import random

def play_round(current_player, scores):
    while True:
        user_choice = input(f"Player {current_player + 1}, Enter 'y' to roll dice and 'n' to skip turn: ")
        try:
            if user_choice == 'y':
                dice_number = random.randint(1, 6)
                if dice_number == 1:
                    print("\n\tDice number: ", dice_number, f"\n\tYou got 1 so score has been reset.\n\tNow, next player turn\n")
                    scores[current_player] = 0
                    return scores
                else:
                    scores[current_player] += dice_number
                    print("\n\tDice number: ", dice_number, f"\n\tPlayer {current_player + 1}, Score: ", scores[current_player], "\n")
                    
            elif user_choice == 'n':
                print(f"\n\tPlayer {current_player + 1} skipped.\n")
                return scores

        except Exception as e:
            print("Value Error, ", e)
            
def start_game():
    scores = [0, 0]
    current_player = 0

    while True:
        scores = play_round(current_player, scores)
        if scores[current_player] >= 50:
            print(f"\n\tPlayer {current_player + 1} won with the score of {scores[current_player]}\n")
            break
        current_player = 1 - current_player

if __name__ == '__main__':
    start_game()