##python project of tictactoe game
board =[" " for _ in range(9)]

def printboard():
    print("\n")
    for i in range(3):
        for j in range(3*i,3*(i+1)):
            print("|",board[j],end="")
        print("|")
    print("\n")

def playgame():
    global board
    board=[" " for _ in range(9)]
    printboard()
    plays=1
    while(plays<=9):
        if(plays%2!=0):
            i=int(input("Player 1: "))
            if board[i-1]!=" ":
                print("square",i,"is already taken enter another input \n")
                continue
            board[i-1]="O"
            
        else:
            i=int(input("Player 2: "))
            if board[i-1]!=" ":
                print("square",i,"is already taken enter another input \n")
                continue
            board[i-1]="X"
        printboard()
        plays+=1
        win=" "
        if(plays>=5):
            #checking if anybody won the game
            #checking horizontal lines
            for i in range(0,9,3):
                if(board[i]==board[i+1] and board[i]==board[i+2] and board[i]!=" "):
                    win=board[i]
            #checking vertical lines
            for i in range(0,3):
                if(board[i]==board[i+3] and board[i]==board[i+6] and board[i]!=" "):
                    win=board[i]
            #checking diagonals
            if (board[0]==board[4] and board[8]==board[4]) or (board[2]==board[4] and board[6]==board[4]):
                win=board[4]
            if win!=" ":
                print(win,"won the game \n")
                break
    #if match is drawn
    if(win==" "):
        print("match is draw \n")
            
def game():
    while True:
        i=input("do you want to play tic tac toe (y/n):")
        if(i=="y" or i=="Y"):
            playgame()
        else:
            break


if __name__=="__main__":
    game()
