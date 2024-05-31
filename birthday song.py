'''
Author: Addison Polo
Date: 4/19/2024
Challenges: None
Sources: Ms. Marciano
'''


import random
#def functin_name(inputs):
    #action
    #output (print or return)
def chorus():# function to print the chorus of happy birthday 
    print ("Happy birthday to you!, Happy birthday to you!")
def sing(name): #function to print the whole happy birthday song
    chorus ()#calls the chorus
    print (f"Happy birthday dear, {name}")
    print ("happy birhtday to you!")
    chorus ()
def add (number1, number2): # function to take two numbers and print there sum 
    print (number1 + number2) # adds number1 and number2 
def print_list(my_list): # function to Takes a list and prints every element in that list individually (vertically)
    for element in my_list:
        print(element)
def is_int(number): # funtion to check if given pramitore is an intiger 
    try: # exicuting code without fully exicuting 
        number = int(number) #
        return True # if true, program with return true 
    except ValueError: # if false 
        return Fase # program will return false 
def contains_element(my_list, element): # 
    if element in my_list: # if the element is in the list 
        return True # then the program will return true 
    else: # otherwise 
        return False # if the element is not in the list then the program will return false 
def is_positive_intenger(string):#
    if string.isnumeric ():#
        return True # if true, return true 
    else: # otherwise 
        return False # if false, return false 
def get_random(): # funtion to Prompts the user for two numbers and prints a random number between the two
    num1= input ("Enter #:") # asking user to input a number 
    num2= input ("Enter #:") # asking user to input a second letter 
    while True:
        if is_int(num1) and is_int(num2): #
            print (random.randint(1,10))# the program will print a random number between 1,10
            break # 
        else:
            print ("please enter a print")  # the program will ask the user to enter a print    
def replace_character (word, old_letter, new_letter): # function to take a string and two characters, then replaces every instance in the string of the first character with the second
    new_word = ""
    
    for letter in word: #
        if letter == old_letter: #
            new_word += new_letter#
        else: #
            new_word += letter#
    return new_word#
def main(): # 
    name = input("enter name: ") # asking user to enter name 
    sing(name)# calling sing function 
    num1 = int(input("Enter number 1: "))# aking user to ender number 
    num2 = int(input("Enter number 2: "))# aking user to ender number 
    add(num1,num2)
    my_list1 =["where","who","when"] #
    print_list(my_list1) # printing my list 
    print (contains_element(my_list1, "where")) # pritnting each element from my list indavisaily 
    print (contains_element(my_list1, "how"))  # pritnting each element from my list indavisaily   
    print (is_positive_intenger("-4"))# pritnting each element from my list indavisaily 
    get_random()
    print (replace_character("hello","l","a")) # cheching if code can replace a old letter 

main() #

