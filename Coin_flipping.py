import random


options = ['heads', 'tails'] 
number_of_times_correct = 0
wrong = 0 

while True:
    user_input = input("Want to play a game of heads & tails? Enter Q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,1)
    # heads:0 ; tails: 1

    computer_pick = options[random_number]
    if user_input == computer_pick:
            number_of_times_correct += 1
            print("That's correct!")
            continue

    else:
        print("Sorry that's incorrect!")
        wrong += 1
        

print("You have been correct", number_of_times_correct, "times!")
print("You were wrong", wrong, "times!")
print("Alright, it's time to move around.")



    
    

    
    


    

