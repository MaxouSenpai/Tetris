__author__ = "Maxime Hauwaert"
__date__ = "Novembre 2017"

import turtle as t
import random as r
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

Spawn = [Colonnes // 2 - 1, Lignes - 2]

Color = {
	1 : "cyan" ,
	2 : "blue" ,
	3 : "orange" ,
	4 : "yellow" ,
	5 : "green" ,
	6 : "purple" ,
	7 : "red"
		}

#Instructions qui permetent de construire les pièces
Bricks = {
	1 : [[-1,0],[0,0],[1,0],[2,0]],
	2 : [[-1,1],[-1,0],[0,0],[1,0]],
	3 : [[-1,0],[0,0],[1,0],[1,1]],
	4 : [[0,1],[0,0],[1,0],[1,1]],
	5 : [[-1,0],[0,0],[0,1],[1,1]],
	6 : [[-1,0],[0,0],[0,1],[1,0]],
	7 : [[-1,1],[0,1],[0,0],[1,0]]
		}

def board():
	""" Fonction qui initialise la fenêtre de jeu """
	t.setup(Colonnes * Epais, Lignes * Epais)
	t.setworldcoordinates(0, 0, Colonnes * Epais + 5, Lignes * Epais)
	t.bgcolor("black")
	t.title("Tetris")
	t.tracer(False)

	column = t.Pen();column.color("grey")
	column.ht();column.penup();column.goto(0,0);column.pendown()
	column.left(90)
	for i in range(1, Colonnes + 2):
		column.fd(Lignes*Epais)
		column.penup();column.goto(i * Epais,0);column.pendown()

	row = t.Pen();row.color("grey")
	row.ht();row.penup();row.goto(0,0);row.pendown()
	for i in range(1,Lignes + 2):
		row.fd(Colonnes * Epais)
		row.penup();row.goto(0,i * Epais);row.pendown()
	
	t.update()

def resetBoard():
	""" Fonction qui réinitialise le board """
	global Board
	
	Board = [[0 for _ in range(Colonnes)] for _ in range(Lignes)]
	updateScreen(Board)

def updateScreen(board):
	""" Fonction qui met à jour l'écran avec le board en reçu en entrée """
	update.ht();update.clearstamps();update.shape("square");update.shapesize(1.4,1.4);update.up()
	
	for i in range(Lignes):
		update.goto(Epais / 2, Epais / 2 + i * Epais)
		for j in range(Colonnes):
			if board[i][j] != 0: # Les blocs libres ne sont pas affichés
				update.color(Color[board[i][j]]) # Les couleurs sont stockées sous forme de chiffre
				update.stamp()
				update.up()
			update.fd(Epais)
	t.update()

def check(board,xy,ins):
	""" Fonction qui vérifie si les blocs peuvent se placer """
	can = True
	i = 0
	while can and i < 4:
		new_x = xy[0] + ins[i][0]
		new_y = xy[1] + ins[i][1]

		if 0 <= new_x < Colonnes and 0 <= new_y < Lignes: # On vérifie que les coordonnées ne dépassent pas les limites
			can = board[new_y][new_x] == 0 # 0 correspond à un bloc libre
			i += 1
		else:
			can = False

	return can

def checkLine():
	""" Fonction qui vérifie si une ou plusieurs lignes sont complètes et les supprime """
	global Score,Board

	i = 0
	
	while i < Lignes:
		yes = True
		j = 0
		while yes and j < Colonnes:
			if Board[i][j] == 0:
				yes = False
			else:
				j += 1
		if yes:
			Score += 1
			del Board[i]
			Board.append([0 for _ in range(Lignes)])
			updateScreen(Board)
		else:
			i += 1

def displayResult():
	""" Fonction qui affiche le score à la fin de la partie """
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
	""" Fonction qui renvoie le board mis à jour """
	global Board,pos,ins,color

	BoardTemp = deepcopy(Board)
	for vec in ins:
		BoardTemp[pos[1] + vec[1]][pos[0] + vec[0]] = color
	
	return BoardTemp

def tetrisBrick():
	""" Fonction qui sélectionne une pièce """
	global Board,color,ins,pos

	checkLine()
	color = r.randint(1,7)
	ins = Bricks[color]
	pos = Spawn[:]

	if color == 1:
		pos[1] += 1
	
	if check(Board,pos,ins):
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		t.onkey(right,"Right")
		t.onkey(left,"Left")
		t.onkey(down,"Down")
		t.onkey(rotate,"Up")
		t.ontimer(movingPart,1000)
	
	else:
		displayResult()
		t.onkey(t.bye,"Escape")
		t.onkey(runGame,"space")

def movingPart():
	""" Fonction qui s'occupe de faire descendre la pièce """
	global Board,ins,pos

	pos[1] -= 1
	if check(Board,pos,ins):
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		t.ontimer(movingPart,1000)

	else:
		t.onkey(None,"Right")
		t.onkey(None,"Left")
		t.onkey(None,"Down")
		t.onkey(None,"Up")
		pos[1] += 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		Board = BoardTemp
		tetrisBrick()

def runGame():
	""" Fonction qui lance une nouvelle partie """
	global Score

	result.reset()
	Score = 0
	t.onkey(None,"Escape")
	t.onkey(None,"space")
	t.listen()
	resetBoard()
	tetrisBrick()

def right():
	""" Fonction qui déplace la pièce à droite de 1 bloc """
	global Board,pos,ins

	coord = (pos[0] + 1,pos[1])
	if check(Board,coord,ins):
		pos[0] += 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def left():
	""" Fonction qui déplace la pièce à gauche de 1 bloc """
	global Board,pos,ins

	coord = (pos[0] - 1,pos[1])
	if check(Board,coord,ins):
		pos[0] -= 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def down():
	""" Fonction qui fait descendre la pièce de 1 bloc """
	global Board,pos,ins

	coord = (pos[0],pos[1]-1)
	if check(Board,coord,ins):
		pos[1] -= 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def rotate():
	""" Fonction qui fait tourner la pièce de 90° """
	global Board,pos,ins

	temp = [None for i in range(len(ins))]
	for i in range(4):
		temp[i] = (-ins[i][1],ins[i][0]) # (x,y) rotation de 90° ---> (-y,x) 
	
	if check(Board,pos,temp):
		ins = temp
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def Tetris():
	""" Fonction qui lance le jeu """
	global update,result
	update = t.Pen()
	result = t.Pen()
	board()
	runGame()
	t.mainloop()

if __name__ == "__main__":
	Tetris()