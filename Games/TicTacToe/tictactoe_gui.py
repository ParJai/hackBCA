import pygame
import threading
from copy import deepcopy
from random import choice, randint

class Board:
    def __init__(self, board_size: int) -> None:
        self.board_size = board_size
        self.boardArr = [[0 for i in range(self.board_size)] for i in range(self.board_size)]
        self.possibleMoves = [i for i in range(self.board_size ** 2)]

    def printBoard(self) -> None:
        for row in self.boardArr:
            for char in row:
                print(char, end=" ")
            print()
    
    def getRows(self) -> list:
        return self.boardArr
    
    def getColumns(self) -> list:
        columns = [[] for i in range(self.board_size)]
        for i in range(self.board_size):
            for j in range(self.board_size):
                columns[j].append(self.boardArr[i][j])
        return columns
    
    def getDiagonals(self) -> list:
        n_1_inc = self.board_size + 1
        n_2_inc = self.board_size - 1
        n_1 = 0
        n_2 = n_2_inc
        diagonals = [[], []]
        while n_1 < self.board_size ** 2 and n_2 < self.board_size ** 2:
            n_1_x = n_1 // self.board_size
            n_1_y = n_1 % self.board_size
            n_2_x = n_2 // self.board_size
            n_2_y = n_2 % self.board_size
            diagonals[0].append(self.boardArr[n_1_x][n_1_y])
            diagonals[1].append(self.boardArr[n_2_x][n_2_y])
            n_1 += n_1_inc
            n_2 += n_2_inc
        return diagonals
    
    def checkSubset(self, listOfLists: list):
        same = True
        checkChar = ""
        for i in listOfLists:
            if "B" in i:
                continue
            for j in range(len(i)):
                if j == 0:
                    checkChar = i[j]
                elif i[j] != checkChar:
                    same = False
                    break
            if same:
                return checkChar
        
        return 0
    
    def checkBoard(self):
        rowsChar = self.checkSubset(self.getRows())
        columnsChar = self.checkSubset(self.getColumns())
        diagonalsChar = self.checkSubset(self.getDiagonals())
        if rowsChar == "X" or rowsChar == "O":
            return rowsChar
        elif columnsChar == "X" or columnsChar == "O":
            return columnsChar
        elif diagonalsChar == "X" or diagonalsChar == "O":
            return diagonalsChar
        return 0

    def returnCenter(self) -> list:
        center = []
        for i in range(self.board_size):
            for j in range(self.board_size):
                if i != 0 and j != 0 and i != self.board_size-1 and j != self.board_size-1:
                    center.append(self.boardArr[i][j])
        return center
    
    def addMove(self, pos: int, char: str) -> None:
        self.boardArr[pos // self.board_size][pos % self.board_size] = char
        self.possibleMoves.remove(pos)
    
    def getBoardSize(self):
        return self.board_size
class AI:
    def __init__(self, board : Board, turnNum : int) -> None:
        self.board = board
        self.turnNum = turnNum
        self.turnPiece = "X" if turnNum == 0 else "O"

    def isWinningMove(self, row : int, col : int) -> bool: #check if the position is a win move
        tempBoard = deepcopy(self.board)
        tempBoard.addMove(row*self.board.board_size+col, self.turnPiece)
        return tempBoard.checkBoard() == self.turnPiece #check for wins, either return True or False

    def checkForForks(self, row : int, col : int) -> bool: #check if the position is a fork
        tempBoard = deepcopy(self.board) #make a copy of Grid
        tempBoard.addMove(row*self.board.board_size+col, self.turnPiece)
        wins = 0 #keep track of how many win moves there are
        
        for i in self.board.possibleMoves:
                check = self.isWinningMove(i // self.board.board_size, i % self.board.board_size) #check if each position is a potential winning move for temp

                if check == True and self.board.boardArr == 0: #if so, and the position is empty:
                    wins += 1 #mark it as a winning move by adding 1 to wins
        
        return wins >= 2

    def getMove(self) -> int:
        for i in self.board.possibleMoves:
            if self.isWinningMove(i // self.board.board_size, i % self.board.board_size): #if the position is empty, and it is a winning move:
                return i
                
        for k in self.board.possibleMoves:
            if self.isWinningMove(k // self.board.board_size, k % self.board.board_size): #if the position is empty, and it is a winning move:
                return k
        
        for m in self.board.possibleMoves:
            if self.checkForForks(m // self.board.board_size, m % self.board.board_size): #if the position is empty, and it is a fork move:
                return m
                
        for o in self.board.possibleMoves:
            if self.checkForForks(o // self.board.board_size, o % self.board.board_size): #if the position is empty, and it is a winning move:
                return o

        center = self.board.returnCenter()
        if len(center) == 1:
            if 4 in self.board.possibleMoves: #first thing to check afterwards is center
                return 4
        else:
            newAI = AI(center, self.turnNum)
            if 0 in center:
                return newAI.getMove()
        
        corners = [(0, 0), (0, self.board.board_size-1), (self.board.board_size-1, 0), (self.board.board_size-1, self.board.board_size-1)]
        
        randomCorner = choice(corners) #randomly choose a corner
        if randomCorner[0]*self.board.board_size+randomCorner[1] in self.board.possibleMoves:
            return randomCorner[0]*self.board.board_size+randomCorner[1]
        else: #if the center and the corners are already full:
            while True: #just randomly choose a possible item
                row = randint(0, self.board.board_size)
                col = randint(0, self.board.board_size)
            
                if row*self.board.board_size+col in self.board.possibleMoves:
                    return row*self.board.board_size+col

class TicTacToe():
    def __init__(self, window, clock, client):
        self.client = client
        self.window = window
        self.clock = clock
        msg = ""
        sending = threading.Thread(target = self.client.send_message, args = (msg,), daemon = True)
        sending.start()
        recieving = threading.Thread(target = self.client.recieve_message, args = (), daemon = True)
        recieving.start()
        self.runGame()
    
    def runGame(self):
        pygame.init()

        white = (255, 255, 255)
        black = (0, 0, 0)
        blue = (0, 0, 255)
        red = (255, 0, 0)
        teal = (0, 128, 128)
        light_green = (124, 252, 0)
        screen = self.window

        x_rect = pygame.Rect((275+100, round(365*7/8)), (100, round(100*7/8)))
        o_rect = pygame.Rect((425+100, round(365*7/8)), (100, round(100*7/8)))

        play_rect = pygame.Rect((300+100, round(525*7/8)), (200, round(80*7/8)))
        quit_rect = pygame.Rect((300+100, round(675*7/8)), (200, round(80*7/8)))

        vs_player = pygame.Rect((50, round(525*7/8)), (300, round(80*7/8)))
        vs_computer = pygame.Rect((650, round(525*7/8)), (300, round(80*7/8)))
        opponent = ""
        computer = 0
        board = Board(3)

        player_1 = ''

        key_pressed = False
        click_pos = (0, 0)
        mouse_pos = (0, 0)

        one = ''
        two = ''
        three = ''
        four = ''
        five = ''
        six = ''
        seven = ''
        eight = ''
        nine = ''

        one_filled = False
        two_filled = False
        three_filled = False
        four_filled = False
        five_filled = False
        six_filled = False
        seven_filled = False
        eight_filled = False
        nine_filled = False

        to_draw = []

        tile_1 = pygame.Rect((20+100, round(20*7/8)), (240, round(240*7/8)))
        tile_2 = pygame.Rect((280+100, round(20*7/8)), (240, round(240*7/8)))
        tile_3 = pygame.Rect((540+100, round(20*7/8)), (240, round(240*7/8)))
        tile_4 = pygame.Rect((20+100, round(280*7/8)), (240, round(240*7/8)))
        tile_5 = pygame.Rect((280+100, round(280*7/8)), (240, round(240*7/8)))
        tile_6 = pygame.Rect((540+100, round(280*7/8)), (240, round(240*7/8)))
        tile_7 = pygame.Rect((20+100, round(540*7/8)), (240, round(240*7/8)))
        tile_8 = pygame.Rect((280+100, round(540*7/8)), (240, round(240*7/8)))
        tile_9 = pygame.Rect((540+100, round(540*7/8)), (240, round(240*7/8)))

        tiles = [
        tile_1, tile_2, tile_3,
        tile_4, tile_5, tile_6,
        tile_7, tile_8, tile_9
        ]

        player_1_x = ['', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        player_1_o = ['', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']

        turn = 1

        win_statement1 = ''
        win_statement2 = ''
        lose_statement1 = ''
        lose_statement2 = ''

        tie = False
        win = False
        home_screen = True
        running = True

        def write(text, font, text_size, center, color):
            text_font = pygame.font.Font(font, text_size)
            text_to_write = text_font.render(text, True, color)
            text_rect = text_to_write.get_rect()
            text_rect.center = center
            screen.blit(text_to_write, text_rect)

        def home():
            nonlocal player_1
            nonlocal home_screen
            nonlocal click_pos
            nonlocal opponent
            nonlocal computer
            nonlocal board
            screen.fill(teal)
            write('TIC-TAC-', 'bahnschrift.ttf', 100, (400+100, round(70*7/8)), white)
            write('TOE', 'bahnschrift.ttf', 150, (400+100, round(190*7/8)), white)
            write('Player 1, choose your symbol:', 'bahnschrift.ttf', 30, (400+100, round(320*7/8)), white)

            pygame.draw.rect(screen, teal, x_rect)
            pygame.draw.rect(screen, teal, o_rect)
            pygame.draw.rect(screen, teal, play_rect)
            pygame.draw.rect(screen, teal, quit_rect)

            if x_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, light_green, x_rect)
                pygame.draw.rect(screen, teal, o_rect)
            elif o_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, teal, x_rect)
                pygame.draw.rect(screen, light_green, o_rect)

            if quit_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, teal, play_rect)
                pygame.draw.rect(screen, light_green, quit_rect)

            if player_1 != '':
                if play_rect.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, light_green, play_rect)
                    pygame.draw.rect(screen, teal, quit_rect)

            write('X', 'tahoma.ttf', 75, (325+100, round(415*7/8)), white)
            write('O', 'tahoma.ttf', 75, (475+100, round(415*7/8)), white)
            write('PLAY', 'freesansbold.ttf', 50, (400+100, round(565*7/8)), white)
            write('QUIT', 'freesansbold.ttf', 50, (400+100, round(715*7/8)), white)
            pygame.draw.rect(screen, teal, vs_player)
            pygame.draw.rect(screen, teal, vs_computer)
            write('MULTIPLAYER', 'freesansbold.ttf', 35, vs_player.center, white)
            write('VS COMPUTER', 'freesansbold.ttf', 35, vs_computer.center, white)

            if click_pos != (0, 0):
                if x_rect.collidepoint(click_pos):
                    player_1 = 'X'
                    pygame.draw.rect(screen, light_green, x_rect)
                    pygame.draw.rect(screen, teal, o_rect)
                elif o_rect.collidepoint(click_pos):
                    player_1 = 'O'
                    pygame.draw.rect(screen, teal, x_rect)
                    pygame.draw.rect(screen, light_green, o_rect)

                write('X', 'tahoma.ttf', 75, (325+100, round(415*7/8)), white)
                write('O', 'tahoma.ttf', 75, (475+100, round(415*7/8)), white)
                if player_1 != '':
                    if vs_player.collidepoint(click_pos):
                        opponent = "Player"
                        pygame.draw.rect(screen, light_green, vs_player)
                        pygame.draw.rect(screen, teal, vs_computer)
                    elif vs_computer.collidepoint(click_pos):
                        opponent = "Computer"
                        computer = AI(board, 0 if player_1 == "X" else 1)
                        pygame.draw.rect(screen, light_green, vs_computer)
                        pygame.draw.rect(screen, teal, vs_player)
                
                write('MULTIPLAYER', 'freesansbold.ttf', 35, vs_player.center, white)
                write('VS COMPUTER', 'freesansbold.ttf', 35, vs_computer.center, white)

                if play_rect.collidepoint(click_pos):
                    if player_1 != '' and opponent != '':
                        click_pos = (0, 0)
                        game()
                        home_screen = False
                elif quit_rect.collidepoint(click_pos):
                    quit()
                else:
                    if player_1 == 'X':
                        pygame.draw.rect(screen, light_green, x_rect)
                        pygame.draw.rect(screen, teal, o_rect)
                    elif player_1 == 'O':
                        pygame.draw.rect(screen, teal, x_rect)
                        pygame.draw.rect(screen, light_green, o_rect)

                    write('X', 'tahoma.ttf', 75, (325+100, round(415*7/8)), white)
                    write('O', 'tahoma.ttf', 75, (475+100, round(415*7/8)), white)

            pygame.display.flip()

        def game():
            nonlocal click_pos
            nonlocal tie
            nonlocal win
            nonlocal turn
            nonlocal one_filled
            nonlocal two_filled
            nonlocal three_filled
            nonlocal four_filled
            nonlocal five_filled
            nonlocal six_filled
            nonlocal seven_filled
            nonlocal eight_filled
            nonlocal nine_filled
            nonlocal one
            nonlocal two
            nonlocal three
            nonlocal four
            nonlocal five
            nonlocal six
            nonlocal seven
            nonlocal eight
            nonlocal nine
            nonlocal to_draw
            nonlocal board
            screen.fill(black)
            for tile in tiles:
                pygame.draw.rect(screen, white, tile)
            if to_draw:
                for marker in to_draw:
                    write(marker[0], marker[1], marker[2], marker[3], marker[4])
            if click_pos != (0, 0):
                if not tie and not win:
                    if turn <= 9:
                        if opponent == "Computer":
                            if tile_1.collidepoint(click_pos):
                                if not one_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_1.center, blue))
                                            board.addMove(0, "X")
                                            one = 'X'
                                            one_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_1.center, blue))
                                            board.addMove(0, "O")
                                            one = 'O'
                                            one_filled = True
                                            turn += 1
                            elif tile_2.collidepoint(click_pos):
                                if not two_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_2.center, blue))
                                            board.addMove(1, "X")
                                            two = 'X'
                                            two_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_2.center, blue))
                                            board.addMove(1, "O")
                                            two = 'O'
                                            two_filled = True
                                            turn += 1
                            elif tile_3.collidepoint(click_pos):
                                if not three_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_3.center, blue))
                                            board.addMove(2, "X")
                                            three = 'X'
                                            three_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_3.center, blue))
                                            board.addMove(2, "O")
                                            three = 'O'
                                            three_filled = True
                                            turn += 1
                            elif tile_4.collidepoint(click_pos):
                                if not four_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_4.center, blue))
                                            board.addMove(3, "X")
                                            four = 'X'
                                            four_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_4.center, blue))
                                            board.addMove(3, "O")
                                            four = 'O'
                                            four_filled = True
                                            turn += 1
                            elif tile_5.collidepoint(click_pos):
                                if not five_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_5.center, blue))
                                            board.addMove(4, "X")
                                            five = 'X'
                                            five_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_5.center, blue))
                                            board.addMove(4, "O")
                                            five = 'O'
                                            five_filled = True
                                            turn += 1
                            elif tile_6.collidepoint(click_pos):
                                if not six_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_6.center, blue))
                                            board.addMove(5, "X")
                                            six = 'X'
                                            six_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_6.center, blue))
                                            board.addMove(5, "O")
                                            six = 'O'
                                            six_filled = True
                                            turn += 1
                            elif tile_7.collidepoint(click_pos):
                                if not seven_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_7.center, blue))
                                            board.addMove(6, "X")
                                            seven = 'X'
                                            seven_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_7.center, blue))
                                            board.addMove(6, "O")
                                            seven = 'O'
                                            seven_filled = True
                                            turn += 1
                            elif tile_8.collidepoint(click_pos):
                                if not eight_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_8.center, blue))
                                            board.addMove(7, "X")
                                            eight = 'X'
                                            eight_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_8.center, blue))
                                            board.addMove(7, "O")
                                            eight = 'O'
                                            eight_filled = True
                                            turn += 1
                            elif tile_9.collidepoint(click_pos):
                                if not nine_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_9.center, blue))
                                            board.addMove(8, "X")
                                            nine = 'X'
                                            nine_filled = True
                                            turn += 1
                                    else:
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_o[turn], 'tahoma.ttf', 150, tile_9.center, blue))
                                            board.addMove(8, "O")
                                            nine = 'O'
                                            nine_filled = True
                                            turn += 1
                            click_pos = (0, 0)
                            check_win()
                            if not tie and not win:
                                computerMove = computer.getMove()
                                if computerMove == 0:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_1.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(0, computerPiece)
                                    one = computerPiece
                                    one_filled = True
                                    turn += 1
                                elif computerMove == 1:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_2.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(1, computerPiece)
                                    two = computerPiece
                                    two_filled = True
                                    turn += 1
                                elif computerMove == 2:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_3.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(2, computerPiece)
                                    three = computerPiece
                                    three_filled = True
                                    turn += 1
                                elif computerMove == 3:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_4.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(3, computerPiece)
                                    four = computerPiece
                                    four_filled = True
                                    turn += 1
                                elif computerMove == 4:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_5.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(4, computerPiece)
                                    five = computerPiece
                                    five_filled = True
                                    turn += 1
                                elif computerMove == 5:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_6.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(5, computerPiece)
                                    six = computerPiece
                                    six_filled = True
                                    turn += 1
                                elif computerMove == 6:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_7.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(6, computerPiece)
                                    seven = computerPiece
                                    seven_filled = True
                                    turn += 1
                                elif computerMove == 7:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_8.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(7, computerPiece)
                                    eight = computerPiece
                                    eight_filled = True
                                    turn += 1
                                elif computerMove == 8:
                                    to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_9.center, red))
                                    computerPiece = "X" if player_1 == "O" else "O"
                                    board.addMove(8, computerPiece)
                                    nine = computerPiece
                                    nine_filled = True
                                    turn += 1
                        else:
                            move = 0
                            if tile_1.collidepoint(click_pos):
                                if not one_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_1.center, blue))
                                            board.addMove(0, "X")
                                            one = 'X'
                                            one_filled = True
                                            turn += 1
                                            move = 0
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_1.center, blue))
                                            board.addMove(0, "O")
                                            one = 'O'
                                            one_filled = True
                                            turn += 1
                                            move = 0
                            elif tile_2.collidepoint(click_pos):
                                if not two_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_2.center, blue))
                                            board.addMove(1, "X")
                                            two = 'X'
                                            two_filled = True
                                            turn += 1
                                            move = 1
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_2.center, blue))
                                            board.addMove(1, "O")
                                            two = 'O'
                                            two_filled = True
                                            turn += 1
                                            move = 1
                            elif tile_3.collidepoint(click_pos):
                                if not three_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_3.center, blue))
                                            board.addMove(2, "X")
                                            three = 'X'
                                            three_filled = True
                                            turn += 1
                                            move = 2
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_3.center, blue))
                                            board.addMove(2, "O")
                                            three = 'O'
                                            three_filled = True
                                            turn += 1
                                            move = 2
                            elif tile_4.collidepoint(click_pos):
                                if not four_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_4.center, blue))
                                            board.addMove(3, "X")
                                            four = 'X'
                                            four_filled = True
                                            turn += 1
                                            move = 3
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_4.center, blue))
                                            board.addMove(3, "O")
                                            four = 'O'
                                            four_filled = True
                                            turn += 1
                                            move = 3
                            elif tile_5.collidepoint(click_pos):
                                if not five_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_5.center, blue))
                                            board.addMove(4, "X")
                                            five = 'X'
                                            five_filled = True
                                            turn += 1
                                            move = 4
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_5.center, blue))
                                            board.addMove(4, "O")
                                            five = 'O'
                                            five_filled = True
                                            turn += 1
                                            move = 4
                            elif tile_6.collidepoint(click_pos):
                                if not six_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_6.center, blue))
                                            board.addMove(5, "X")
                                            six = 'X'
                                            six_filled = True
                                            turn += 1
                                            move = 5
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_6.center, blue))
                                            board.addMove(5, "O")
                                            six = 'O'
                                            six_filled = True
                                            turn += 1
                                            move = 5
                            elif tile_7.collidepoint(click_pos):
                                if not seven_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_7.center, blue))
                                            board.addMove(6, "X")
                                            seven = 'X'
                                            seven_filled = True
                                            turn += 1
                                            move = 6
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_7.center, blue))
                                            board.addMove(6, "O")
                                            seven = 'O'
                                            seven_filled = True
                                            turn += 1
                                            move = 6
                            elif tile_8.collidepoint(click_pos):
                                if not eight_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_8.center, blue))
                                            board.addMove(7, "X")
                                            eight = 'X'
                                            eight_filled = True
                                            turn += 1
                                            move = 7
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_8.center, blue))
                                            board.addMove(7, "O")
                                            eight = 'O'
                                            eight_filled = True
                                            turn += 1
                                            move = 7
                            elif tile_9.collidepoint(click_pos):
                                if not nine_filled:
                                    if player_1 == 'X':
                                        if player_1_x[turn] == 'X':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_9.center, blue))
                                            board.addMove(8, "X")
                                            nine = 'X'
                                            nine_filled = True
                                            turn += 1
                                            move = 8
                                    else:
                                        if player_1_x[turn] == 'O':
                                            to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_9.center, blue))
                                            board.addMove(8, "O")
                                            nine = 'O'
                                            nine_filled = True
                                            turn += 1
                                            move = 8
                            click_pos = (0, 0)
                            check_win()
                            self.client.messageQueue.append(str(move))
                pygame.display.flip()
                check_win()

        def check_win():
            nonlocal win
            nonlocal win_statement1
            nonlocal win_statement2
            nonlocal lose_statement1
            nonlocal lose_statement2
            nonlocal tie
            nonlocal to_draw
            if (one == two == three) or (four == five == six) or (seven == eight == nine) or (one == four == seven) or (two == five == eight) or (three == six == nine) or (one == five == nine) or (three == five == seven):
                if (one == two == three == 'X') or (four == five == six == 'X') or (seven == eight == nine == 'X') or (one == four == seven == 'X') or (two == five == eight == 'X') or (three == six == nine == 'X') or (one == five == nine == 'X') or (three == five == seven == 'X'):
                    if player_1 == 'X':
                        win_statement1 = 'Congratulations Player 1 (X),'
                        win_statement2 = 'YOU WIN!'
                        lose_statement1 = 'Better luck next time,'
                        lose_statement2 = 'Player 2 (O).'
                        win = True
                    elif player_1 == 'O':
                        win_statement1 = 'Congratulations Player 2 (X),'
                        win_statement2 = 'YOU WIN!'
                        lose_statement1 = 'Better luck next time,'
                        lose_statement2 = 'Player 1 (O).'
                        win = True
                elif (one == two == three == 'O') or (four == five == six == 'O') or (seven == eight == nine == 'O') or (one == four == seven == 'O') or (two == five == eight == 'O') or (three == six == nine == 'O') or (one == five == nine == 'O') or (three == five == seven == 'O'):
                    if player_1 == 'O':
                        win_statement1 = 'Congratulations Player 1 (O),'
                        win_statement2 = 'YOU WIN!'
                        lose_statement1 = 'Better luck next time,'
                        lose_statement2 = 'Player 2 (X).'
                        win = True
                    elif player_1 == 'X':
                        win_statement1 = 'Congratulations Player 2 (O),'
                        win_statement2 = 'YOU WIN!'
                        lose_statement1 = 'Better luck next time,'
                        lose_statement2 = 'Player 1 (X).'
                        win = True
            if len(to_draw) == 9:
                if not (one == two == three) or (four == five == six) or (seven == eight == nine) or (one == four == seven) or (two == five == eight) or (three == six == nine) or (one == five == nine) or (three == five == seven):
                    tie = True

        def end_screen(statement1, statement2, statement3, statement4):
            nonlocal key_pressed
            nonlocal click_pos
            nonlocal player_1
            nonlocal one
            nonlocal two
            nonlocal three
            nonlocal four
            nonlocal five
            nonlocal six
            nonlocal seven
            nonlocal eight
            nonlocal nine
            nonlocal one_filled
            nonlocal two_filled
            nonlocal three_filled
            nonlocal four_filled
            nonlocal five_filled
            nonlocal six_filled
            nonlocal seven_filled
            nonlocal eight_filled
            nonlocal nine_filled
            nonlocal to_draw
            nonlocal turn
            nonlocal home_screen
            nonlocal win
            nonlocal tie
            nonlocal board
            nonlocal opponent
            nonlocal computer
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            transparent_surface = pygame.Surface((1000, 700), pygame.SRCALPHA)
            transparent_surface.fill((60, 179, 113, 128))
            screen.blit(transparent_surface, (0, 0))
            write(statement1, 'freesansbold.ttf', 50, (400+100, round(135*7/8)), white)
            write(statement2, 'freesansbold.ttf', 80, (400+100, round(250*7/8)), white)
            write(statement3, 'freesansbold.ttf', 50, (400+100, round(400*7/8)), white)
            write(statement4, 'freesansbold.ttf', 50, (400+100, round(495*7/8)), white)
            write('(PRESS ANY KEY TO PLAY AGAIN)', 'freesansbold.ttf', 40, (400+100, round(650*7/8)), white)
            pygame.display.flip()
            if key_pressed:
                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                player_1 = ''
                one = ''
                two = ''
                three = ''
                four = ''
                five = ''
                six = ''
                seven = ''
                eight = ''
                nine = ''
                one_filled = False
                two_filled = False
                three_filled = False
                four_filled = False
                five_filled = False
                six_filled = False
                seven_filled = False
                eight_filled = False
                nine_filled = False
                to_draw = []
                turn = 1
                home_screen = True
                key_pressed = False
                tie = False
                win = False
                computer = 0
                board = Board(3)
                opponent = ""

        def tie_screen():
            nonlocal key_pressed
            nonlocal click_pos
            nonlocal player_1
            nonlocal one
            nonlocal two
            nonlocal three
            nonlocal four
            nonlocal five
            nonlocal six
            nonlocal seven
            nonlocal eight
            nonlocal nine
            nonlocal one_filled
            nonlocal two_filled
            nonlocal three_filled
            nonlocal four_filled
            nonlocal five_filled
            nonlocal six_filled
            nonlocal seven_filled
            nonlocal eight_filled
            nonlocal nine_filled
            nonlocal to_draw
            nonlocal turn
            nonlocal home_screen
            nonlocal tie
            nonlocal win
            nonlocal computer
            nonlocal board
            nonlocal opponent
            
            pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            transparent_surface = pygame.Surface((1000, 700), pygame.SRCALPHA)
            transparent_surface.fill((60, 179, 113, 128))
            screen.blit(transparent_surface, (0, 0))
            write('DRAW', 'freesansbold.ttf', 170, (400+100, round(350*7/8)), white)
            write('(PRESS ANY KEY TO PLAY AGAIN)', 'freesansbold.ttf', 43, (400+100, round(500*7/8)), white)
            pygame.display.flip()
            if key_pressed:
                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                player_1 = ''
                one = ''
                two = ''
                three = ''
                four = ''
                five = ''
                six = ''
                seven = ''
                eight = ''
                nine = ''
                one_filled = False
                two_filled = False
                three_filled = False
                four_filled = False
                five_filled = False
                six_filled = False
                seven_filled = False
                eight_filled = False
                nine_filled = False
                to_draw = []
                turn = 1
                home_screen = True
                key_pressed = False
                win = False
                tie = False
                computer = 0
                board = Board(3)
                opponent = ""

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_pos = pygame.mouse.get_pos()
                    if len(self.client.recievingQueue) != 0:
                        print(self.client.recievingQueue[0])
                        if not tie and not win:
                            computerMove = int(self.client.recievingQueue[0][1])
                            if computerMove == 0:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_1.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(0, computerPiece)
                                one = computerPiece
                                one_filled = True
                                turn += 1
                            elif computerMove == 1:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_2.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(1, computerPiece)
                                two = computerPiece
                                two_filled = True
                                turn += 1
                            elif computerMove == 2:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_3.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(2, computerPiece)
                                three = computerPiece
                                three_filled = True
                                turn += 1
                            elif computerMove == 3:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_4.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(3, computerPiece)
                                four = computerPiece
                                four_filled = True
                                turn += 1
                            elif computerMove == 4:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_5.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(4, computerPiece)
                                five = computerPiece
                                five_filled = True
                                turn += 1
                            elif computerMove == 5:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_6.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(5, computerPiece)
                                six = computerPiece
                                six_filled = True
                                turn += 1
                            elif computerMove == 6:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_7.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(6, computerPiece)
                                seven = computerPiece
                                seven_filled = True
                                turn += 1
                            elif computerMove == 7:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_8.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(7, computerPiece)
                                eight = computerPiece
                                eight_filled = True
                                turn += 1
                            elif computerMove == 8:
                                to_draw.append((player_1_x[turn], 'tahoma.ttf', 150, tile_9.center, red))
                                computerPiece = "X" if player_1 == "O" else "O"
                                board.addMove(8, computerPiece)
                                nine = computerPiece
                                nine_filled = True
                                turn += 1
                        click_pos = (0, 0)
                        del self.client.recievingQueue[0]
                elif event.type == pygame.KEYDOWN:
                    key_pressed = True
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()

            if home_screen:
                home()
            else:
                game()

            if win:
                end_screen(win_statement1, win_statement2, lose_statement1, lose_statement2)
            elif tie:
                tie_screen()

            pygame.display.flip()