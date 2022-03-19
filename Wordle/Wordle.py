#Wordle

import pygame
import Logic
pygame.init()
logic = Logic.Logic()


YELLOW = [255,255,0]
WHITE = [255,255,255]
GREEN = [0,128,0]
BLACK = [0,0,0]
CHARCOAL = [54,69,79]
KEYS = {pygame.K_a : 'A',pygame.K_b : 'B',pygame.K_c : 'C',pygame.K_d : 'D',pygame.K_e : 'E',
        pygame.K_f : 'F',pygame.K_g : 'G',pygame.K_h : 'H',pygame.K_i : 'I',pygame.K_j : 'J',
        pygame.K_k : 'K',pygame.K_l : 'L', pygame.K_m : 'M',pygame.K_n : 'N',pygame.K_o : 'O',
        pygame.K_p : 'P',pygame.K_q : 'Q',pygame.K_r : 'R',pygame.K_s : 'S',pygame.K_t : 'T',
        pygame.K_u : 'U',pygame.K_v : 'V',pygame.K_w : 'W',pygame.K_x : 'X',pygame.K_y : 'Y',
        pygame.K_z : 'Z',}

RES = [600,600]
WINDOW = pygame.display.set_mode(RES)
pygame.display.set_caption('Wordle')


FPS = 60

TOTAL_COLUMNS = 5
TOTAL_ROWS = 6
CUSHION = 20
squares = []

TEXT_FONT = pygame.font.Font('Helvetica-Neue-Font/Helvetica Neue Medium Extended/Helvetica Neue Medium Extended.ttf', 55)

class square(pygame.Rect):
    def __init__(self, x ,y, height, width, surface ):
        self.COLOR = CHARCOAL
        self.surface = surface
        self.rect = pygame.Rect( [x,y], [height, width])
        self.text = ''

    def draw_sq(self):
        pygame.draw.rect(self.surface,self.COLOR,self.rect)

    def change_text(self,letter):
        self.text = letter
        self.draw_sq()

    def show_text(self):
        self.surface.blit(TEXT_FONT.render(self.text,True,WHITE), self.rect.topleft)

    def change_color_sq(self, color):

        self.COLOR = color


def set_squares():

    row = 0

    while row < TOTAL_ROWS:
        column = 0
        squares.append([])
        while column < TOTAL_COLUMNS:
            top = ((RES[0] / TOTAL_COLUMNS) * column)+CUSHION
            right = ((RES[1] / TOTAL_ROWS) * row) + CUSHION
            width = (RES[0] / TOTAL_COLUMNS ) - CUSHION
            height = (RES[1] / TOTAL_ROWS) - CUSHION

            squares[row].append(square(top, right, width, height, WINDOW))

            column += 1

        row += 1




def draw_window():
    WINDOW.fill(BLACK)

    for item in squares:
        for squareob in item:

            squareob.draw_sq()
            squareob.change_text(squareob.text)

    pygame.display.update()

def update():
    WINDOW.fill((0,0,0))

    for row in squares:
        for squareob in row:
            squareob.draw_sq()

    for row in squares:
        for squareob in row:
            squareob.show_text()

    pygame.display.flip()



def main():
    clock = pygame.time.Clock()
    run = True
    won = False
    row = 0
    column = 0
    set_squares()
    draw_window()

    while run:
        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and row!=6 and won == False:
                if event.key == pygame.K_RETURN:
                    word = ''
                    #Processing the word
                    for item in squares[row]:
                        word+=item.text
                    output = logic.check(word)

                    #Changing the color of the text
                    if output == 'xxxxx':
                        won = True
                    for i in range(TOTAL_COLUMNS):
                        if output[i] == 'x':

                            squares[row][i].change_color_sq(GREEN)
                        elif output[i] == 'l':

                            squares[row][i].change_color_sq(YELLOW)

                    #Dealing with line change
                    # if row == 5:
                    #     run = False
                    column = 0
                    row +=1

                elif event.key == pygame.K_BACKSPACE:
                    column-=1
                    squares[row][column].change_text('')

                elif column!=5:
                    try :
                        key = KEYS[event.key]
                        squares[row][column].change_text(key)
                        column+=1
                    finally:
                        pass
        update()

if __name__ == '__main__':
    main()






