def add_entry(websites, usernames, passwords):
    websites.append(input("Enter website: ")) 
    usernames.append(input("Enter username: "))
    passwords.append(input("Enter password: "))
def password_keeper (websites, usernames, passwords, i):
    print(f'''\nwebsite: {websites[i]}
password: {passwords [i]}
username:{usernames [i]}''')
def main ():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)
    while True:  
        mode = input("What would you like to do: 1.add 2. print all, 3.print spacific 4. change entry 5. break ")

        if mode == "5":
            break
        elif mode == "1":
            add_entry(websites, usernames, passwords)
        elif mode == "2":
            for i in range(len(websites)):
                password_keeper(websites,usernames,passwords, i)
        elif mode == "3":  
            website = input("what website do you want to print: ")  #ask the user for the website they want to print

            if website in websites:
                password_keeper(websites,usernames,passwords, websites.index(website)) #call password_keeper with websites,usernames,passwords, and index
        elif mode == "4":
            website = input("what website do you want to change: ") #ask the user for the website they want to print

            if website in websites:
                i = website.index(website) #find the index of website in websites
                usernames[i] = input("New username: ")#set usernames at index to input("New username: "
                passwords[i] = input("New passowrd: ")#set passwords at index to input("New password: ")


main()
