'''
Author: Addison Polo
Date: 11/14/23
Description: Ask the program quesstions, and it will give yes, no answers until you tell it to stop.
Bugs: None 
Challenges: It will keep askwering questions until you say stop
Sources: None 
'''

import random #bring in random library for random function uses 

while True:# an infinite loop (while condition true, is true)
    question = input("Enter a question: ")#telling the user to ask a question 

    if question == "stop": #if you answer prompt with stop 
        break #end the loop 
    
    print(random.choice(["yes" , "no" ,"maybe"]))#printing a rondomly selection of thoes asnwers 

