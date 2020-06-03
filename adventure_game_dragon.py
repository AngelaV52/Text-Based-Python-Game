# Group Project
import random

user_name = input("What is your name brave adventurer? ")
while user_name == "":
    user_name = input("That was not a name. Try again: ")
print("")

print("In front of you", user_name + ",", "is the dragon's cave.")
print("There is only darkness ahead of you. You hold up your sheild in one hand and torch in the other. A sword is belted at your side.")
print("You are on a quest to find the treaure hidden within the cave and return it to your king.")
print("You will be forced to make decisions that may seem simple, but are very deadly. If you make the wrong decision, you may die.")
print("")

while True:
    ans1 = input("Do you choose to enter, yes or no? ")
    if ans1 == "yes" or ans1 == "Yes":
        break
    else:
        print("Wrong decision")

print("")

while True:
    user_choice = input ("Type 'Great Hall' to continue: ")
    if user_choice == "Great Hall":
        break
    else:
        print("That is not an option.")

print("\n")
user_choice == "Great Hall"
while user_choice != "exit":
    # the player is in Great Hall
    if user_choice == "Great Hall":
        print("Welcome to the Great Hall! This is where the king's loyal subjects come to revel in his majesty's gracious ruling.")
        print("Type 'exit' to leave anytime.")
        print("The walls are covered in gigantic oil paintings of the royal family. The paintings are coated with dust and cobwebs.")
        print("\n")
        print("You see multiple hallways leading out of the Great Hall.")
        user_choice= input("Choose where you would like to search next: 'Magician's Hall', 'Dining Room', or 'Dwarf's Armory': ")
        # this is if player chooses the Magician's Hall, Dwarf's Armory, or Dinning Room
        if user_choice == "Magician's Hall":
            print("")
            print("The Magician's Hall is made of many traps and tricks. The magicians use to practice often here before the dragon took over this cave.")
            death = random.randint (1,50)
            if death > 37:
                print ("You accidently step on a trap left by the magicians for the evil dragon. Better luck next time.")
                break
            print("On your left is a beautiful library, full of books written in languages you do not recognize. The book covers are peeling off.")
            print("On your right is a room with tables piled with papers and steaming potions.")
            print("\n")
            user_choice = input("Would you like to search 'Potion Room' or 'Mystical Library' next: ")
        elif user_choice == "Dining Room":
            print("The Dining Room is where much mischief is afoot. Jealous courtiers and lovers were known for poisoning the food on the plates of rivals.")
            death = random.randint (1,50)
            if death > 40:
                print ("Your curiosity gets the better of you and you eat a poisoned apple. Better luck next time.")
            print("\n")
            user_choice = input("If you dare to eat the food, enter 'eat'. If not, type 'do not eat': ")
        elif user_choice == "Dwarf's Armory":
            print("The Dwarf's Armory was a place full of cheer before the dragon came, but beware that Dwarfs can be untrusting and love to place booby traps.")
            death = random.randint (1,50)
            if death > 30:
                print ("The pile of heavy armour falls onto you as you enter the room. Better luck next time.")
                break
            print("\n")
            user_choice = input("Would you like to search the 'Throne Room' or 'Dragon's Lair' next: ")
        elif user_choice == "exit":
            break
        else:
            print("That is not an option.")

        # This is if the player selects Magician's Hall
        if user_choice == "Potion Room":
            user_choice = input("You have entered the potion room. Do you choose to drink the posion named 'honesty' or 'soothslayer': ")
        elif user_choice == "Mystical Library":
            user_choice = input("You have entered the Mystical Library. Do you choose the book called 'Flight of Secrets' or 'Warlocks of Dunshire': ")
        # Coding for in potion room
        if user_choice == "honesty":
            print("You have a pure heart and an honest life ahead of you.")
            print("\n")
            user_choice = input("Continue to the Treasure Room, 'yes enter' or 'do not enter'?: ")
        elif user_choice == "soothslayer":
            print("Although the name may sound thrilling, soothslayer causes you to see the future and you die from all you have seen.")
            print("\n")
            break
        # coding for library
        if user_choice == "Flight of Secrets":
            print("You have a heart for stealing and that will not save you in this tale.")
            print("\n")
            print("You have died from being sucked into the book forever.")
            break
        elif user_choice == "Warlocks of Dunshire":
            print("You have chosen a path of revenge which is being rewarded this once. But revenge is always best served cold. Remember this lesson.")
            print("\n")
            user_choice = input("Continue to the Treasure Room, 'yes enter' or 'do not enter'?: ")
        # This is if the player select's the Dining Hall
        if user_choice == "do not eat":
            print("Well chosen", user_name)
            user_choice = input("Continue to the Treasure Room, 'yes enter' or 'do not enter'?: ")
        elif user_choice == "eat":
            print("You have died from posioned food.")
            break
        # This is if the player selects the Dwarf's Armory
        if user_choice == "Throne Room":
            print("In the Throne Room the king would sit and listen to his people's problems and help in anyway he could. The ceiling is lined with hanging swords.")
            print("Now might be your only chance to sit on the throne.")
            print("\n")
            user_choice = input("Will you sit? 'sit' or 'do not sit': ")
        elif user_choice == "Dragon's Lair":
            print("You have entered the musty depths of the Dragon's Lair. It is lined with riches beyond your wildest dreams.")
            print("You see a beautiful gem that you know would make you richer than the king.")
            print("\n")
            user_choice = input("Do you steal it? Type 'steal' or 'do not steal': ")
        # What happens in throne Room
        if user_choice == "sit":
            print("You sit on the throne and see a hidden passage that was invisble before. It leads to the treasure room.")
            print("\n")
            user_choice = input("Continue to the Treasure Room, 'yes enter' or 'do not enter'?: ")
        elif user_choice == "do not sit":
            print("You chose not to sit and instead have stepped on a trap which casues the hanging swords to fall upon you.")
            print("\n")
            user_choice = input("You are dead. Please type 'exit': ")
        # what happens in Dragon's Lair
        if user_choice == "steal":
            print("You have stolen from the dragon and will now face his wrath.")
            user_choice = input("You burn to death.")
            break
        elif user_choice == "do not steal":
            print("You are a wise person and have avoided the dragon's fire. You can see an openning in the rock and move towards it. There lies the Treasure Room.")
            print("\n")
            user_choice = input("Continue to the Treasure Room, 'yes enter' or 'do not enter'?: ")
        # treasure room code
        if user_choice == "yes enter":
            print("Welcome to the Treasure Room !!! You made it to the treasure and have completed the quest.")
            user_choice = input("You won the game ! please type 'exit': ")
        elif user_choice == "do not enter":
            print("You chose not to enter the treasure room.")
            user_choice = input("You have failed the quest. Please type 'exit': ")
    else:
        user_choice == "exit"
        break
