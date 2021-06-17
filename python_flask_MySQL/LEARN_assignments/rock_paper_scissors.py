# 
# 
# ROCK - PAPER - SCISSORS:
# 
# 
from random import randint

play_options = ["Rock", "Paper", "Scissors"]
machine = play_options [randint(0,2)]
machine_counter = 0
man_counter = 0

while man_counter < 3 and machine_counter < 3:
    man = input("Rock, Paper, Scissors? ")
    if man == machine:
        print("Tie! Throw again!")
    elif man == "Rock":
        if machine == "Paper":
            print("You are one pathetic loser!", machine, "beats", man)
            machine_counter += 1
        elif machine == "Scissors":
            print("Winner winner, chicken dinner!", man, "beats", machine)
            man_counter += 1
    elif man == "Paper":
        if machine == "Scissors":
            print("You are one pathetic loser!", machine, "beats", man)
            machine_counter += 1
        elif machine == "Rock":
            print("Winner winner, chicken dinner!", man, "beats", machine)
            man_counter +=1
    elif man == "Scissors":
        if machine == "Rock":
            print("You are one pathetic loser!", machine, "beats", man)
            machine_counter +=1
        elif machine == "Paper":
            print( "Winner winner, chicken dinner!", man, "beats", machine)
            man_counter +=1
    elif man == "Paper":
        if machine == "Rock":
            print("Winner winner, chicken dinner!", man, "beats", machine)
            man_counter += 1
        elif machine =="Scissors":
            print("You are one pathetic loser!", machine, "beats", man)
    elif man == "Scissors":
        if machine == "Paper": 
            print("Winner winner, chicken dinner!", man, "beats", machine)
            man_counter += 1
        elif machine == "Rock":
            print("You are one pathetic loser!", machine, "beats", man)
            machine_counter += 1
    elif man == "Rock":
        if machine == "Scissors":
            print("Winner winner, chicken dinner!", man, "beats", machine)
            man_counter += 1
        elif machine == "Paper":
            print("You are one pathetic loser!", machine, "beats", man)
        
    else:
        print("Mmm...I dont think that's correct...")

    print(f"score: player {man_counter}, computer {machine_counter}")
    
if man_counter == 3:
    print("Player wins the match!")
elif machine_counter == 3:
    print("Player wins the match!")
