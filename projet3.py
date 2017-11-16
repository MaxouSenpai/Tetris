import turtle as t
import random as r
import time
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

update = t.Pen();update.up();update.shape("square")

Bricks =[None,["cyan",(None)],["blue",(None)],["orange",(None)],["yellow",((0,1),(0,0),(1,0),(1,1))],["green",(None)],["purple",(None)],["red",(None)]] 

Spawn = [Colonnes//2 - 1,Lignes - 2]

def board():
	t.setup(Colonnes*Epais,Lignes*Epais)
	t.setworldcoordinates(0,0,Colonnes*Epais,Lignes*Epais)
	t.bgcolor("black")
	t.tracer(False)

	column = t.Pen();column.color("white")
	column.ht();column.penup();column.goto(0,0);column.pendown()
	column.left(90)
	for i in range(1,Colonnes+2):
		column.fd(Lignes*Epais)
		column.penup();column.goto(i*Epais,0);column.pendown()

	row = t.Pen();row.color("white")
	row.ht();row.penup();row.goto(0,0);row.pendown()
	for i in range(1,Lignes+2):
		row.fd(Colonnes*Epais)
		row.penup();row.goto(0,i*Epais);row.pendown()
	
	t.update()

def boardReset():
	Board = [["black" for _ in range(Colonnes)] for _ in range(Lignes)]
	boardUpdate(Board)
	return Board


def boardUpdate(Board):
	update.ht();update.clearstamps();update.shapesize(1.4,1.4);update.up()
	for i in range(Lignes):
		update.goto(Epais/2,Epais/2 + i * Epais)
		for j in range(Colonnes):
			if Board[i][j] != "black":
				update.color(Board[i][j])
				update.stamp()
				update.up()
			update.fd(Epais)
	t.update()


def check(Board,ins,coord):
	yes = True
	i = 0
	while yes and i < 4: # Another exeptions needed
		yes = Board[coord[1]+ins[i][1]][coord[0]+ins[i][0]] == "black"
		if coord[1]+ins[i][1] < 0:
			yes = False
		i += 1
	return yes

def tetrisBrick():
	#return Bricks[r.randint(1,7)]
	return Bricks[4]

def movingPart(Board):
	color,ins = tetrisBrick()
	xy = Spawn[:]
	if check(Board,ins,xy):
		falling = True
		while falling:
			BoardTemp = deepcopy(Board)
			for coo in ins:
				BoardTemp[xy[1]+coo[1]][xy[0]+coo[0]] = color
			boardUpdate(BoardTemp)
			time.sleep(0.2)
			xy[1] -= 1
			falling = check(Board,ins,xy)
		Board[:] = BoardTemp
		gameover = False
	else:
		gameover = True

	return gameover

def checkLine(Board):
	i = 0
	while i < Lignes:
		yes = True
		j = 0
		while yes and j < Colonnes:
			if Board[i][j] == "black":
				yes = False
			else:
				j += 1
		if yes:
			del Board[i]
			Board.append(["black" for _ in range(Lignes)])
			boardUpdate(Board)
		else:
			i += 1

def runGame():
	board()
	play = True
	while play:
		Board = boardReset()
		gameover = False
		while not gameover:
			gameover = movingPart(Board)
		print("You have lost")
		play = int(input("Wanna play again ? (1:Yes,2:No) : "))
		if play == 1:play = True
		else:play = False


#Board = [["black" for _ in range(Colonnes)] for _ in range(Lignes)]
#board()

runGame()

#movingPart(Board)

#Board[3][2] = "yellow"
#Board[10][4] = "blue"
#for i in range(Colonnes):
#	Board[15][i] = "red"


#for i in range(Colonnes):
#	Board[5][i] = "blue"

#boardUpdate(Board)
#input()
#checkLine(Board)
#input()