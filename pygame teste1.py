#esse foi meu primeiro teste no pygame, como base, utilizei o jogo que foi o ''marco'' inicial no mundo dos games o famoso jogo de Arcade e de Atari o 'Pong'
#this was my first test on pygame, as a base, i utilize a game which was a mark to the game world, the game called 'Pong'

import pygame 
def menu():
    pygame.init()
    leave = False
    display = pygame.display.set_mode([1280,720])
    imagem_menu = pygame.image.load ('menu.jpeg')
    display.blit(imagem_menu, (50,10))
    while leave!= True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave = True    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  
                    main()
                    
            pygame.display.update()
pygame.init()


display = pygame.display.set_mode([1280, 720])                              #variaveis, aqui tem variaveis da tela, do campo, da movimentacao dos players, da bola e do placar. 
pygame.display.set_caption('Pong')
field = pygame.image.load('') #essas linhas tao em branco, pq aqui e a localizacao da pasta/it has just the '' because in this line, u put the folder with the images
player1 = pygame.image.load('') 
player1_y = 310
player1_moveup = False
player1_movedown = False
player2 = pygame.image.load('')
player2_y = 310
player2_moveup = False
player2_movedown = False
ball = pygame.image.load('')
ball_x = 617
ball_y = 337
ball_dir = -10
ball_dir_y = 10
score1 = 8
score2 = 0
score1_img = pygame.image.load('')
score2_img = pygame.image.load('')
win = pygame.image.load('') 

def move_player1():                    #def da movimentacao do player1
    global  player1_y
    if player1_moveup:
        player1_y -= 5
    else:
        player1_y += 0
    if player1_movedown:
        player1_y += 5
    else:
        player1_y += 0
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2():                         #def da movimentacao do player2
    global  player2_y
    if player2_moveup:
        player2_y -= 5
    else:
        player2_y += 0
    if player2_movedown:
        player2_y += 5
    else:
        player2_y += 0
    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575
    

def move_ball():                              #def da move ball
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y
    global score1
    global score2
    global score1_img
    global score2_img
    
    ball_x += ball_dir
    ball_y += ball_dir_y
    
    if ball_x < 120:
        if player1_y < ball_y + 23:
            if player1_y + 146 > ball_y:
                ball_dir *= -1
    if ball_x > 1120:
         if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1
    if ball_y > 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1
    if ball_x <- 50:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load('score/' + str(score2) + '.png') #aqui sao linhas de codigos para carregar o placar e adicionar mais um a cada gol feito
    elif ball_x > 1320:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load('score/' + str(score1) + '.png') #aqui sao linhas de codigos para carregar o placar e adicionar mais um a cada gol feito


def draw():                                                  #def dos desenhos da tela
    if score1 or score2 < 9:
        display.blit(field, (0, 0))
        display.blit(player1, (50, player1_y))
        display.blit(player2, (1150, player2_y))
        display.blit(ball, (ball_x, ball_y))
        display.blit(score1_img, (500, 50))
        display.blit(score2_img, (710, 50)) 
        move_ball()
        move_player1()
        move_player2()
    else:
        display.blit(win, (300, 330))


loop = True
while loop:                                                   #While - Manter o jogo aberto/ to keep the game opened
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_moveup = True
            if event.key == pygame.K_s:
                player1_movedown = True
            if event.key == pygame.K_i:
                player2_moveup = True
            if event.key == pygame.K_k:
                player2_movedown = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1_moveup = False
            if event.key == pygame.K_s:
                player1_movedown = False
            if event.key == pygame.K_i:
                player2_moveup = False
            if event.key == pygame.K_k:
                player2_movedown = False
    draw()
    pygame.display.update()
    
    def main():
        main()

pygame.quit()
quit()
