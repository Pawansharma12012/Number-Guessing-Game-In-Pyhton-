import random
no_of_attempts=0
number=random.randint(0,20)
print("Hi there, whats your name?")
name=input()
print("You have got a nice name! lets play "+name+" I have gussed a number now is your turn")
while no_of_attempts<6:
    print("Take a guess "+name)
    guess=input()
    guess=int(guess)
    no_of_attempts+=1
    if guess<number:
        print("Your is low,increse the number "+name)
    if guess>number:
        print("your guess is high, try to lower your guess")
    if guess==number:
        break;
if guess==number:
    no_of_attempts=str(no_of_attempts)
    print("Congo' "+name+" you defeted me by guessing the number in "+no_of_attempts+" guesses")
if guess!=number:
    print("Your were close "+name+" never give up, try again!")
    
