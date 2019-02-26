import random
l = ["r","s","p"]
while True:
	u = input("enter your choice,press n to discontinue")

	if u == "n":
		print("gameover")
		exit()

	c = random.choice(l)
	print("computer chooses",c)

	if u == c:
		print("tie")
	elif u == "r" and c == "s":
		print("user wins")
	elif u == "r" and c == "p":
		print("computer wins")
	elif u == "p" and c == "r":
		print("user wins")
	elif u == "s" and c == "r":
		print("computer wins")
	elif u == "s" and c == "p":
		print("user wins")
	elif u =="p" and c == "s":
		print("comp wins")
	else:
		print("discontinue")
		exit()