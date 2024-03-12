# Импорт библиотек
import pygame
import OpenGL
import random
from pygame import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


# Константы
global quadricItem
quadricItem = gluNewQuadric()
global alfa
alfa = 0.0
n = 1
sp_size = [random.uniform(0.4, 0.75) for _ in range(100)]
sp_color = [(random.randint(210, 255), random.randint(155, 220), random.randint(60, 130)) for _ in range(100)]


def draw(n, r, k, sp, sp_color):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glTranslated(0.75, 0, -0.75)
    glColor3d(0.97, 0.58, 0.24)
    gluSphere(quadricItem, 2, 50, 50)

    glColor3d(216/255, 174/255, 109/255)
    glRotatef(90,1,1,0)
    gluDisk(quadricItem, 3, 5, 100, 50)

    glColor3d(255/255, 187/255, 87/255)
    glTranslated(-0.5,6,0)

    
    for i in range(n):
        glColor3d(sp_color[i][0]/255, sp_color[i][1]/255, sp_color[i][2]/255)
        try:
            gluSphere(quadricItem, sp[i], 25, 25)
            glTranslated(-0.5, 2, 0)
        except:
            gluSphere(quadricItem, 0.7, 25, 25)
            glTranslated(-0.5, 2, 0)


    glPopMatrix()    

    # Управление
    if r:
        glRotatef(1, 0, 1, 0)
    if k == 'L':
        glRotatef(-1, 0, 1, 0)
    if k == 'R':
        glRotatef(1, 0, 1, 0)
    if k == 'U':
        glRotatef(-1, 1, 0, 1)
    if k == 'D':
        glRotatef(1, 1, 0, 1)



def main():
    # Позиции освещения
    pos = (3, 3, 3, 1)
    pos1 = (3, 3, 3, 1)
    direc = (-1, -1,-1)

    # Окно
    pygame.init()
    pygame.mixer.music.load('music1.mp3')
    display = (1200, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL | GL_RGB | GL_DEPTH)
    gluPerspective(45, display[0]/display[1], 2, 50.0)

    glTranslatef(0.0, 0.0, -20)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_COLOR_MATERIAL)
    # Цикл отрисовки
    n = 1
    r = True
    k = 'T'
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Обработка кнопок
                if event.key == pygame.K_KP_PLUS:
                    n += 1
                elif event.key == pygame.K_KP_MINUS:
                    if n > 1:
                        n -= 1
                elif event.key == pygame.K_r:
                    if r:
                        r = False
                    else:
                        r = True
                elif event.key == pygame.K_RIGHT:
                    k = 'R'
                elif event.key == pygame.K_LEFT:
                    k = 'L'
                elif event.key == pygame.K_UP:
                    k = 'U'
                elif event.key == pygame.K_DOWN:
                    k = 'D'
                elif event.key == pygame.K_o:
                    pygame.mixer.music.play()
                elif event.key == pygame.K_p:
                    pygame.mixer.music.pause()
                elif event.key == pygame.K_PAGEUP:
                    glEnable(GL_LIGHT0)
                elif event.key == pygame.K_PAGEDOWN:
                    glDisable(GL_LIGHT0)
                    glDisable(GL_LIGHTING)
        glEnable(GL_LIGHTING)
        glLightfv(GL_LIGHT2,GL_POSITION,pos1)
        glLightfv(GL_LIGHT2,GL_SPOT_DIRECTION,direc)
        glLightfv(GL_LIGHT0,GL_POSITION,pos)
        glLightfv(GL_LIGHT0,GL_SPOT_DIRECTION,direc)
        # Отрисовка
        draw(n, r, k, sp_size, sp_color)
        pygame.display.flip()
        pygame.time.wait(10)
        
        

if __name__ == '__main__':
    main()