
# task 1
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass # invalid input
elif place == "cave":
    action_cave = input("light a torch or proceed in the dark?")
    if action_cave == "light a torch":
        print("You found a treasure chest!")
    elif action_cave == "proceed in the dark":
        print("You fell off a ledge that you didn't see and got badly hurt! Ouch!")
    else:
        pass # invalid input
else:
    pass # invalid input

#2


attendees = int(input("Enter number of attendees: "))
venue = "large hall" 
if attendees > 100:
    choice = input("would you like to use an 'audio system' or 'projector'?")
    print(choice + " inside " + venue) 
    catering_choice = input("Are you vegetarian? 'yes' or 'no'?")
    if catering_choice == "yes":
        print("We recommend that you eat Veggie Delight Caterers")
    elif catering_choice == "no":
        print("We recommend to try our delicious Gourmet Meals Caterers")
else:
    choice = input("would you like to use an 'audio system' or 'projector'?")
    print(choice + " inside " + "conference room") 
    catering_choice = input("Are you vegetarian? 'yes' or 'no'?")
    if catering_choice == "yes":
        print("We recommend that you eat Veggie Delight Caterers")
    elif catering_choice == "no":
        print("We recommend to try our delicious Gourmet Meals Caterers")
    




































