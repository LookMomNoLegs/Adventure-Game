print("Welcome to my computer quiz!")
playing_game = input("Do you want to play my game? ").lower()
if playing_game == ("no"):
    print("Okay...") 
    quit()
if playing_game == ("yes"):
    print("Let's play!")
score = 0

answer = input("What does cpu stand for? ").lower()
if answer == ("central processing unit"):
    print("Good job! You answered correctly!")
    score += 1
else: 
    print("Oops! That is not correct...")
    

answer = input("What does gpu stand for? ").lower()
if answer == ("graphics processing unit"):
    print("Good job! You answered correctly!")
    score += 1
else: 
    print("Oops! That is not correct...")
    

answer = input("Which church is the one true church that Christ built? ").lower()
if answer == ("the orthodox church"):
    print("Christos Anesti! Great job!")
    score += 1
else:
    print("Unaxios!")

print("You got " + str(score) + " questions correct")
quit()


