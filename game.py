import pygame
pygame.init #Iniciar aplicação

x = 400
y = 300
pos_x = 200
pos_y = 300
velocidade = 25
velocidade_ini = 20
pos_x = 200
pos_y = 300


fundo = pygame.image.load("ruajogo.png")
heroi = pygame.image.load("sonic-removebg-preview.png")
inimigo1 = pygame.image.load("shrek-removebg-preview.png")
inimigo2 = pygame.image.load("blue-removebg-preview.png")
inimigo3 = pygame.image.load("bonero.png")

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
    if comandos[pygame.K_UP]: #seta pra cima
        y -= velocidade #decrementar
    if comandos[pygame.K_DOWN]: #seta pra baixo
        y += velocidade #encrementar
    if comandos[pygame.K_LEFT]: #seta pra esquerda
        x -= velocidade #decrementar
    if comandos[pygame.K_RIGHT]:
        x += velocidade #encrementar
    if(pos_y <= -200):
        pos_y = 900
    pos_y -= velocidade_ini    

    #janela.fill((0,0,0))    

    #pygame.draw.circle(janela, (255, 255, 255), (x,y), 10)
                       #local,     cor,     local, tamanho
    janela.blit(fundo,(0,0))
    janela.blit(heroi,(x,y))
    janela.blit(inimigo1,(pos_x - 50,pos_y - 100))
    janela.blit(inimigo2,(pos_x + 170,pos_y - 290))
    janela.blit(inimigo3,(pos_x + 370,pos_y - 195))

    pygame.display.update()










pygame.QUIT() #encerrar o jogo

