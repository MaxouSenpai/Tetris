import turtle as t
import random as r
import time
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

update = t.Pen();update.up();update.shape("square")

Bricks =[None,
	["cyan",((-1,1),(0,1),(1,1),(2,1))],
	["blue",((-1,1),(-1,0),(0,0),(1,0))],
	["orange",((-1,0),(0,0),(1,0),(1,1))],
	["yellow",((0,1),(0,0),(1,0),(1,1))],
	["green",((-1,0),(0,0),(0,1),(1,1))],
	["purple",((-1,0),(0,0),(0,1),(1,0))],
	["red",((-1,1),(0,1),(0,0),(1,0))]]

#Bricks =[None,
#	["cyan",[[-1,1],[0,1],[1,1],[2,1]]],
#	["blue",[[-1,1],[-1,0],[0,0],[1,0]]],
#	["orange",[[-1,0],[0,0],[1,0],[1,1]]],
#	["yellow",[[0,1],[0,0],[1,0],[1,1]]],
#	["green",[[-1,0],[0,0],[0,1],[1,1]]],
#	["purple",[[-1,0],[0,0],[0,1],[1,0]]],
#	["red",[[-1,1],[0,1],[0,0],[1,0]]]]

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
	while yes and i < 4:
		if coord[0]+ins[i][0] >= 0 and coord[0]+ins[i][0] < Colonnes:
			yes = Board[coord[1]+ins[i][1]][coord[0]+ins[i][0]] == "black"
			if coord[1]+ins[i][1] < 0:
				yes = False
			i += 1
		else:
			yes = False
	return yes

def tetrisBrick():
	return Bricks[r.randint(1,7)]

def movingPart(Board):

	def right():
		coord = (xy[0] + 1,xy[1])
		if check(Board,ins,coord):
			xy[0] += 1
	
	def left():
		coord = (xy[0] - 1,xy[1])
		if check(Board,ins,coord):
			xy[0] -= 1

	def down():
		It[:] = [1]

	def up():
		pass # TODO

	color,ins = tetrisBrick()
	xy = Spawn[:]
	It = [100]
	if check(Board,ins,xy):
		falling = True
		t.onkey(right,"Right")
		t.onkey(left,"Left")
		t.onkey(down,"Down")
		t.onkey(up,"Up")
		t.listen()
		i = 0
		while falling:
			BoardTemp = deepcopy(Board)
			for coo in ins:
				BoardTemp[xy[1]+coo[1]][xy[0]+coo[0]] = color
			boardUpdate(BoardTemp)

			if i >= It[0]:
				xy[1] -= 1
				i = 0
				It = [100]

			falling = check(Board,ins,xy)
			i += 1
		Board[:] = BoardTemp
		gameover = False
		time.sleep(0.75)
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
			checkLine(Board)
		print("You have lost")
		play = int(input("Wanna play again ? (1:Yes,2:No) : "))
		if play == 1:play = True
		else:play = False

if __name__ == "__main__":
	runGame()