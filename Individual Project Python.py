# Name of the project: Individual Project Germán Germán De Souza
# Description: IPE on Human Behaviour Prediction Game with two different levels of difficulty
# Author: Germán Germán De Souza
# Last Updated: 7th of February 2021
from mypackage.demo import linear_congruence # First of all, we have to use the function random linear_congruance and define all the variables within this py file before we start the game
################################################################################################################################################################################################################################################
def game_difficulty(): # game_difficulty is used to extract the game difficulty that the user wants to play. This section has been purposely desined to catch any errors that deviate from the actual value that we are requesting (int) - Try and except have been used to avoid this. Also follows a while loop until it gathers the desired output.
    global difficult_level
    while True:
        try :
            difficult_level = int(input("Choose the type of game (1:Easy; 2:Dificult):"))
            if difficult_level == 2:
                difficult_level=2
                moves_number()
                break
            elif difficult_level == 1:
                difficult_level=1
                moves_number()
                break
            elif difficult_level > 2: print("We dont have that many levels yet, please select the options below")
        except ValueError: print("Please don't insert alphanumeric values nor decimals, insert 1:Easy or 2:Dificult")

def moves_number(): # moves_number gets the number of moves that the user wants to play the game. This section has been purposely desined to catch any errors that deviate from the actual value that we are requesting (int) - Try and except have been used to avoid this. Also follows a while loop until it gathers the desired output.
    global moves_level
    while True:
        try:
            num_moves= int(input("Enter the number of moves:"))
            if num_moves > 0:
                moves_level=num_moves
                break            
        except ValueError: print("Please don't insert alphanumeric values nor decimals, the number of trials have to be rounded numbers")             

def trial_output(): # trial_output will be used in the function play_game. This function will evaluate the values from the user and the computer and print a personalised message based on the logic below.
    global MS,PS
    if player_trial == 0 and computer_trial == 0:
        MS = MS + 1
        print("player = 0 machine = 0 - Machine wins! \nYou: {} Computer: {}".format(PS,MS))
    elif player_trial == 0 and computer_trial == 1:
        PS = PS + 1
        print("player = 0 machine = 1 - Player wins! \nYou: {} Computer: {}".format(PS,MS))
    elif player_trial == 1 and computer_trial == 0:
        PS = PS + 1
        print("player = 1 machine = 0 - Player wins! \nYou: {} Computer: {}".format(PS,MS))
    else:
        MS = MS + 1
        print("player = 1 machine = 1 - Machine wins! \nYou: {} Computer: {}".format(PS,MS))
    print("PLAYER: "+"*"*PS)
    print("COMPUTER: "+"*"*MS)

def play_game(): # play_game is the main core of the game, it repeats the game n number of times (from the function "moves_number") and depending on the game difficulty it will use other functions and a different computation.
    global player_input_game,computer_trial,player_trial,xi,MW,PW
    xi=1234
    player_input_game=[]
    for i in range(1,moves_level+2):
        if i<=moves_level: # If the moves_level is below the ones inputed by the user it will continue executing this chunk.
            while True:
                try:
                    player_trial=int(input("ROUND"+ str(i) +" Choose your move number for round: "+ str(i) +",(0 or 1): "))
                    if player_trial == 0 or player_trial == 1: # If the player trial is either a 1 or a 0, then append the throw into the accumulated list and the current game list.
                        player_input_acc.append(player_trial)
                        player_input_game.append(player_trial)
                        if difficult_level==1: # If the "player_trial" is either a 1 or a 0 and the game difficulty is 1, then get the computer trial from "linear_congruence" and evaluate the results in "trial_output".
                            computer_trial, xi = linear_congruence(xi)
                            trial_output()
                            break
                        elif difficult_level==2 and i==1: # If the "player_trial" is either a 1 or a 0, the game difficulty is 2 and we are in the first round, then get the computer trial from the function "difficult" and evaluate the results in "trial_output".
                            computer_trial = difficult(player_trial)
                            trial_output()
                            break
                        elif difficult_level==2 and i>1: # If the "player_trial" is either a 1 or a 0, the game difficulty is 2 and the round is higher than round 1, then analyse the users last move with the function "comp_predictor", re-evaluate the computer trial with the new parameters from the function "difficult" and evaluate the results in "trial_output".
                            last_player_num=player_input_game[i-1]
                            comp_predictor(last_player_num)
                            computer_trial = difficult(player_trial)
                            trial_output()
                            break
                    else:
                        print("We just have 2 options, either 0 or 1") #If the user inputs a value that is bigger than 1 or smaller than 0, this message will loop until the user inputs the expected value.
                except ValueError: print("It just accepts integers that are either 1 or 0") #If the user inputs a value that is not a 0 nor a 1, this message will loop until the user inputs the expected value.
        elif i>moves_level: # If the moves_level is above the inputed by the user it will stop and evaluate the results to print the winner of the game.
            if difficult_level==1 and MS>PS:
                MW=MW+1
                print("\nEasy game is over, final score: player {} - {} computer - The COMPUTER won!".format(PS,MS))
            elif difficult_level==1 and MS<PS:
                PW=PW+1
                print("\nEasy game is over, final score: player {} - {} computer - The PLAYER won!".format(PS,MS))
            elif difficult_level==1 and MS==PS:
                PW,MW=[PW+1,MW+1]
                print("\nEasy game is over, final score: player {} - {} computer - It was a tie!".format(PS,MS))
            elif difficult_level==2 and MS>PS:
                MW=MW+1
                print("\nDifficult game is over, final score: player {} - {} computer - The COMPUTER won!".format(PS,MS))
            elif difficult_level==2 and MS<PS:
                PW=PW+1
                print("\nDifficult game is over, final score: player {} - {} computer - The PLAYER won!".format(PS,MS))
            elif difficult_level==2 and MS==PS:
                PW,MW=[PW+1,MW+1]
                print("\nDifficult game is over, final score: player {} - {} computer - It was a tie!".format(PS,MS))
            play_again() # It will ask the user if he wants to play again, this refers to the function "play_again".   
                    
def difficult(x): # difficult it is used to evaluate the compter trial in difficulty number 2, this is a evaluation layer in my code to analyse the users moves and predict what could be his next move. Based on that data, this code will determine the adequate value for "computer_trial" in specific rounds.
    global xi
    if x == 0 and throw_10>throw_00: a=1
    elif x == 0 and throw_10<throw_00: a=0
    elif x == 0 and throw_10==throw_00: a,xi=linear_congruence(xi)
    elif x == 1 and throw_11>throw_01: a=1
    elif x == 1 and throw_11<throw_01: a=0
    elif x == 1 and throw_11==throw_01: a,xi=linear_congruence(xi)
    return(a)

def comp_predictor(x): # Computer_predictor will start when we arrive to the second round of difficulty 2. This is an algorith that analyses the users last move and counts the accumulated player_trials taht correspond to the last_player_trial. This score is constatly changing every round. It can be seen by the assignation of global for each throw.
    global throw_00,throw_10,throw_01,throw_11
    if x==0:
        throw_00,throw_10=[player_input_acc.count(0),player_input_acc.count(1)]
    if x==1:
        throw_01,throw_11=[player_input_acc.count(0),player_input_acc.count(1)]

def play_again(): # This is the final stage of the game or the stage which the player can play again. If the player doesnt want to play again, it will print the times which each player and computer won the game. However, if the player wants to play again, it will loop the game again without reseting the player throws.
    global MS,PS
    confirmation=input("Would you like to play again (yes or no)? ")
    if confirmation.lower()=="yes":
        MS,PS=[0,0]
        game_difficulty()
        play_game()
    elif confirmation.lower()=="no": 
        print("\nTotal Player Wins: {} \nTotal Computer Wins: {} \nSee you next time!".format(PW,MW))
    else:
        while True: # Also, the code was designed, if the user inputs a value that is totally different from the desired, then it will return a warning message. Try and except has been used, also it will be looped repetitive times until the user inserts the desired output.
            start2= input("\nSorry, You have written something different from what we were asking. Do you still want to play this game (yes or no)? ")
            if start2.lower()=="yes":
                MS,PS=[0,0]
                game_difficulty()
                play_game()
                break
            elif start2.lower()=="no":
                print("\nTotal Player Wins: {} \nTotal Computer Wins: {} \nSee you next time!".format(PW,MW))
                break
################################################################################################################################################################################################################################################
player_input_acc=[] # From here onwards I am creating the function in the global environment and executing just "game_difficulty" and "play_game". As these functions are interconnected in their definition, there is no need to call other functions.
MS,PS,MW,PW,throw_10,throw_00,throw_11,throw_01=[0,0,0,0,0,0,0,0] 
print("\nWelcome to Human Behaviour Prediction by Germán Germán De Souza")
game_difficulty()
play_game()


