import random

def get_player_move():
    move = input("Enter your move (rock, paper, or scissors): ").lower()
    while move not in ['rock', 'paper', 'scissors']:
        move = input("Invalid move. Enter your move (rock, paper, or scissors): ").lower()
    return move

def get_computer_move():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

def find_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    if (player_move == "rock" and computer_move == "scissors") or \
       (player_move == "scissors" and computer_move == "paper") or \
       (player_move == "paper" and computer_move == "rock"):
        return "player"
    return "computer"

def play_round():
    player_move = get_player_move()
    computer_move = get_computer_move()
    print("Computer Choice Was '" + computer_move + "'")
    winner = find_winner(player_move, computer_move)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "player":
        print("You win!")
    else:
        print("Computer wins!")
    return winner

def play_game():
    player_score = 0
    computer_score = 0
    while True:
        winner = play_round()
        if winner == "player":
            player_score += 1
        elif winner == "computer":
            computer_score += 1
        print("Player score: ", player_score)
        print("Computer score: ", computer_score)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Final scores: ")
    print("Player score: ", player_score)
    print("Computer score: ", computer_score)

play_game()