board=["-","-","-","-","-","-","-","-","-"]
finish=False
currentPlayer="X"
def displayBoard():
    print(board[0], "|", board[1], "|", board[2],"     1 | 2 | 3")
    print(board[3], "|", board[4], "|", board[5],"     4 | 5 | 6")
    print(board[6], "|", board[7], "|", board[8],"     7 | 8 | 9")
def changeTurn():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    elif currentPlayer=="O":
        currentPlayer="X"
def turn():
    global currentPlayer
    valid=False
    while not valid:
        chosenLocation=input("{}'s turn. Choose a location to continue: ".format(currentPlayer))
        if chosenLocation in ["1","2","3","4","5","6","7","8","9"]:
            chosenLocation=int(chosenLocation)-1
            if board[chosenLocation]!="-":
                print("The position you entered is already filled.")
            else:
                valid = True
        else:
            print("You entered a valid input.")
    board[chosenLocation]="{}".format(currentPlayer)
def winCheck():
    global finish
    global currentPlayer
    if (board[0]==board[1]==board[2]!="-")or(board[3]==board[4]==board[5]!="-")or(board[6]==board[7]==board[8]!="-"):
        finish=True
        print("{} won the game.".format(currentPlayer))
    elif (board[0]==board[3]==board[6]!="-")or(board[1]==board[4]==board[7]!="-")or(board[2]==board[5]==board[8]!="-"):
        finish=True
        print("{} won the game.".format(currentPlayer))
    elif (board[0]==board[4]==board[8]!="-")or(board[2]==board[4]==board[6]!="-"):
        finish=True
        print("{} won the game.".format(currentPlayer))
    else:
        pass
def main():
    global finish
    global currentPlayer
    while not finish:
        displayBoard()
        turn()
        winCheck()
        changeTurn()

main()