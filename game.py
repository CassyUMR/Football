#Importar las librerias que vamos a utilizar
import pygame
import sys
pygame.init()

#Definir las variables que vamos a utilizar, como colores, proporciones, imagenes, etc
#Colores:
AZUL = (0,0,255)
ROJO = (255,0,0)
BLANCO = (255,255,255)

#Proporciones
ALTO = 452
ANCHO = 800

#Imagenes
FONDO = pygame.display.set_mode((ANCHO, ALTO))
ImgFONDO = pygame.image.load("fondo.jpg")
CLOCK = pygame.time.Clock()

#Posiciones:
Coordx1 = 50
Coordy1 = 256
coordx2 = 755
Coordy2 = 214
coordBallX = 400
coordBallY = 300

#Velocidades:
speedx = 0
speedy = 0
speedx1 = 0
speedy1 = 0
speedBallY = 2
speedBallx = 2


#Iniciar el juego
while True:
    #Insertar la imagen del fondo:
    FONDO.blit(ImgFONDO, [0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Teclado:
        if event.type == pygame.KEYDOWN:
            #Jugador 1
            if event.key == pygame.K_LEFT: 
                speedx = -2
            
            if event.key == pygame.K_RIGHT: 
                speedx = 2
            
            if event.key == pygame.K_UP: 
                speedy = -2       
            
            if event.key == pygame.K_DOWN: 
                speedy = 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speedx = 0
            if event.key == pygame.K_RIGHT:
                speedx = 0
            if event.key == pygame.K_UP:
                speedy = 0
            if event.key == pygame.K_DOWN:
                speedy = 0

        #Jugador 2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d: 
                speedx1 = 2
            
            if event.key == pygame.K_a: 
                speedx1 = -2
            
            if event.key == pygame.K_s: 
                speedy1 = 2       
            
            if event.key == pygame.K_w: 
                speedy1 = -2
            
            #PowerUp
            if event.key == pygame.K_m:
                Coordx1 = coordx2
                Coordy1 = Coordy2
                coordx2 = 400
                Coordy2 = 200

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                speedx1 = 0
            if event.key == pygame.K_a:
                speedx1 = 0
            if event.key == pygame.K_w:
                speedy1 = 0
            if event.key == pygame.K_s:
                speedy1 = 0
    
    #Aparecemos la pelota
    ball = pygame.draw.rect(FONDO, BLANCO, (coordBallX, coordBallY, 10, 10))

    #Hacemos que el movimiento sea funcional:
    #Jugador 1:
    Coordx1 += speedx
    Coordy1 += speedy
    #Jugador 2:
    coordx2 += speedx1
    Coordy2 += speedy1
    #Pelota:
    if coordBallY > 440 or coordBallY < 4 :
        speedBallY *= -1

    if coordBallX > 784: 
        speedBallx *= -1
        points = 'Punto del jugador 1'
        print(points)

    if coordBallX < 4:
        speedBallx *= -1
        points2 = 'Punto del jugador 2'
        print(points2)
    
    coordBallY += speedBallY
    coordBallX += speedBallx

    #Aparecemos a el jugador 1 y 2
    p1 = pygame.draw.rect(FONDO, AZUL,(Coordx1, Coordy1, 25, 25))
    p2 = pygame.draw.rect(FONDO, ROJO,(coordx2, Coordy2, 25, 25))
    
    #Fisicas de colisiones en la pelota
    if ball.colliderect(p1) or ball.colliderect(p2):
        speedBallx *= -1
        speedBallY *= -1

    #Fisicas para que nada salga de la pantalla
    #Jugador 1
    if Coordx1 < 0 :
        Coordx1 = 10
    if Coordy1 > 450:
        Coordy1 = 430   
    if Coordy1 < 0:
        Coordy1 = 10
    if Coordx1 > 795:
        Coordx1 = 785

    #Jugador 2
    if coordx2 < 0 :
        coordx2 = 10
    if Coordy2 > 450:
        Coordy2 = 430   
    if Coordy2 < 0:
        Coordy2 = 10
    if coordx2 > 795:
        coordx2 = 785

    #Pelota
    if coordBallX == 795:
        coordBallX = 400

    if coordBallX == 5:
        coordBallX = 400


    #Actualizar la pantalla y limitar los fotogramas por segundo
    pygame.display.update()
    pygame.display.flip()
    CLOCK.tick(60)

    
