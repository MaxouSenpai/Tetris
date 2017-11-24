__author__ = "Maxime Hauwaert"
__date__ = "Novembre 2017"

import turtle as t
import random as r
from copy import deepcopy

Colonnes = 8
Lignes = 20
Epais = 35

Spawn = [Colonnes // 2 - 1, Lignes - 2]

Colors = {
	1 : "cyan" ,
	2 : "blue" ,
	3 : "orange" ,
	4 : "yellow" ,
	5 : "green" ,
	6 : "purple" ,
	7 : "red"
		}

#Instructions qui permettent de construire les pièces
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
	t.setworldcoordinates(0, 0, Colonnes * Epais + 5, Lignes * Epais + 100)
	t.bgcolor("black")
	t.title("Tetris")
	t.tracer(False)

	column = t.Pen();column.color("grey");column.ht()
	column.penup();column.goto(0,0);column.pendown()
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
	""" Fonction qui réinitialise le board en global """
	global Board
	
	Board = [[0 for _ in range(Colonnes)] for _ in range(Lignes)]
	updateScreen(Board)

def updateScreen(board):
	""" Fonction qui met à jour l'écran avec le board en reçu en entrée """
	updatep.ht();updatep.shape("square");updatep.shapesize(1.35,1.35)
	updatep.clearstamps();updatep.up()

	for i in range(Lignes):
		updatep.goto(Epais / 2, Epais / 2 + i * Epais )
		for j in range(Colonnes):
			if board[i][j] != 0: # Les blocs vides ne sont pas affichés
				updatep.color(Colors[board[i][j]]) # Les couleurs sont stockées sous forme de chiffre (voir le dictionnaire Colors)
				updatep.stamp()
				updatep.up()
			updatep.fd(Epais)
	t.update()

def check(board,xy,ins):
	""" Fonction qui vérifie si les blocs peuvent se placer sans superposer d'autres blocs """
	can = True
	i = 0
	while can and i < len(ins):
		new_x = xy[0] + ins[i][0]
		new_y = xy[1] + ins[i][1]

		if 0 <= new_x < Colonnes and 0 <= new_y < Lignes: # On vérifie que les nouvelles coordonnées des blocs ne dépassent pas les limites
			can = board[new_y][new_x] == 0 # 0 correspond à un bloc vide
			i += 1
		else:
			can = False

	return can

def checkLine():
	""" Fonction qui vérifie si une ou plusieurs lignes sont complètes, les supprime  et met à jour le score """
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
			
	scorep.ht();scorep.color("white");scorep.clear()
	scorep.up();scorep.goto(Colonnes * Epais / 2, Lignes * Epais + 25)
	
	scorep.write("Score : " + str(Score),False,align = "center",font = ("Ubuntu",30,"bold"))

def displayResult():
	""" Fonction qui affiche le score à la fin de la partie """
	global Score

	resultp.ht();resultp.up();resultp.goto(0,Lignes*Epais/3);resultp.color("grey");resultp.down()
	resultp.begin_fill()
	for _ in range(2):
		resultp.fd(Colonnes*Epais);resultp.left(90);resultp.fd(Lignes*Epais/3);resultp.left(90)
	resultp.color("grey20")
	resultp.end_fill()
	resultp.color("white")
	resultp.ht();resultp.right(90);resultp.goto(Colonnes*Epais/2,Lignes*Epais*7/12-20);
	resultp.write(str(Score)+" rows !",False,align = "center",font = ("Ubuntu",30,"bold"))
	resultp.fd(2 * Epais);resultp.write("New Game  :  <spacebar>",False,align = "center",font = ("Ubuntu",15,"normal"))
	resultp.fd(Epais);resultp.write("Quit  :  <escape>",False,align = "center",font = ("Ubuntu",15,"normal"))

	scorep.clear()
	scorep.write("Game Over",False,align = "center",font = ("Ubuntu",30,"bold"))

def updateBoard():
	""" Fonction qui renvoie le board mis à jour """
	global Board,Pos,Ins,Color

	BoardTemp = deepcopy(Board)
	for vec in Ins:
		BoardTemp[Pos[1] + vec[1]][Pos[0] + vec[0]] = Color
	
	return BoardTemp

def tetrisBrick():
	""" Fonction qui sélectionne une pièce """
	global Board,Color,Ins,Pos

	checkLine()
	Color = r.randint(1,7)
	Ins = Bricks[Color]
	Pos = Spawn[:]

	if Color == 1: # La pièce 1 n'est que sur un seul étage donc la position de départ doit être un bloc plus haut
		Pos[1] += 1
	
	if check(Board,Pos,Ins):
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		t.onkey(right,"Right")
		t.onkey(left,"Left")
		t.onkey(down,"Down")
		t.onkey(rotate,"Up")
		t.ontimer(movingPart,1000)
	
	else: # Si la pièce ne peut pas se placer juste après qu'elle ait été choisie c'est gameover
		displayResult()
		t.onkey(t.bye,"Escape")
		t.onkey(runGame,"space")

def movingPart():
	""" Fonction qui s'occupe de faire descendre la pièce """
	global Board,Ins,Pos

	Pos[1] -= 1
	if check(Board,Pos,Ins):
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		t.ontimer(movingPart,1000)

	else: # Désactivation des touches pour éviter tout problème
		t.onkey(None,"Right")
		t.onkey(None,"Left")
		t.onkey(None,"Down")
		t.onkey(None,"Up")
		Pos[1] += 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)
		Board = BoardTemp
		tetrisBrick()

def runGame():
	""" Fonction qui lance une nouvelle partie """
	global Score

	resultp.reset()
	Score = 0
	t.onkey(None,"Escape")
	t.onkey(None,"space")
	t.listen()
	resetBoard()
	tetrisBrick()

def right():
	""" Fonction qui déplace la pièce à droite de 1 bloc """
	global Board,Pos,Ins

	coord = (Pos[0] + 1,Pos[1])
	if check(Board,coord,Ins):
		Pos[0] += 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def left():
	""" Fonction qui déplace la pièce à gauche de 1 bloc """
	global Board,Pos,Ins

	coord = (Pos[0] - 1,Pos[1])
	if check(Board,coord,Ins):
		Pos[0] -= 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def down():
	""" Fonction qui fait descendre la pièce de 1 bloc """
	global Board,Pos,Ins

	coord = (Pos[0],Pos[1]-1)
	if check(Board,coord,Ins):
		Pos[1] -= 1
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def rotate():
	""" Fonction qui fait tourner la pièce de 90° """
	global Board,Pos,Ins

	temp = [None for i in range(len(Ins))]
	for i in range(len(Ins)):
		temp[i] = (-Ins[i][1],Ins[i][0]) # (x,y) rotation de 90° ---> (-y,x) 
	
	if check(Board,Pos,temp):
		Ins = temp
		BoardTemp = updateBoard()
		updateScreen(BoardTemp)

def Tetris():
	""" Fonction qui lance le jeu """
	global updatep,resultp,scorep
	updatep = t.Pen()
	resultp = t.Pen()
	scorep = t.Pen()
	board()
	runGame()
	t.mainloop()

if __name__ == "__main__":
	Tetris()