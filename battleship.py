# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    ship_names = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    board1 = [[["-" for i in range(board_size)] for j in range(5) for y in range(2)] for t in range(2)]
    board2=[[["-" for i in range(board_size)] for j in range(5) for k in range(2)] for w in range(2)]

    ships_place = {'Carrier': 0, 'Battleship': 0, 'Cruiser': 0, 'Submarine': 0, 'Destroyer': 0}
    placement = 0
    k=0
    while not k == 2:  #while loop for two players to place their ship until k is equal to 2.
        while placement < len(ship_names):  #placement is control statement, ship_names is a descending list as ships are placed;therefore, loop exit when ship_names' number of elements is equal to 0.
            print_3d_list([board1[k],board2[1-k]])  #printing board acording to final placement
            print_ships_to_be_placed()
            for i in ship_names:          #indicating the remaining ships
                print_single_element(i)
            print_empty_line()
            print_player_turn_to_place(k+1)  #k is a control variable to determine which player's turn it is.
            print_to_place_ships()
            inf_input = input().capitalize().split()  #input is taken from user.
            inf_input = inf_input[:4]
            try:
                x=int(inf_input[1])
                y=int(inf_input[2])
            except:
                pass                               #Errors show to user that their input is somehow incorrect.
            if not str(inf_input[1]).isdigit():
                print_incorrect_input_format()     #many type of error for each case.
                continue
            elif not str(inf_input[2]).isdigit():
                print_incorrect_input_format()
                continue
            elif int(inf_input[1])==0:
                print_incorrect_coordinates()             #ERRORS
                continue
            elif int(inf_input[2])==0:
                print_incorrect_coordinates()
                continue
            elif len(inf_input) < 4:
                print_incorrect_input_format()
                continue
            elif int(inf_input[1]) > 10:
                print_incorrect_coordinates()
                continue
            elif int(inf_input[2]) > 10:
                print_incorrect_coordinates()
                continue
            elif inf_input[0] not in ships.keys():
                print_incorrect_ship_name()
                continue
            elif inf_input[3] != 'h' and inf_input[3] != 'v':
                print_incorrect_orientation()
                continue
            elif ships_place[inf_input[0]] == 1:
                print_ship_is_already_placed(inf_input[0])  #if there is an error in input,due to continue, inut is taken again fromm user.
                continue
            else:     #in case of there is not any error, placement part is starting.
                if inf_input[3]== "h": #if decides whether placement will be horizontal or vertical.
                    if int(inf_input[1])+ships[inf_input[0]]>11:
                        print_ship_cannot_be_placed_outside(inf_input[0])
                        continue
                    for a in range(ships[inf_input[0]]):
                            flag = True  #flag is for controlling two errors
                            if k==0: #for player 1
                                if board1[0][y-1][x-1+a]=="#":
                                    flag = False #if there is already a ship part in coordinates that is given by user, flag returns to false and error is printed then control loop is exit.
                                    print_ship_cannot_be_placed_occupied(inf_input[0])
                                    break
                            if k==1: #for player 2
                                if board2[0][y-1][x-1+a]=="#":
                                    flag = False #again for control
                                    print_ship_cannot_be_placed_occupied(inf_input[0])
                                    break #if cannot place, break the loop and and same circle again.
                if inf_input[3] == "v":  #for vertical placement's control of two situation
                    if int(inf_input[2]) + ships[inf_input[0]] > 11:
                        print_ship_cannot_be_placed_outside(inf_input[0])
                        continue
                    for a in range(ships[inf_input[0]]): #control for loop
                        flag = True #control variable
                        if k==0: #for player 1
                            if board1[0][y-1+a][x-1]=="#":
                                flag = False #returning false to break the loop
                                print_ship_cannot_be_placed_occupied(inf_input[0]) #printing the error
                                break
                        if k==1: #for player 2
                            if board2[0][y-1+a][x-1]=="#":
                                flag = False
                                print_ship_cannot_be_placed_occupied(inf_input[0])
                                break
                if not flag: #if false, go back to loop and flag is again true, then inside the loop until flag is true.
                    continue
                if inf_input[3]== "h": #controlling is over,now place the ships horizontally without any errors
                    if k==0: #player 1
                        for a in range(ships[inf_input[0]]):
                            board1[0][y - 1][x - 1 + a] = "#"
                    if k == 1: #player 2
                        for a in range(ships[inf_input[0]]):
                            board2[0][y - 1][x - 1 + a] = "#"

                if inf_input[3] == "v": #placing vertically
                    if k == 0:
                        for a in range(ships[inf_input[0]]):
                            board1[0][y - 1+a][x - 1] = "#"
                    if k == 1:
                        for a in range(ships[inf_input[0]]):
                            board2[0][y - 1 + a][x - 1] = "#"
                ship_names.remove(inf_input[0]) #remove ships names from list as they are placed to display only the remaining ships
                ships_place[inf_input[0]] = 1 #in a dictionary, already placed ships' values are changed to 1 from 0.

        conf = ""   #confirmation part
        cont = False
        print_3d_list([board1[k], board2[1 - k]])
        while conf != "Y" and conf!="N":  #only if input is y,n,N or Y
            print_confirm_placement()
            conf= input().capitalize() #input is taken from user as string and return to integers
            if conf=="Y": # if player 1 confirms the ships' places, k increases 1 and it is player 2's turn to place ships.
                k+=1
                cont=True #to break the loop and exit
                ship_names = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"] #lists and dictionary should return the first form to repeat the same things again.
                ships_place = {'Carrier': 0, 'Battleship': 0, 'Cruiser': 0, 'Submarine': 0, 'Destroyer': 0}
                break #exit the loop
            elif conf=="N": #if placement is not confirmed by players, k will not increase, and the same player will place the ships.
                cont=True #to exit the loop
                if k==0: #for player 1
                    board1[0] = [["-" for i in range(board_size)] for j in range(5) for k in range(2)] #board should be reset in order to place it again.
                    ship_names = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"] #list should be reset too.
                    ships_place = {'Carrier': 0, 'Battleship': 0, 'Cruiser': 0, 'Submarine': 0, 'Destroyer': 0} #dictionary should be reset too.
                    break #exit the loop
                elif k==1: #for player 2
                    board2[0] = [["-" for i in range(board_size)] for j in range(5) for k in range(2)]
                    ship_names = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]
                    ships_place = {'Carrier': 0, 'Battleship': 0, 'Cruiser': 0, 'Submarine': 0, 'Destroyer': 0}
                    break
            else:
                continue #if cont is not N or Y take input again.
        if cont==True:
            continue
    print_3d_list([board1[0],board2[1]]) #print the board once
    cont2=True #control statement
    while cont2==True:
        turn = 0
        control3=True
        whose_turn =0 #to determine the whose turn it is.
        hits_of1=0 #counter of hits for player 1
        hits_of2=0 #counter of hits for player 2
        while control3:
            if hits_of1==17:  #this ifs for end the game when one player reaches the 17 hit score.
                # print_3d_list([board1[0],board2[1]])
                print_player_won(1)
                print_thanks_for_playing()
                cont2=False
                control3=False
                break
            if hits_of2==17:
                # print_3d_list([board1[1],board2[0]])
                print_player_won(2)
                print_thanks_for_playing()
                cont2 = False
                control3 = False
                break
            if whose_turn==0: #this part for player 1's turn to strike
                print_player_turn_to_strike(whose_turn+1)
                print_choose_target_coordinates()
                coord_input = input().split()
                try:                                #printing errors for acquiring the proper input
                    cx = int(coord_input[0])
                    cy = int(coord_input[1])
                    if cx > 10:
                        print_incorrect_coordinates()
                        print_3d_list([board1[0], board2[1]])
                        continue
                    if cy > 10:
                        print_incorrect_coordinates()
                        print_3d_list([board1[0], board2[1]])
                        continue
                except:
                     print_incorrect_input_format()
                     print_3d_list([board1[0], board2[1]])
                     continue
                if board2[0][cy-1][cx-1]=="!":
                    print_tile_already_struck()
                    print_3d_list([board1[0], board2[1]])
                    continue                                    #ERRORS
                elif board2[0][cy-1][cx-1]=="O":
                    print_tile_already_struck()
                    print_3d_list([board1[0], board2[1]])
                    continue
                if len(coord_input)<2:
                    print_incorrect_input_format()
                    print_3d_list([board1[0], board2[1]])
                    continue
                if board2[0][cy-1][cx-1]=="#":
                    print_hit()
                    board2[0][cy-1][cx-1]="!"
                    board2[1][cy-1][cx-1]="!"
                    print_3d_list([board1[0],board2[1]])
                    hits_of1+=1
                    continue
                elif board2[0][cy-1][cx-1]=="-":  #if there is no ship part(#) player miss and other player's turn to strike.
                    print_miss()
                    print_type_done_to_yield(2)
                    done_cont=input().lower() #taking input for done
                    cont5=True
                    while cont5==True:
                        if done_cont!='done':
                            print_type_done_to_yield(2)
                            x2=input().lower()
                            if x2=='done':
                                whose_turn+=1  #after player 1 give the chance to player1 control is increasing 1 to enter second player's loop
                                break #breaking the loop
                            else:
                                continue #if still input is not correct do not break, continue.
                        elif done_cont=='done':
                            whose_turn+=1 #correct input, break the loop.
                            break
                    board2[0][cy - 1][cx - 1] = "O" #miss symbol for both player's boards.
                    board2[1][cy - 1][cx - 1] = "O"
                    print_3d_list([board1[1],board2[0]]) #the board which player 2' see and player 2's own board.
                    turn+=1
            if whose_turn==1: #player 2's turn to strike
                print_player_turn_to_strike(whose_turn + 1)
                print_choose_target_coordinates()
                coord_input = input().split() #coordinate inputs
                try:
                    cx = int(coord_input[0])   #controlling if it is integers or not
                    cy = int(coord_input[1])
                except:
                    print_incorrect_input_format()
                    print_3d_list([board1[1], board2[0]])      #printing errors
                    continue
                if board1[0][cy-1][cx-1]=="!":  #! symbol means that coordinates are struck
                    print_tile_already_struck()
                    print_3d_list([board1[1], board2[0]])
                    continue
                elif board1[0][cy-1][cx-1]=="O": #O symbol means that coordinates are struck
                    print_tile_already_struck()
                    print_3d_list([board1[1], board2[0]])
                    continue
                if len(coord_input) < 2:
                    print_incorrect_input_format()
                    print_3d_list([board1[1], board2[0]])     #ERRORS
                    continue
                elif cx > 10:
                    print_incorrect_coordinates()
                    print_3d_list([board1[1], board2[0]])
                    continue
                elif cy > 10:
                    print_incorrect_coordinates()
                    print_3d_list([board1[1], board2[0]])
                    continue

                if board1[0][cy-1][cx-1]=="#":  #player 2's hit part
                    print_hit()
                    board1[0][cy-1][cx-1]="!"
                    board1[1][cy-1][cx-1]="!"
                    print_3d_list([board1[1],board2[0]])
                    hits_of2+=1
                    continue
                elif board1[0][cy-1][cx-1]=="-":  #player 2's miss part
                    print_miss()
                    print_type_done_to_yield(whose_turn)
                    done_cont2=input().lower()
                    cont6 = True
                    while cont6 == True:
                        if done_cont2 != 'done':            #same done control as above
                            print_type_done_to_yield(whose_turn)
                            x3 = input().lower()
                            if x3 == 'done':
                                whose_turn-= 1
                                break
                            else:
                                continue
                        elif done_cont2 == 'done':
                            whose_turn-=1
                            break
                    board1[0][cy - 1][cx - 1] = "O"
                    board1[1][cy - 1][cx - 1] = "O"
                    print_3d_list([board1[0],board2[1]])









    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
      f.close()
