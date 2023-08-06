import time
import random
import mainbot


def tictactoe_game():

    print("When you type 0, it means the first one, 1 is the second, 2 is the third")
    def initialize_board():
        return [[" " for _ in range(3)] for _ in range(3)]

    def display_board(board):
        for row in board:
            print("|".join(row))
            print("-" * 5)

    def get_player_move():
        while True:
            try:
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                return row, col
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")

    def is_valid_move(board, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

    def is_winner(board, symbol):
        # check rows, columns, and diagonals for a win.
        for i in range(3):
            if all(board[i][j] == symbol for j in range(3)):
                return True
            if all(board[j][i] == symbol for j in range(3)):
                return True
        if all(board[i][i] == symbol for i in range(3)):
            return True
        if all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def is_draw(board):
        return all(board[i][j] != " " for i in range(3) for j in range(3))

    def get_empty_cells(board):
        return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

    def computer_move(board):
        empty_cells = get_empty_cells(board)
        return random.choice(empty_cells)


    board = initialize_board()
    player_symbol = "X"
    computer_symbol = "O"

    while True:
        display_board(board)

        # player's turn
        while True:
            row, col = get_player_move()
            if is_valid_move(board, row, col):
                board[row][col] = player_symbol
                break
            else:
                print("Invalid move. The cell is already occupied.")

        if is_winner(board, player_symbol):
            display_board(board)
            print("Congratulations! You win!")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # computer's turn
        row, col = computer_move(board)
        board[row][col] = computer_symbol

        if is_winner(board, computer_symbol):
            display_board(board)
            print("Computer wins! You lose.")
            break

        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

    #game choice code
    print ("Would you like to play again?")
    playAgain = input("Enter Yes/No\n")
    if playAgain.lower() ==  "yes" or playAgain.lower() == "y":
        print("Amazing!")
        gameChoice = input("Would you like to play hangman, tic-tac-toe, or codebreaker?\n")
        if gameChoice.lower() == "hangman":
            hangman()
        elif gameChoice.lower() == "codebreaker":
            codebreaker(code_length, max_attempts)
        elif gameChoice.lower() == "tic-tac-toe" or gameChoice.lower() == "tictactoe":
            tictactoe_game()
    else:
        print("Aw man, that's alright.\n")
        mainbot.robo()

def codebreaker(code_length, max_attempts):

    def generate_secret_code(code_length):
        # this function generates a random secret code of the specified length
        code_digits = [str(random.randint(0, 9)) for _ in range(code_length)]
        return "".join(code_digits)

    def get_player_guess(code_length):
        # this function gets the player's guess as input
        guess = input(f"Enter your {code_length}-digit guess: ")
        return guess

    def compare_codes(secret_code, player_guess):
        # this function compares the player's guess with the secret code and provides feedback
        if secret_code == player_guess:
            return "Congratulations! You guessed the code!"

        feedback = []
        for i in range(len(secret_code)):
            if secret_code[i] == player_guess[i]:
                feedback.append("X")
            elif player_guess[i] in secret_code:
                feedback.append("O")
            else:
                feedback.append("_")
        return "".join(feedback)

    # main game loop
    secret_code = generate_secret_code(code_length)
    attempts = 0

    print(f"Welcome to the Codebreaker Game! Try to guess the {code_length}-digit code.")
    print("Feedback: X - correct digit and position, O - correct digit but wrong position, _ - incorrect digit.")

    while attempts < max_attempts:
        player_guess = get_player_guess(code_length)
        attempts += 1

        if len(player_guess) != code_length or not player_guess.isdigit():
            print(f"Invalid guess! Please enter a {code_length}-digit number.")
            continue

        feedback = compare_codes(secret_code, player_guess)
        print(f"Attempt {attempts}/{max_attempts}: {feedback}")

        if feedback == "Congratulations! You guessed the code!":
            break

    if feedback != "Congratulations! You guessed the code!":
        print(f"Sorry, you couldn't guess the code. The secret code was {secret_code}.")

    #game choice code
    print ("Would you like to play again?")
    playAgain = input("Enter Yes/No\n")
    if playAgain.lower() ==  "yes" or playAgain.lower() == "y":
        print("Amazing!")
        gameChoice = input("Would you like to play hangman, tic-tac-toe, or codebreaker?\n")
        if gameChoice.lower() == "hangman":
            hangman()
        elif gameChoice.lower() == "codebreaker":
            codebreaker(code_length, max_attempts)
        elif gameChoice.lower() == "tic-tac-toe" or gameChoice.lower() == "tictactoe":
            tictactoe_game()
    else:
        print("Aw man, that's alright.\n")
        mainbot.robo()

def hangman():

    print ("Ready to start? Let's go!")
    time.sleep(1)
    print ("Start guessing now!\n")
    time.sleep(0.5)
    # list of the words and setting up our random word and guess count/turns
    words = ['panic','tourist','bomb','lemon','mouse','towel','era','dollar','neighbour','wood','copper','cottage','wave','ghost']
    word = random.choice(words)
    wordLength = len(word)
    guesses = ''
    turns = 7
    print(f"The word is {wordLength} letters long")
    #as long as we have turns remaining, this loop runs
    while turns > 0:
        failed = 0
        #checks the word to see if it contains the character, and gives feedback based on if it does or not
        for char in word:
            if char in guesses:
                print (char,end="")
            else:
                print ("_",end=""),
                failed += 1
        #if you got the word, you win
        if failed == 0:
            print ("\nYou won! Great job!")
            break
        #constantly guessing the character until one of the if statements occur
        guess = input("\nGuess a character:")
        guesses += guess
        #if the character isnt in the word,  takes away a turn and makes you go again.
        #if your turns are all gone, you lose
        if guess not in word:
            turns -= 1
            print("\nThat's wrong")
            print("\nYou have", + turns, 'more guesses')
            if turns == 0:
                print ("\nYou lose")
    #game choice code
    print ("Would you like to play again?")
    playAgain = input("Enter Yes/No\n")
    if playAgain.lower() ==  "yes" or playAgain.lower() == "y":
        print("Amazing!")
        gameChoice = input("Would you like to play hangman, tic-tac-toe, or codebreaker?\n")
        if gameChoice.lower() == "hangman":
            hangman()
        elif gameChoice.lower() == "codebreaker":
            codebreaker(code_length, max_attempts)
        elif gameChoice.lower() == "tic-tac-toe" or gameChoice.lower() == "tictactoe":
            tictactoe_game()
    else:
        print("Aw man, that's alright.\n")
        mainbot.robo()
def main():

    #starts with an introduction
    name = input("\nHello random human! I'm Gamebot. May I have your name?\n")
    print(f'"{name}". What a wonderful name! Would you like to play a game with me?')
    yesno = input("(Enter Yes/No)\n")

    #continue if input is yes, kill the script if input is no
    if yesno.lower() ==  "yes" or yesno.lower() == "y":
        print("Amazing!")
    else:
        print("Aw man, that's alright.\n")
        mainbot.robo()

    #asking which game to play, and then running that game(game choice code)
    gameChoice = input("Would you like to play hangman, tic-tac-toe, or codebreaker?\n")
    if gameChoice.lower() == "hangman":
        hangman()
    elif gameChoice.lower() == "codebreaker":
        codebreaker(code_length, max_attempts)
    elif gameChoice.lower() == "tic-tac-toe":
        tictactoe_game()

if __name__ == "__main__":
    code_length = 4
    max_attempts = 10
    main()
