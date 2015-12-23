# -*- coding: latin-1 -*-
import pygame,math,sys
from pygame.locals import *
import os
from random import *
from pygame.compat import geterror
BLACK = (0,0,0)
WHITE = (255,255,255)
waterFlowConstant = 20


##lets go
def waterTick(waterBoard,board,prev,curr,score,scoreCheck):
	(previousX,previousY) = prev
	(currentX,currentY) = curr
	up = 0 #up to down
	left = 0 #left to right
	if previousX < currentX:
		left = 1
	if previousY < currentY:
		up = 1
	if previousX > currentX:
		left = 2
	if previousY > currentY:
		up = 2

	tile = board[currentX][currentY]
	tileNR = tile[0]
	angle = tile[1]
	gameOver = 0	
	if tileNR == 0:
		if angle == 90 or angle == 270:
			if up == 1:
				gameOver =1
			elif up == 2:
				gameOver =1
			elif left == 1:
				waterBoard[currentX + 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX +1 ,currentY)
				
			elif left == 2:
				waterBoard[currentX - 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr =( currentX -1 ,currentY)
				
		else:
			if up == 1:
				waterBoard[currentX  ][currentY +1] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX,currentY +1)
			elif up == 2:
				waterBoard[currentX][currentY-1] = (1,0)
				prev = (currentX,currentY)
				curr =(currentX,currentY-1)
				
			elif left == 1:
				gameOver =1
			elif left == 2:
				gameOver =1
		
	elif tileNR == 1 or tileNR == 2 or tileNR == 3:
		if angle == 90:
			if up == 1:
				gameOver =1
			elif up == 2:
				waterBoard[currentX - 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX -1 ,currentY)
				
			elif left == 1:
				waterBoard[currentX][currentY+1] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX ,currentY+1)
				
			elif left == 2:
				gameOver =1
				
		elif angle == 180:
			if up == 1:
				gameOver =1
			elif up == 2:
				waterBoard[currentX + 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX +1 ,currentY)
			elif left == 1:
				gameOver =1
				
			elif left == 2:
				waterBoard[currentX][currentY +1] = (1,0)
				prev = (currentX,currentY)
				curr =( currentX,currentY +1)
				
		elif angle == 270:
			if up == 1:
				waterBoard[currentX + 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX +1 ,currentY)
			elif up == 2:
				gameOver =1
			elif left == 1:
				gameOver =1
				
			elif left == 2:
				waterBoard[currentX  ][currentY-1] = (1,0)
				prev = (currentX,currentY)
				curr =( currentX  ,currentY -1)
				
		else:
			if up == 1:
				waterBoard[currentX - 1 ][currentY] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX - 1 ,currentY)
			elif up == 2:
				gameOver =1
			elif left == 1:
				waterBoard[currentX ][currentY-1] = (1,0)
				prev = (currentX,currentY)
				curr = (currentX ,currentY-1)
				
			elif left == 2:
				gameOver =1
	
	elif tileNR == 4:
		if up == 2:
			if currentY == 0:		
				waterBoard[currentX ][8] = (1,0)
				prev = (currentX,9)
				curr = (currentX ,8)
				scoreCheck = 1
			else:
				waterBoard[currentX][currentY-1] = (1,0)
				prev = (currentX,currentY)
				curr =(currentX,currentY-1)
			
		elif up == 1:
			if currentY == 8:		
				waterBoard[currentX ][0] = (1,0)
				prev = (currentX,-1)
				curr = (currentX ,0)
				scoreCheck = 1
			else:
				waterBoard[currentX][currentY+1] = (1,0)
				prev = (currentX,currentY)
				curr =(currentX,currentY+1)
				
	elif tileNR == 5:
		if left == 2:
			if currentX == 0:		
				waterBoard[8][currentY] = (1,0)
				prev = (9,currentY)
				curr = (8 ,currentY)
				scoreCheck = 1
			else:
				waterBoard[currentX-1][currentY] = (1,0)
				prev = (currentX,currentY)
				curr =(currentX-1,currentY)
			
		elif left == 1:
			if currentX == 8:		
				waterBoard[0][currentY] = (1,0)
				prev = (-1,currentY)
				curr = (0 ,currentY)
				scoreCheck = 1
			else:
				waterBoard[currentX+1][currentY] = (1,0)
				prev = (currentX,currentY)
				curr =(currentX+1,currentY)
	score += 1
	return (waterBoard,prev,curr,gameOver,score,scoreCheck)	
	
def resetWaterSquares(board,waterBoard,prev,curr):
	for i in range(9):
		for j in range(9):
			if not ( i == curr[0] and j == curr[1]) and waterBoard[i][j][0] == 1:
				waterBoard[i][j] = (0,0)
				if board[i][j][0] != 4 and board [i][j][0] != 5:
					board[i][j] = (randint(0,3),(randint(0,3) *90))


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
	
def getWaterTile(tileNr):
	return {
		0: "../res/pipeUpDownWater.png",
        1: "../res/pipeTurnWater.png",
        2: "../res/pipeTurnWater.png",
		3: "../res/pipeTurnWater.png",
		4: "../res/pipeStuckUpDownWater.png",
		5: "../res/pipeStuckLeftRightWater.png",
		
		
	}[tileNr]

	
def getTile(tileNr):
	return {
		0: "../res/pipeUpDown.png",
        1: "../res/pipeTurn.png", #1: "pipeTsection.png",
        2: "../res/pipeTurn.png",#2: "pipeCross.png",
		3: "../res/pipeTurn.png",
		4: "../res/pipeStuckUpDown.png",
		5: "../res/pipeStuckLeftRight.png",
		
	}[tileNr]

	
def createEmptyWaterBoard(xSquareNumber,ySquareNumber):
	#board = [[(randint(0,3),(0)) for x in range(9)] for x in range(9)]
	waterBoard = [[(0,0) for x in range(9)] for x in range(9)]
	waterBoard[0][4] = (1,0)
	waterBoard[1][4] = (1,0)
	return (waterBoard,(0,4),(1,4))
	
	
	
def createBoard(xSquareNumber,ySquareNumber):
	#board = [[(randint(0,3),(0)) for x in range(9)] for x in range(9)]
	board = [[(randint(0,3),(randint(0,3) *90)) for x in range(9)] for x in range(9)]
	for i in range(xSquareNumber):
		board[0][i] = (5,0)
		board[i][0] = (4,0)
		board[xSquareNumber-1][i] = (5,0)
		board[i][xSquareNumber-1] = (4,0)		
	board[1][4] = (0,90)
	return board
	
def startGraphics(w,h):
	pygame.init()
	screen = pygame.display.set_mode((1600,900),FULLSCREEN)
	
	pygame.display.flip()
	running = 1
	background = pygame.image.load("../res/background.png").convert()			
	background = pygame.transform.scale(background, (w,h))
	backgroundpos = background.get_rect(center=(w/2,h/2))
	screen.blit(background,backgroundpos)		
	pygame.display.flip()
	return screen		
		
w = 1600
h = 900
SQUARESIZE = h/9 -1
UIStartX = SQUARESIZE*9
screen = startGraphics(w,h)
play = 1
xSquareNumber,ySquareNumber = 9,9
board = createBoard(xSquareNumber,ySquareNumber)
WB = createEmptyWaterBoard(xSquareNumber,ySquareNumber)
waterBoard = WB[0]
prev = WB[1]
curr = WB[2]
score = 0
scoreCheck = 0
clock = pygame.time.Clock()
scoreToReset = 15
timer = 0
print("hello")
while play:
	
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				pygame.display.quit()
				
		elif event.type == pygame.MOUSEBUTTONDOWN:
			(x,y) = pygame.mouse.get_pos()
			(newX,newY) = (x/SQUARESIZE,y/SQUARESIZE)
			if (newX < xSquareNumber - 1 and newY < ySquareNumber -1 and newX > 0 and newY > 0) and waterBoard[newX][newY][0] != 1:
				tuple = board[newX][newY]
				angle = tuple[1] 
				angle = angle - 90 
				angle = angle % 360
				board[newX][newY] = (tuple[0],angle)
			
	panel = pygame.image.load("../res/panel.jpg").convert()
	panel = pygame.transform.scale(panel, (w-UIStartX, h))
	screen.blit(panel,(UIStartX, 0))
	
	
	for i in range(len(board)):
		for j in range(len(board)):
			tuple = board[i][j]
			tileName = getTile(tuple[0])
			gridpart = pygame.image.load(tileName).convert()
			gridpart = pygame.transform.scale(gridpart, (SQUARESIZE,SQUARESIZE) )	
			gridpart = rot_center(gridpart,tuple[1]) #WOOT
			
			screen.blit(gridpart,(i*SQUARESIZE,j*SQUARESIZE))
			tuple2 = waterBoard[i][j]
			if (tuple2[0] == 1):#contains water
				tileName = getWaterTile(tuple[0]) #using boards tuple
				waterPart = pygame.image.load(tileName).convert()
				waterPart = pygame.transform.scale(waterPart, (SQUARESIZE,SQUARESIZE) )	
				waterPart = rot_center(waterPart,tuple[1]) #WOOT
				waterPart.set_colorkey(WHITE)
				screen.blit(waterPart,(i*SQUARESIZE,j*SQUARESIZE))	
	
			
	pygame.display.flip()
	
	timer += 1
	if timer % waterFlowConstant == 0:
		res = waterTick(waterBoard,board,prev,curr,score,scoreCheck)
		waterBoard = res[0]
		prev = res[1]
		curr = res[2]
		gameOver = res[3]
		score = res[4]
		scoreCheck = res[5]
		if scoreCheck == 1:
			scoreCheck = 0
			if score >= scoreToReset:
				score = 0
				resetWaterSquares(board,waterBoard,prev,curr)
		if gameOver:
			pygame.display.quit()
			
	clock.tick(60)
				


