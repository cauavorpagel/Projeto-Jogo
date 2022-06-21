from random import randint
import pygame
pygame.font.init()
pygame.init #Iniciar aplicação
 
x = 400
y = 300
pos_x = 200
pos_y = 800
pos_y_a = 1050
pos_y_b = 800
pos_y_c = 1200
velocidade = 25
velocidade_ini = 12
pos_x = 200
pos_y = 300
timer = 0
seg = 0

fundo = pygame.image.load("ruajogo.png")
heroi = pygame.image.load("sonic-removebg-preview.png")
inimigo1 = pygame.image.load("shrek-removebg-preview.png")
inimigo2 = pygame.image.load("blue-removebg-preview.png")
inimigo3 = pygame.image.load("bonero.png")

#timer
font = pygame.font.SysFont('Arial', 30) #objeto fonte
texto = font.render("Tempo: ", True,(255,255,255)) #cor


#Criando janela
janela = pygame.display.set_mode((800,600)) #Tamanho da tela
pygame.display.set_caption("Jogo em Pyhton") #Nome da tela

janela_aberta = True
while janela_aberta: #enquanto janela aberta
    pygame.time.delay(50)
    for event in pygame.event.get(): #aguarda um evento get
        if event.type == pygame.QUIT: #se o evento get for QUIT
            janela_aberta = False #janela é fechada

    #comando de movimentação
    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]: #seta pra cima
        #y -= velocidade #decrementar
    #if comandos[pygame.K_DOWN]: #seta pra baixo
        #y += velocidade #encrementar
    if comandos[pygame.K_LEFT] and x >=120: #seta pra esquerda
        x -= velocidade #decrementar
    if comandos[pygame.K_RIGHT] and x <=599:
        x += velocidade #encrementar
    if(pos_y <= -200):
        pos_y = 900
    pos_y -= velocidade_ini   


    if (x + 93 > pos_x and y + 80 > pos_y): #colisão com a direita
        y = 1900

    if (pos_y_a <= -50): 
        pos_y_a = randint(800,1100)
    if (pos_y_b <= -50):
        pos_y_b = randint(800,950)
    if (pos_y_c <= -50):
        pos_y_c = randint(800,1250)
        
    pos_y -= velocidade_ini
    pos_y_a -= velocidade_ini +19 
    pos_y_b -= velocidade_ini +12
    pos_y_c -= velocidade_ini +10

    if (timer < 20):
        timer += 1
    else:
        seg += 1
        texto = font.render("Tempo: "+str(seg), True,(255,255,255)) #cor    
        timer = 0



    #janela.fill((0,0,0))    

    #pygame.draw.circle(janela, (255, 255, 255), (x,y), 10)
                       #local,     cor,     local, tamanho
    janela.blit(fundo,(0,0))
    janela.blit(heroi,(x,120))
    janela.blit(inimigo1,(pos_x - 50,pos_y_a))
    janela.blit(inimigo2,(pos_x + 170,pos_y_b))
    janela.blit(inimigo3,(pos_x + 370,pos_y_c))
    janela.blit(texto,(13,20))

    pygame.display.update()










pygame.QUIT() #encerrar o jogo

