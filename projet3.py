import turtle as t
import random as r
import time
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

update = t.Pen();update.up();update.shape("square")
result = t.Pen();result.ht();result.up()

Bricks =[None,
	["cyan",((-1,1),(0,1),(1,1),(2,1))],
	["blue",((-1,1),(-1,0),(0,0),(1,0))],
	["orange",((-1,0),(0,0),(1,0),(1,1))],
	["yellow",((0,1),(0,0),(1,0),(1,1))],
	["green",((-1,0),(0,0),(0,1),(1,1))],
	["purple",((-1,0),(0,0),(0,1),(1,0))],
	["red",((-1,1),(0,1),(0,0),(1,0))]]
	
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
		up2(ins)

	def up2(ins):
		a,b,c,d = t.Vec2D(ins[0][0],ins[0][1]), t.Vec2D(ins[1][0],ins[1][1]), t.Vec2D(ins[2][0],ins[2][1]), t.Vec2D(ins[3][0],ins[3][1])
		temp = [(round(a.rotate(90)[0]),round(a.rotate(90)[1])),(round(b.rotate(90)[0]),round(b.rotate(90)[1])),(round(c.rotate(90)[0]),round(c.rotate(90)[1])),(round(d.rotate(90)[0]),round(d.rotate(90)[1]))]
		if check(Board,temp,xy):
			ins[:] = temp

	color,ins = tetrisBrick()
	xy = Spawn[:]
	It = [50]
	ins = [x for x in ins]
	if check(Board,ins,xy):
		falling = True
		t.onkey(right,"Right")
		t.onkey(left,"Left")
		t.onkey(down,"Down")
		t.onkey(up,"Up")
		t.listen()
		i = 0
		time.sleep(0.5)
		while falling:
			BoardTemp = deepcopy(Board)
			for coo in ins:
				BoardTemp[xy[1]+coo[1]][xy[0]+coo[0]] = color
			boardUpdate(BoardTemp)

			if i >= It[0]:
				xy[1] -= 1
				i = 0
				It = [50]
			else:
				time.sleep(0.01)

			falling = check(Board,ins,xy)
			i += 1
		Board[:] = BoardTemp
		gameover = False
		t.onkey(None,"Right")
		t.onkey(None,"Left")
		t.onkey(None,"Down")
		t.onkey(None,"Up")
	else:
		gameover = True

	return gameover

def checkLine(Board):
	i = 0
	score = 0
	while i < Lignes:
		yes = True
		j = 0
		while yes and j < Colonnes:
			if Board[i][j] == "black":
				yes = False
			else:
				j += 1
		if yes:
			score += 1
			del Board[i]
			Board.append(["black" for _ in range(Lignes)])
			boardUpdate(Board)
		else:
			i += 1
	return score

def displayResult(score):
	print("Your score :",score)
	result.ht();result.up();result.goto(0,Lignes*Epais/4);result.color("black","grey");result.down()
	result.begin_fill()
	for _ in range(2):
		result.fd(Colonnes*Epais);result.left(90);result.fd(Lignes*Epais/2);result.left(90)
	result.end_fill()

	input()
	result.reset()

def runGame():
	board()
	play = True
	while play:
		Board = boardReset()
		gameover = False
		score = 0
		while not gameover:
			gameover = movingPart(Board)
			score += checkLine(Board)
		print("Gameover!")
		displayResult(score)
		play = int(input("Wanna play again ? (1:Yes,2:No) : "))
		if play == 1:play = True
		else:play = False

if __name__ == "__main__":
	runGame()