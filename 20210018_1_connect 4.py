# Connect 4 game
# each player put coin and the player who connect 4 coins consecutively in vertical or horizontal or diagonal way be the winner
# Author: Ahmed Reda Elsayed
# Date: 04-03-2022


import numpy
import pygame
import os


FPS = 60
ROW_NUM = 6
COLUMN_NUM = 7
WIDTH, HEIGHT = 700, 600
RED, YELLOW, BLACK, WHITE = (
    255, 0, 0), (255, 255, 0), (0, 0, 0), (255, 255, 255)
COIN_RADIUS = 43
FONT_SIZE = 100


# build board with 6 rows and 7 columns
def create_board():
    board = numpy.zeros((ROW_NUM, COLUMN_NUM))
    return board


# check that column is not full
def check_location(board, column):
    return board[5][column] == 0


# check that row in chosen column is empty to put coins as if not the coin will go to the next row
def check_next_row(board, column):
    for r in range(ROW_NUM):
        if board[r][column] == 0:
            return r


# put coins in chosen column but first check that column is not full and then check in which row it will be
def put_coins(board, row, column, coin):
    board[row][column] = coin


# this function flip the board as when i test to enter coins i found it in the upper row
def flip_board(board):
    print(numpy.flip(board, 0))


# check all win conditions
def win_conditions(board, coin):
    # check horizontal win
    for c in range(COLUMN_NUM - 3):
        for r in range(ROW_NUM):
            if board[r][c] == coin and board[r][c+1] == coin and board[r][c+2] == coin and board[r][c+3] == coin:
                return True
    # check vertical win
    for c in range(COLUMN_NUM):
        for r in range(ROW_NUM - 3):
            if board[r][c] == coin and board[r+1][c] == coin and board[r+2][c] == coin and board[r+3][c] == coin:
                return True
    # check diagonal win
    for c in range(COLUMN_NUM - 3):
        for r in range(ROW_NUM - 3):
            if board[r][c] == coin and board[r+1][c+1] == coin and board[r+2][c+2] == coin and board[r+3][c+3] == coin:
                return True

    for c in range(COLUMN_NUM - 3):
        for r in range(3, ROW_NUM):
            if board[r][c] == coin and board[r-1][c+1] == coin and board[r-2][c+2] == coin and board[r-3][c+3] == coin:
                return True


# check drew
def drew_condition(board):
    if board[5][0] != 0 and board[5][1] != 0 and board[5][2] != 0 and board[5][3] != 0 and board[5][4] != 0 and board[5][5] != 0 and board[5][6] != 0:
        return True

# this functions draw coins as it replace 1 with red coins and 2 with yellow coin


def draw_coins(board):
    for c in range(COLUMN_NUM):
        for r in range(ROW_NUM):
            if board[r][c] == 1:
                pygame.draw.circle(
                    WINDOW, RED, (int(c*100+52), HEIGHT - int(r*100+47)), COIN_RADIUS)
            if board[r][c] == 2:
                pygame.draw.circle(WINDOW, YELLOW, (int(
                    c*100+52), HEIGHT - int(r*100+47)), COIN_RADIUS)


# this function used to write on the window
def write_on_window(text, z):
    font = pygame.font.SysFont("comicsans", FONT_SIZE)
    draw_text = font.render(text, 1, BLACK)
    WINDOW.blit(draw_text, (z, 25))


pygame.init()

board = create_board()
flip_board(board)
turn = 0

# to generate the screen window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill(WHITE)  # give the screen white colour

pygame.display.set_caption("CONNECT 4")

BACKGROUND = pygame.image.load(os.path.join(
    'connect4_pygame', '20210018_background.png'))
# please put code file with the image
# and if put them in folder write folder name in the code before 'background.png'
# as if folder name is (assignment 1) edit code to (BACKGROUND = pygame.image.load(os.path.join('assignment 1', '20210018_background.png')) )

# change the dimension of the image
B_G = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))
WINDOW.blit(B_G, (0, 0))  # generate the image to the screen

pygame.display.update()  # update anything happened to be shown on the screen


def main(board, turn):
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # check that if quit or exit from the screen game it will be close
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # this mean that if click with mouse it will go on this if

                if turn == 0:
                    # event.pos[0] get x-axis position at which the mouse clicked
                    position_by_click = event.pos[0]
                    # divided 100 to reduce the range from (0 and 700) to (0 and 7)
                    column = int(position_by_click/100)
                    turn += 1  # change the player turn

                    if check_location(board, column):
                        row = check_next_row(board, column)
                        put_coins(board, row, column, 1)
                        print("*************************")
                        flip_board(board)
                        draw_coins(board)

                        if win_conditions(board, 1):
                            write_on_window(text="player1 win", z=100)
                            run = False

                        if drew_condition(board):
                            write_on_window(text="drew", z=235)
                            run = False

                else:
                    # event.pos[0] get x-axis position at which the mouse clicked
                    position_by_click = event.pos[0]
                    # divided 100 to reduce the range from (0 and 700) to (0 and 7)
                    column = int(position_by_click/100)
                    turn -= 1  # change the player turn

                    if check_location(board, column):
                        row = check_next_row(board, column)
                        put_coins(board, row, column, 2)
                        print("*************************")
                        flip_board(board)
                        draw_coins(board)

                        if win_conditions(board, 2):
                            write_on_window(text="player2 win", z=100)
                            run = False

                        if drew_condition(board):
                            write_on_window(text="drew", z=235)
                            run = False

        pygame.display.update()

    # when the game end it delay the screen for 5 second before close
    pygame.time.delay(5000)


main(board, turn)
