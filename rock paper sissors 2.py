'''
Auther: Addison Polo
Discroiption: The comouter is playing RPS 
Date: 12/1/23
Bugs: I have no bugs 
Challenges: A chalenge 
'''

import random # enters the random library so you can use random functions

rps_options = ['rock', 'paper', 'sissors'] # the list of options to play in the game

while True: #an infinite loop (while condition true, is true)
    play = str.lower(input ("do you want to play rock papaer sissors? ")) # this is asking if you want to play RPS and will continue to ask until user unputs yes 
    if play == "no": # user imputs no this is an invalid aswer
        break # ends the loop 
    elif play == "yes":# user imputs yes 
        print ("you go first") # if user inputs yes then the program will print you go first 
        user_input = input("rock, paper, sissors shoot: ")# inputs the list 
        bot = random.choice(["rock", "paper", "scissors"])# radomly generated responce 

        print(f"User chose {user_input} and bot chose {bot}")# the user goes first then the program generates a responce 

        if user_input == bot: # If the user and bots responce is the smae it is a tie 
            print("tie") # printing a tie 
        elif user_input == "rock" and bot == "paper": # if user inputs rock and bot enters paper
            print("Bot won!")# then print bot won
        elif user_input == "rock" and bot == "scissors": # if user intputs rock and bot inouts scissors 
            print ("User won!")# then print user won 
        elif user_input == "paper" and bot == "scissors": # if user inputs paper and bot inputs scissers 
            print("Bot won!") # then print bot won
        elif user_input == "paper" and bot == "rock": # if user inputs paper and bot inputs rock 
            print ("Bot won!")# then print bot won 
        elif user_input == "scissors" and bot == "paper": # if user inputs scissors and bot inputs paper 
            print ("User won!") # then print user won 
        elif user_input == "scissors" and bot == "rock": # if user inputs scissors and bot inputs rock 
            print ("Bot won")# then print bot won 
    else:
        print ("Invalid")# if user inputs anything els then porgram will print invalid until a valid aswer 
    

        



        

