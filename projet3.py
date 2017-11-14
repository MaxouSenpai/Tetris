import turtle as t
import random as r
import time

Colonnes = 8
Lignes = 20

Briques = []

def Board():
	t.bgcolor("grey")
	t.tracer(False)
	origin_x = (-Colonnes//2*30)
	origin_y = (-Colonnes//2*30-150)
	column = t.Pen()
	column.ht();column.penup();column.goto(origin_x,origin_y);column.pendown()
	column.left(90)
	for i in range(1,Colonnes+2):
		column.fd(Lignes*30)
		column.penup();column.goto(origin_x + i*30,origin_y);column.pendown()

	row = t.Pen()
	row.ht();row.penup();row.goto(origin_x,origin_y);row.pendown()
	for i in range(1,Lignes+2):
		row.fd(Colonnes*30)
		row.penup();row.goto(origin_x,origin_y + i*30);row.pendown()
	t.update()

def Falling(board,block):
	pass

def Spawn():
	block = r.randint(0,6)
	if block == 

Play = True

board = [[0 for _ in range(Colonnes)] for _ in range(Lignes)]
Board()
while Play:
	Play = False
	input()
