import pygame as pg
import sys
import numpy as np
import time 

pg.init()
#dimensions
WIDTH = 600
HEIGHT = WIDTH
CIRCLE_RADIUS = 60
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

#colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (239,231,200)
CROSS_COLOR = (66,66,66)

game_over = False


screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Tic Tac Toe by Saif")
screen.fill( BG_COLOR)

#board
board = np.zeros( (BOARD_ROWS,BOARD_COLS) ) 

def draw_lines():
    pg.draw.line( screen, LINE_COLOR, (0, 200), (WIDTH,200), 15)
    pg.draw.line( screen, LINE_COLOR, (0, 400), (WIDTH, 400), 15)
    pg.draw.line( screen, LINE_COLOR, (200,0), (200,HEIGHT), 15)
    pg.draw.line( screen, LINE_COLOR, (400,0), (400,HEIGHT), 15)
    
def mark_square( row, col, player):
    board[row][col] = player

def available_square(row,col):
    if board[row][col] == 0:
        return True
    else:
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pg.draw.circle( screen, CIRCLE_COLOR, (int(col*200 + 200//2), int(row*200 + 200//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pg.draw.line( screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 -SPACE, row * 200 + SPACE), CROSS_WIDTH)
                pg.draw.line( screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE), (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
    
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player: 
        draw_desc_diagonal(player)
        return True
    
    return False

def draw_vertical_winning_line(col,player):
    posX = col * 200 + 200//2
    
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pg.draw.line(screen, color, (posX, 15), (posX, HEIGHT -15 ), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 200//2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pg.draw.line( screen, color, (15, posY), (WIDTH - 15, posY), 15)
def draw_asc_diagonal(player):

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pg.draw.line(screen, color, (15, HEIGHT -15), (WIDTH - 15, 15),15)
def draw_desc_diagonal(player):

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pg.draw.line(screen,color, (15,15), (WIDTH-15, HEIGHT - 15), 15)
def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    game_over = False
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
            
draw_lines()

player = 1



# main loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        
        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)

            if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = 2
                
                elif player == 2:
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
        
        


        if event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                restart()
                game_over = False
    pg.display.update()
