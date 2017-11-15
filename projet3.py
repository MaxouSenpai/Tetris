import turtle as t
import random as r
import time

Colonnes = 8
Lignes = 20
Epais = 30

board = [[0 for _ in range(Colonnes)] for _ in range(Lignes)]

origin_x = (-Colonnes//2*Epais)
origin_y = (-Colonnes//2*Epais-150)

spawn_x = -2*Epais
spawn_y = origin_y + Lignes*Epais

Briques = []

def Board():
	t.bgcolor("grey")
	t.tracer(False)
	column = t.Pen()
	column.ht();column.penup();column.goto(origin_x,origin_y);column.pendown()
	column.left(90)
	for i in range(1,Colonnes+2):
		column.fd(Lignes*Epais)
		column.penup();column.goto(origin_x + i*Epais,origin_y);column.pendown()

	row = t.Pen()
	row.ht();row.penup();row.goto(origin_x,origin_y);row.pendown()
	for i in range(1,Lignes+2):
		row.fd(Colonnes*Epais)
		row.penup();row.goto(origin_x,origin_y + i*Epais);row.pendown()
	
	t.update()


def Falling():
	y = blockp.pos()[1]
	if block == 0:
		y += Epais
	return y >= origin_y + 2 * Epais

def block0():
	print('Yes')

def block1():
	print('Yes')

def block2():
	print('Yes')

def block3():
	blockp.pendown();blockp.color("yellow");blockp.begin_fill()
	for _ in range(4):
		blockp.fd(2*Epais);blockp.right(90)
	blockp.end_fill()
	blockp.penup()

def block4():
	print('Yes')

def block5():
	print('Yes')

def block6():
	print('Yes')


def Moving_part(block):
	# Must add an exception when a block can't be spawned --> Game lost
	inst[block]()
	time.sleep(1)
	t.update()
	while Falling():
		blockp.clear();blockp.right(90);blockp.fd(Epais);blockp.left(90);time.sleep(1)
		inst[block]()
		t.update()



	t.update()
def Spawn(block):
	if block in (3,4,5):
		blockp.fd(Epais)

	elif block == 2:
		blockp.fd(2 * Epais)


Play = True

inst = (block0,block1,block2,block3,block4,block5,block6)

blockp = t.Pen();blockp.ht();blockp.penup();blockp.goto(spawn_x,spawn_y)

board = [[0 for _ in range(Colonnes)] for _ in range(Lignes)]
Board()
block = 3
Spawn(block)
Moving_part(block)
input()

