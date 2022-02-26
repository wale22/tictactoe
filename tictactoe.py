"""tictactoe designed using python """ 

# this is a demo layout showing the locations of points in the game
def boardDemo():
    print("0" + '|' + "1" + '|' +"2" )
    print('-+-+-')
    print("3" + '|' + "4" + '|' + "5")
    print('-+-+-')
    print("6" + '|' + '7' + '|' + "8")

#board demo function call
boardDemo()

# a list data structure holding values of location or point on the game board
boardplan = [' ',' ',' ',' ',' ', ' ', ' ', ' ',' ']

# a function to draw the board
def showboard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

""""" a function to check if a player has won"""""
def checkingwins(board,turn):
    # list containing locations on the board of the letter current player is using  
    tested=[]
    #a loop to add locations on the board of the letter current player is using 
    for i in range(len(board)):
        # checking if the location contains letter current player is using
        if board[i]==turn:
            # appending location to the list
            tested.append(i)
    """"sorting locations in the tested list, to prepare it for looping """""
    tested.sort()
    # looping through tested to know if player has won
    for i in tested:
        # list containing number deviced by wale to know if current player has won 
        mgn=[1,3,4]
        #looping through the list to know if current player has won
        for j in mgn:
            if j+i in tested:
                if j+j+i in tested:
                    return True

# list that contains location on the board filled with datas
choosen_spt=[] 
"""this is the main looping it runs the game and displays the game board after updating  it
 """
turn='x'

for i in range(len(boardplan)):
    print('brought to you by wale')
    # calling of function to display the board
    showboard(boardplan)
    # getting location that a player wants to input the letter  
    location=int(input('choose your the location you want to place '+ turn +' '))
    #checking if the location is already occupied
    if location in choosen_spt:
        print('spot is already choosen')
    else:   
        choosen_spt.append(location)
        boardplan[location]=turn

    if checkingwins(boardplan,turn):
        print('the player using '+ turn +' wins')
        break
    else:
        if turn=='x':
            turn='o'
        elif turn=="o":
            turn='x'



