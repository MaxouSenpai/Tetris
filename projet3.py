import turtle as t
import random as r
import time
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

Bricks =[None,["cyan",(None)],["blue",(None)],["orange",(None)],["yellow",((0,1),(0,0),(1,0),(1,1))],["green",(None)],["purple",(None)],["red",(None)]] 

Spawn = [Colonnes//2 - 1,Lignes - 2]
# SpawnC = (Epais/2 + Colonnes/2*Epais,Epais/2 + (Lignes-1)*Epais)

def board():
	t.ht()
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

def boardUpdate(Board):
	update.clearstamps();update.shapesize(1.4,1.4)
	for i in range(Lignes):
		update.goto(Epais/2,Epais/2 + i * Epais)
		for j in range(Colonnes):
			if Board[i][j] != "black":
				update.color(Board[i][j])
				update.stamp()
				update.up()
			update.fd(Epais)
	t.update()


def check(Board,brick):
	return True

def tetrisBrick():
	#return Bricks[r.randint(1,7)]
	return Bricks[4]

def movingPart(Board):
	color,ins = tetrisBrick()
	print(color)
	print(ins)
	if check(Board,None):
		falling = True
		i = 0
		xy = Spawn
		while falling:
			BoardTemp = deepcopy(Board)
			for coo in ins:
				BoardTemp[xy[1]+coo[1]][xy[0]+coo[0]] = color
			boardUpdate(BoardTemp)
			#falling = check(Board,None)
			time.sleep(1)
			falling = i != 18
			i+=1
			xy[1] -= 1
		Board[:] = BoardTemp
	else:
		print("Game Over")

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

Board = [["black" for _ in range(Colonnes)] for _ in range(Lignes)]

board()

update = t.Pen();update.ht();update.up();update.shape("square")


movingPart(Board)

#Board[3][2] = "yellow"
#Board[10][4] = "blue"
for i in range(Colonnes):
	Board[15][i] = "red"


for i in range(Colonnes):
	Board[5][i] = "blue"

boardUpdate(Board)

input()

checkLine(Board)



input()