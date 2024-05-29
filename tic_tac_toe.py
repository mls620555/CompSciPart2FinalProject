# Tic Tac Toe

import random


class Tic_Tac_Toe:
    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
        return("")

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            if game_mode == "computer":
                print('Do you want to be X or O?')
            elif game_mode == "two player":
                print("Does Player 1 want to be X or O?")
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'computer'
        else:
            return 'player'

    def playAgain(self):
        # This function returns True if the player wants to play again, False if not.
        # Returns "pastgames" for past games, and asks the user to enter again if they entered none of the above.
        print('Do you want to play again? (yes or no)')
        print("Alternatively, you can access your past games by entering 'past games'. ")
        user_play = input()
        while True:
            if user_play.lower() == "yes":
                return True
            elif user_play.lower() == "no":
                return False
            elif user_play.lower() == "past games":
                return "past games"
            else:
                user_play = input("Please enter 'yes', 'no', or 'past games' (not case sensitive). ")
                continue

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self, board):
        # Let the player type in their move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            if game_mode == "two player" and turn == "player":
                print("Player 1 to move.")
            elif game_mode == "two player" and turn == "computer":
                print("Player 2 to move.")
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getComputerMove(self, board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True

    def recallPastGame(self):
        gameid = input("Which past game would you like to view? (Enter game number 0 to " + str(len(boards)-1) + ") inclusive. ")
        while True:
            try:
                val = int(gameid)
            except ValueError:
                gameid = input("Please input an integer!")
                continue
            gameid = int(gameid)
            if gameid < 0 or gameid > len(boards):
                gameid = input("Please enter an integer from 0 to " + str(len(boards)-1) + " inclusive (you can type both 0 and" + str(len(boards)-1) + ". ")
                continue
            else:
                print(self.drawBoard(boards[gameid]))
                break

    def gameMode(self):
        # Asks user for the gamemode. Returns "robot" for robot and "two player" for two player mode.
        print('Select your gamemode (computer or two players)')
        user_play = input()
        while True:
            if user_play.lower() == "computer":
                return "computer"
            elif user_play.lower() == "two players":
                return "two player"
            else:
                user_play = input("Please enter 'robot' or 'two players' (not case sensitive). ")
                continue

# End of Tic_Tac_Toe class

# Stores current and past games
games = []
# Counts current game from the games list. Starts at 0
current_game = 0
# Stores past boards
boards = []
# Shows which page the user is on. True: play, False: exit, "past games": recall past games
# "two player": two player mode
play_again = True
# Stores gamemode: robot or two player. If it's set to two player, the computerLetter variable
# will be used to store the second player's letter.
game_mode = ""

print('Welcome to Tic Tac Toe!')
print("HOW TO PLAY\nIn this game, you may play against another player or the computer. \nThe goal is to get three X's or 0's in a row.")
print("You can make moves by typing in a number. The board is printed like so:")
print('   |   |')
print(' 7 | 8 | 9')
print('   |   |')
print('-----------')
print('   |   |')
print(' 4 | 5 | 6')
print('   |   |')
print('-----------')
print('   |   |')
print(' 1 | 2 | 3')
print('   |   |')
while True:
    if play_again == True:

        # Creates a new game ONLY if this is the first game
        # Otherwise, this happens at the end of the code.
        if len(games) == 0:
            games.append(Tic_Tac_Toe())

        # Setting gamemode: robot or two player
        game_mode = games[current_game].gameMode()

        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = games[current_game].inputPlayerLetter()
        turn = games[current_game].whoGoesFirst()
        if game_mode == "computer":
            print('The ' + turn + ' will go first.')
        elif game_mode == "two player" and turn == "player":
            print("Player 1 will go first.")
        gameIsPlaying = True

        while gameIsPlaying:
            if turn == 'player':
                # Player's turn.
                games[current_game].drawBoard(theBoard)
                move = games[current_game].getPlayerMove(theBoard)
                games[current_game].makeMove(theBoard, playerLetter, move)

                if games[current_game].isWinner(theBoard, playerLetter):
                    games[current_game].drawBoard(theBoard)
                    if game_mode == "player":
                        print('Hooray! You have won the game!')
                    elif game_mode == "two player":
                        print("Player 1 wins.")
                    gameIsPlaying = False
                else:
                    if games[current_game].isBoardFull(theBoard):
                        games[current_game].drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else:
                # Computer's turn.
                if game_mode == "computer":
                    move = games[current_game].getComputerMove(theBoard, computerLetter)
                else:
                    games[current_game].drawBoard(theBoard)
                    move = games[current_game].getPlayerMove(theBoard)
                games[current_game].makeMove(theBoard, computerLetter, move)

                if games[current_game].isWinner(theBoard, computerLetter):
                    games[current_game].drawBoard(theBoard)
                    if game_mode == "computer":
                        print('The computer has beaten you! You lose.')
                    elif game_mode == "two player":
                        print("Player 2 wins!")
                    gameIsPlaying = False
                else:
                    if games[current_game].isBoardFull(theBoard):
                        games[current_game].drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'

        # Save the board and starts another game
        if "theBoard" in globals():
            boards.append(theBoard)
            current_game = current_game + 1
        games.append(Tic_Tac_Toe())

        # After the game is over, the user can go to a different page
        play_again = games[current_game].playAgain()
    elif not play_again:
        print("Thank you for playing!")
        break
    elif play_again == "past games":
        games[current_game].recallPastGame()
        play_again = games[current_game].playAgain()

