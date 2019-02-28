import time
from random import randint
print("Welcome to my game please input the players names")
player1=input("Please enter player 1's name followed by the return key : ")
player2=input("Please enter player 2's name followed by the return key : ")
print("right then ", player1," and ",player2, " the game is simple i'll explain the rules as we go along")
player1position=1
player2position=1
while player1position<48 or player2position<48:
    print("Its" , player1 , "' go ")
    dice1=randint(0,6)
    dice2=randint(0,6)
    if dice1==dice2:
        print("both dices rolled a ", dice1, " so you move back ", dice1+dice2 ," spaces")
        player1position=player1position-dice1+dice2
    else:
        print("Your first dice was a ", dice1, " and your second was a ", dice2)
        print("your total is ", dice1+dice2)
        player1position=player1position+dice1+dice2
        print("player one is now on square ", player1position)
        time.sleep(0.1)
    print("Its" , player2 , "' go ")
    dice1=randint(0,6)
    dice2=randint(0,6)
    if dice1==dice2:
        print("both dices rolled a ", dice1, " so you move back " ,dice1+dice2 ," spaces")
        player2position=player2position-dice1+dice2
    print("Your first dice was a ", dice1, " and your second was a ", dice2)
    print("your total is ", dice1+dice2)
    player2position=player2position+dice1+dice2
    print("player two is now on square ", player2position)
    time.sleep(0.1)
else:
    if player1position >49:
        print(player1 , "has won well done")
    else:
        print(player2 , "has won well done")