print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play!")
wants_to_play = input("Do you want to play? ").lower()
if wants_to_play == "yes":
        print("Lets play ")
if age < 18:
      print("You are not old enough to play...")
if age >= 18: 
    right_or_left = input("You wake up in a room with two doors on the right and the left. Which door do you go through? (right/left) ").lower()
if right_or_left == "right":
    print("You walk through the right door and die")
if right_or_left == "left":
    open_or_leave = input("You walk through the left door and see a treasure chest. Do you open the chest or leave the chest? (open/leave) ").lower()
if open_or_leave == ("open"):
    print("You open the chest and die")            
if open_or_leave == ("leave"):
     print("You have won the game! The real treasure is the friends we made along the way!")
              
            







    



