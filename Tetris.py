import turtle as t
import random as r
import time
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

update = t.Pen();update.up()
result = t.Pen();result.ht();result.up()

Score = 0
Board = []
color = None
ins = None
ins = None
xy = []
Counter = 0
Count = 0

Color = {
	1 : "cyan" ,
	2 : "blue" ,
	3 : "orange" ,
	4 : "yellow" ,
	5 : "green" ,
	6 : "purple" ,
	7 : "red",
	8 : "black"
		}

Bricks = {
	1 : ((-1,0),(0,0),(1,0),(2,0)),
	2 : ((-1,1),(-1,0),(0,0),(1,0)),
	3 : ((-1,0),(0,0),(1,0),(1,1)),
	4 : ((0,1),(0,0),(1,0),(1,1)),
	5 : ((-1,0),(0,0),(0,1),(1,1)),
	6 : ((-1,0),(0,0),(0,1),(1,0)),
	7 : ((-1,1),(0,1),(0,0),(1,0))
		}

Spawn = [Colonnes//2 - 1,Lignes - 2]

def board():
	"""TODO"""
	print("Board")
	t.setup(Colonnes*Epais,Lignes*Epais)
	t.setworldcoordinates(0,0,Colonnes*Epais+5,Lignes*Epais)
	t.bgcolor("black")
	t.title("Tetris by MaxouSenpai")
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

def resetBoard():
	"""TODO"""
	print("Board Reset")
	global Board
	Board = [[8 for _ in range(Colonnes)] for _ in range(Lignes)]
	updateScreen(Board)

def updateScreen(board):
	"""TODO"""
	print("Board update")
	update.ht();update.clearstamps();update.shape("square");update.shapesize(1.4,1.4);update.up()
	for i in range(Lignes):
		update.goto(Epais/2,Epais/2 + i * Epais)
		for j in range(Colonnes):
			if board[i][j] != Colonnes:
				update.color(Color[board[i][j]])
				update.stamp()
				update.up()
			update.fd(Epais)
	t.update()

def check(board,pos,ins):
	"""TODO"""
	print("Check")
	can = True
	i = 0
	print(pos)
	while can and i < 4:
		if 0 <= pos[0]+ins[i][0] < Colonnes and pos[1] + ins[i][1]<Lignes:
			can = board[pos[1]+ins[i][1]][pos[0]+ins[i][0]] == 8
			if pos[1]+ins[i][1] < 0:
				can = False
			i += 1
		else:
			can = False
	print(can)
	return can

def tetrisBrick():
	"""TODO"""
	global ins,color
	print("Tetris Brick")
	color = r.randint(1,7)
	ins = Bricks[color]

def checkLine():
	"""TODO"""
	print("Check Line")
	global Score,Board
	i = 0
	while i < Lignes:
		yes = True
		j = 0
		while yes and j < Colonnes:
			if Board[i][j] == 8:
				yes = False
			else:
				j += 1
		if yes:
			Score += 1
			del Board[i]
			Board.append([8 for _ in range(Lignes)])
			updateScreen(Board)
		else:
			i += 1

def displayResult():
	"""TODO"""
	print("Display Result")
	global Score
	result.ht();result.up();result.goto(0,Lignes*Epais/3);result.color("grey");result.down()
	result.begin_fill()
	for _ in range(2):
		result.fd(Colonnes*Epais);result.left(90);result.fd(Lignes*Epais/3);result.left(90)
	result.color("grey20")
	result.end_fill()
	result.color("white")
	result.ht();result.right(90);result.goto(Colonnes*Epais/2,Lignes*Epais*7/12-20);
	result.write(str(Score)+" rows !",False,align = "center",font = ("Arial",30,"normal"))
	result.fd(2 * Epais);result.write("New Game  :  <spacebar>",False,align = "center",font = ("Arial",15,"normal"))
	result.fd(Epais);result.write("Quit  :  <escape>",False,align = "center",font = ("Arial",15,"normal"))

def updateBoard():
	global Board,xy,ins,color
	BoardTemp = deepcopy(Board)
	for coo in ins:
		BoardTemp[xy[1]+coo[1]][xy[0]+coo[0]] = color
	return BoardTemp

def start():
	print("Start")
	resetBoard()
	play()

def play():
	checkLine()
	print("Play")
	global Board,color,ins,xy
	tetrisBrick()
	ins = list(ins)
	xy = Spawn[:]
	if color == 1:
		xy[1] += 1
	if check(Board,xy,ins):
		movingPart()
	else:
		displayResult()
		t.onkey(None,"Right")
		t.onkey(None,"Left")
		t.onkey(None,"Down")
		t.onkey(None,"Up")
		t.onkey(t.bye,"Escape")
		t.onkey(runGame,"space")
		print("Finish")

def movingPart():
	print("Moving Part")
	global Board,ins,ins,xy,Counter
	BoardTemp = updateBoard()
	updateScreen(BoardTemp)
	
	if Counter == 0:
		xy[1] -= 1
		Counter = 1
	elif Counter == 60:
		Counter = 0
	else:
		Counter += 1
	if check(Board,xy,ins):
		t.ontimer(movingPart,10)
	else:
		Board = BoardTemp
		play()


def runGame():
	print("Run Game")
	global Score,Count
	Count += 1
	print(Count)
	result.reset()
	Score = 0
	t.onkey(None,"Escape")
	t.onkey(None,"space")
	t.onkey(right,"Right")
	t.onkey(left,"Left")
	t.onkey(down,"Down")
	t.onkey(up,"Up")
	t.listen()
	start()
	t.mainloop()

def right():
	global Board,BoardTemp,xy,ins
	print("Right")
	coord = (xy[0] + 1,xy[1])
	if check(Board,coord,ins):
		BoardTemp = updateBoard()
		xy[0] += 1
		updateScreen(BoardTemp)

def left():
	print("Left")
	global Board,BoardTemp,xy,ins
	coord = (xy[0] - 1,xy[1])
	if check(Board,coord,ins):
		BoardTemp = updateBoard()
		xy[0] -= 1
		updateScreen(BoardTemp)

def down():
	print("Down")
	global Board,BoardTemp,xy,ins
	coord = (xy[0],xy[1]-1)
	if check(Board,coord,ins):
		BoardTemp = updateBoard()
		xy[1] -= 1
		updateScreen(BoardTemp)

def up():
	print("Up")
	global Board,BoardTemp,xy,ins
	a,b,c,d = t.Vec2D(ins[0][0],ins[0][1]), t.Vec2D(ins[1][0],ins[1][1]), t.Vec2D(ins[2][0],ins[2][1]), t.Vec2D(ins[3][0],ins[3][1])
	temp = [(round(a.rotate(90)[0]),round(a.rotate(90)[1])),(round(b.rotate(90)[0]),round(b.rotate(90)[1])),(round(c.rotate(90)[0]),round(c.rotate(90)[1])),(round(d.rotate(90)[0]),round(d.rotate(90)[1]))]
	if check(Board,xy,temp):
		ins = temp


if __name__ == "__main__":
	print("---Debug---")
	board()
	runGame()