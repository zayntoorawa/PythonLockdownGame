# For the code lets say:
# At the beginning of the code, we have a print to explain the game!
# Then an input asking the user to pree enter to start the game !
# And then we have ten methods one per question they'll be called in sequences from q one to q ten !
# Every method contain  print for the questions and the answers form 1 to 4, and int(input) so the user can pick a number
# Four global variables one per lockdown!
# At the end we have an if condition to print the result depending on the score form the global variables !

import sys
counter_lockdown1=0
counter_lockdown2=0
counter_lockdown3=0
counter_lockdown4=0

def the_game():
 q_one() 
 q_two()
 q_three()
 q_four()
 q_five()
 q_six()
 q_sven()
 q_eight()
 q_nine()
 q_ten()  
 check_the_res()
print("#################################################################################################")
print("#                                   What lockdown are you!                                      #")
print("#                       Find out what lockdown you are from your favourite things!              #")
print("#################################################################################################")

start_the_game= input("                           -_- Press enter to start the game -_-                                        ")

###################### Question 1 ################################
def q_one():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("1-What's your Favourite Season?\n\n")
    # Spring 1, Summer 2, Autumn 3, Winter 4
    print("1-Spring\n2-Summer\n3-Autumn\n4-Winter \n\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_one()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()
    
        
        
        
########################## Question 2 #######################################
def q_two():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("2-What's your Favourite Colour Combination?\n\n")
    #Rainbow 1, Pastel 2, Warm 3, Cool 4    
    print("1-Rainbow\n2-Pastel\n3-Warm\n4-Cool\n\n ")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list:"))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1 
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_two
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()
       




########################## Question 3 #######################################
def q_three():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("3-What's your Favourite Exercise?\n\n")
    # Running 1, Gym 2, Nothing 3, Zoom Workouts 4   
    print("1-Running\n2-Gym\n3-Nothing\n4-Zoom Workouts\n\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 2:
        counter_lockdown1 += 1
    elif the_answer == 1:
        counter_lockdown2 += 1
    elif the_answer == 4:
        counter_lockdown3 += 1
    elif the_answer == 3:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_three()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 4 #######################################
def q_four():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("4-What's your Favourite Mealtime?\n\n")
    # Breakfast 1, Lunch 2, Dinner 3, Brunch 4
    print("1-Breakfast\n2-Lunch\n3-Dinner\n4-Brunch\n\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 3:
        counter_lockdown1 += 1
    elif the_answer == 4:
        counter_lockdown2 += 1
    elif the_answer == 1:
        counter_lockdown3 += 1
    elif the_answer == 2:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_four()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 5 #######################################
def q_five():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("5-What's your Favourite TV Genre?\n\n")
    #TV Genre – Action 1, Romance 2, Horror 3, Comedy 4
    print("1-Action\n2-Romance\n3-Horror\n4-Comedy\n\n ")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 4:
        counter_lockdown1 += 1
    elif the_answer == 3:
        counter_lockdown2 += 1
    elif the_answer == 2:
        counter_lockdown3 += 1
    elif the_answer == 1:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_five()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 6 #######################################
def q_six():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("6-What's your Favourite Music Genre?\n\n")
    # Music Genre – Pop 1, Country 2, R&B 3, Rock 4
    print("1-Pop\n2-Country\n3-R&B\n4-Rock\n\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_six()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 7 #######################################
def q_sven():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("7-What's your Favourite Social Media App?\n\n")
    #Social Media App – House Party 1, Instagram 2, Twitter 3, TikTok 4
    print("1-House Party\n2-Instagram\n3-Twitter\n4-TikTok\n\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_sven()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 8 #######################################
def q_eight():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("8-What's your Favourite Outfit?\n\n")
    #– Loungewear 1, Fancy 2, Work Wear 3, Gym Wear 4    
    print("1-Loungewear\n2-Fancy\n3-Work Wear\n4-Gym Wear\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 4:
        counter_lockdown1 += 1
    elif the_answer == 3:
        counter_lockdown2 += 1
    elif the_answer == 2:
        counter_lockdown3 += 1
    elif the_answer == 1:
        counter_lockdown4 += 1 
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_eight()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()
    




########################## Question 9 #######################################
def q_nine():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("9-What's your Favourite Type of Hoarder?\n\n")
    #Toilet Paper 1, Hand Sanitizer 2, Fruit 3, Cupboard food 4    
    print("1-Toilet Paper\n2-Hand Sanitizer\n3-Fruit\n4-Cupboard Food\n ")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1 
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_nine()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





########################## Question 10 #######################################
def q_ten():
    print("#############################################################################################")
    global counter_lockdown1
    global counter_lockdown2 
    global counter_lockdown3 
    global counter_lockdown4 
    print("10-What's your Favourite Pass Time?\n\n")
    #Reading 1, Gaming 2, Watching TV 3, Learning a New Skill 4,
    print("1-Reading\n2-Gaming TV\n3-Watching TV\n4-Learning a New Skill\n")
    print("Press 0+Enter to skip - 9+Enter to exit the game - 8+Enter to restart the game\n")
    print("Pssst... Type the numbers not the words!\n")
    the_answer= int(input("Select form the list: "))
    if the_answer == 1:
        counter_lockdown1 += 1
    elif the_answer == 2:
        counter_lockdown2 += 1
    elif the_answer == 3:
        counter_lockdown3 += 1
    elif the_answer == 4:
        counter_lockdown4 += 1 
    elif the_answer not in [1, 2, 3, 4, 9, 0, 8]:
        print("          \nPlese select from the above list !          ")
        q_ten()
    elif the_answer == 9:
        print("Thanks !")
        sys.exit()
    elif the_answer == 0:
        pass
    elif the_answer == 8:
        the_game()





def check_the_res():
    def computer():
        print("         ,---------------------------,                  ")
        print("         |  /---------------------\  |                  ")
        print("         | |                       | |                  ")
        print("         | |       THANK YOU       | |                  ")
        print("         | |          FOR          | |                  ")
        print("         | |        PLAYING!       | |                  ")
        print("         | |                       | |                  ")
        print("         |  \_____________________/  |                  ")
        print("         |___________________________|                  ")
        print("        ,---\_____     []     _______/------,           ")
        print("        /         /______________\           /|         ")
        print("       /___________________________________ /  |__      ")
        print("      |                                   |   |   )     ")
        print("      |  _ _ _                 [-------]  |   |  (      ")
        print("      |  o o o                 [-------]  |  /    )_    ")
        print("      |__________________________________ |/    /  /    ")
        print("     /-------------------------------------/   /()/     ")
        print("    /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-//            ")
        print("   /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-//             ")
        print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               ")

    if counter_lockdown1 > counter_lockdown2 and counter_lockdown1> counter_lockdown3 and counter_lockdown1 >counter_lockdown4:
        print("*************************************************************************************")
        print("*                                  You are in Lockdown One!                         *")
        print("You love to stick to the rules, and you really value the key workers who keep you safe.\n#ClapfortheNHS")
        print("*************************************************************************************")
        computer()
    elif counter_lockdown2 > counter_lockdown1 and counter_lockdown2> counter_lockdown3 and counter_lockdown2 >counter_lockdown4:
        print("*************************************************************************************")
        print("*                                   You are in Lockdown Two!                        *")
        print("You are a party animal and love to be round your friends having fun and enjoying food!\n#EatOuttoHelpOut")
        print("*************************************************************************************")
        computer()
    elif counter_lockdown3 > counter_lockdown1 and counter_lockdown3> counter_lockdown2 and counter_lockdown3 >counter_lockdown4:
        print("*************************************************************************************")
        print("*                                     You are in Lockdown Three!                    *")
        print("Back inside again! You love to troll the forums and addicted to watching Boris \n“try” and control the nation. #ChristmasTiers")
        print("*************************************************************************************")
        computer()
    elif counter_lockdown4 > counter_lockdown1 and counter_lockdown4> counter_lockdown2 and counter_lockdown4 >counter_lockdown3:
        print("*************************************************************************************")
        print("*                               You are in Lockdown Four!                           *")
        print("Time to achieve those new year’s resolutions! That is all you can do anyways…\n#Lockdownneverends")
        print("*************************************************************************************")
        computer()
    
    ending_option=input("Type E+Enter to exit the game or P+Enter to play again -_-")
    if ending_option == "E":
        print("Thanks !")
    elif ending_option=="P":
       the_game()

        
        



q_one() 
q_two()
q_three()
q_four()
q_five()
q_six()
q_sven()
q_eight()
q_nine()
q_ten()  
check_the_res() 
the_game()
# print(counter_lockdown1)
# print(counter_lockdown2)
# print(counter_lockdown3)
# print(counter_lockdown4)



