import pygame
import time
from random import randint

pygame.init()

clock = pygame.time.Clock()


# variable
run2= True
lost = True
height = [250, 250]
height2 = [120, 120]
count = [0, 0]
track2 = []
track = []
pos = 400
xaxis = 0

counting=[0,0]

sgen = [1000,1400]
hei=[420,480]

agen=[800,1200,1500]
ahei=[294,354,415]
daxis=0
acounting=[0,0,0]
xx=0








# Screen

screen = pygame.display.set_mode((800, 560))
pygame.display.set_caption("Dooms Day")


#char
dav = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png'),
           pygame.image.load('4.png'), pygame.image.load('5.png'), pygame.image.load('6.png'),
           pygame.image.load('7.png'), pygame.image.load('8.png'), pygame.image.load('9.png'),
           pygame.image.load('10.png')]


s1 = pygame.image.load('s1.png')

devil = [pygame.image.load('1a.png'), pygame.image.load('2a.png'), pygame.image.load('3a.png'),
             pygame.image.load('4a.png'), pygame.image.load('5a.png'), pygame.image.load('6a.png'),
             pygame.image.load('7a.png'), pygame.image.load('8a.png'), pygame.image.load('9a.png'),
             pygame.image.load('10a.png'), pygame.image.load('11a.png'), pygame.image.load('12a.png'),
             pygame.image.load('13a.png'), pygame.image.load('14a.png'), pygame.image.load('15a.png')]


# music

music = pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

# mountains
while count[0] != 804:

    if (height[0] < height[1] + 8) and (height[0] > height[1] - 8):
        height[1] = height[0]

        track.append(height[0])

        count[0] += 3

    height[0] = randint(180, 280)
while count[1] != 804:
    if (height2[0] < height2[1] + 8) and (height2[0] > height2[1] - 8):
        height2[1] = height2[0]

        track2.append(height2[0])
        count[1] += 2

    height2[0] = randint(60, 240)

def end():
    global lost
    lost = False
    time.sleep(1)



def stone():
    global counting
    global sgen
    global hei
    global s1
    global run2
    loop = [0, 1]

    for x in loop:

        screen.blit(s1, (sgen[x] - (counting[x] * 5), hei[x]))

        counting[x] += 1
        if counting[x] == 450:
            sgen[x] = randint(1500, 2000)

            counting[x] = 0


def pointer():
    global xx
    global run2
    yy=0

    yy, xx = pygame.mouse.get_pos()
    if run2:

        k1, k2 = pygame.mouse.get_pos()

        if k2 > 508 and k2 < 530 and k1 > 343 and k1 < 440:
            run2 = False




def davpos():
    global xx
    global pos
    global dav
    global acounting
    global ahei
    global agen
    global daxis
    global devil
    global run


    if xx>=380 and xx<440:

        pos=340

    if xx>=440 and xx <500:
        pos=400
    if xx >=500 and xx<560:
        pos=460





    daxis += 1
    if daxis > 14:
        daxis = 0
    aloop=[0,1,2]

    check=[0,1,2]

    if pos ==340:



        screen.blit(devil[daxis], (agen[0] - acounting[0] * 6, ahei[0]))


        screen.blit(dav[xaxis], (120, pos))


        screen.blit(devil[daxis], (agen[1] - acounting[1] * 6, ahei[1]))


        screen.blit(devil[daxis], (agen[2] - acounting[2] * 6, ahei[2]))

        if (agen[0] - acounting[0] * 6) > 163 and (agen[0] - acounting[0] * 6) < 170:
            end()

    if pos == 400:


        screen.blit(devil[daxis], (agen[0] - acounting[0] * 6, ahei[0]))

        screen.blit(devil[daxis], (agen[1] - acounting[1] * 6, ahei[1]))


        screen.blit(dav[xaxis], (120, pos))

        screen.blit(devil[daxis], (agen[2] - acounting[2] * 6, ahei[2]))


        if (agen[1] - acounting[1] * 6) > 163 and (agen[1] - acounting[1] * 6) < 170:
            end()

    if pos == 460:

        screen.blit(devil[daxis], (agen[0] - acounting[0] * 6, ahei[0]))


        screen.blit(devil[daxis], (agen[1] - acounting[1] * 6, ahei[1]))

        screen.blit(devil[daxis], (agen[2] - acounting[2] * 6, ahei[2]))

        screen.blit(dav[xaxis], (120, pos))


        if (agen[2] - acounting[2] * 6)>163 and (agen[2] - acounting[2] * 6)< 170:
            end()





    for ax in aloop:

        acounting[ax] += 1
        if acounting[ax] == 350:
            agen[ax] = randint(800, 1500)
            acounting[ax] = 0



# mountains move
def motion():
    global track
    global track2
    global xaxis
    global run2
    global lost

    # davis
    xaxis += 1

    if xaxis > 9:
        xaxis = 0

    screen.fill((255, 69, 0))
    surface = pygame.image.load('surface.jpg')
    screen.blit(surface, (0, 380))



    if run2== False:
        pygame.draw.rect(screen, (132, 115, 90), (0, 380, 800, 180))
        pygame.draw.rect(screen, (255, 255, 255), (0, 440, 800, 1))
        pygame.draw.rect(screen, (255, 255, 255), (0, 500, 800, 1))


    pygame.draw.circle(screen, (178, 34, 34), (80, 80), 80, 0)
    pygame.draw.circle(screen, (178, 34, 34), (200, 100), 30, 0)



    # mountain movement

    track.pop(0)
    track2.pop(0)

    countt = [0, 0]
    trackcount = [0, 0]

    simple = True
    simple2 = True

    for x in track:
        pygame.draw.rect(screen, (72, 61, 139), (countt[0], 380, 1, -track[trackcount[0]]))
        countt[0] += 3
        trackcount[0] += 1

    for y in track2:
        pygame.draw.rect(screen, (25, 25, 112), (countt[1], 380, 1, -track2[trackcount[1]]))
        countt[1] += 2
        trackcount[1] += 1

    while simple:
        heighttemp = randint(180, 280)
        if (heighttemp < track[-1] + 8) and (heighttemp > track[-1] - 8):
            pygame.draw.rect(screen, (72, 61, 139), (801, 380, 1, -heighttemp))
            track.append(heighttemp)
            simple = False
    while simple2:

        heighttemp2 = randint(60, 240)
        if (heighttemp2 < track2[-1] + 8) and (heighttemp2 > track2[-1] - 8):
            pygame.draw.rect(screen, (25, 25, 112), (801, 380, 1, -heighttemp2))
            track2.append(heighttemp2)

            simple2 = False



    # position of davis
    if run2== False:
        if lost== True:
            stone()
            davpos()
        else:
            end = pygame.image.load('end.jpg')
            screen.blit(end, (0, 380))


# mainloop


run = True



while run:
    pygame.display.update()
    clock.tick(33)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pointer()


        if event.type == pygame.QUIT:
            run = False
    motion()

pygame.quit()
