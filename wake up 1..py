print ("Alarm")
print ("snooze")
print ("ALARM")

while True:
    snooze = str.lower(input("snooze alarm? "))

    if (snooze == "no"):
        print ("wake up")
        break
    elif snooze == "yes":
        print("sleep for 5 min")
    else:
        print("Invalid")

while True:
    dressed = str.lower(input("get dressed? "))

    if (dressed == "yes"):
        print("ok, get dressed")
        break 
    elif (dressed == "no"):
        print ("go to school in pjs")
        break
    else:
        print("Invalid")
        
while True:     
    eat_at_home = str.lower(input("eat at home? "))

    if eat_at_home == "yes":
        print("eat then go to school")
        break 
    elif (eat_at_home == "no"):
        print("eat at school!")
        break
    else:
        print("Invalid")


while True:    
    eat_a_bagle = str.lower(input ("eat a bagle? "))

    if (eat_a_bagle == "yes"):
        print ("eat a bagle")
        break 
    elif (eat_a_bagle == "no"):
        print (" don't eat")
        break
    else:
        print("Invalid") 
      

