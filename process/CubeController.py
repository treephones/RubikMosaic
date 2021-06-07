import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from process.CubeConstants import *
from process.ImageParser import Colors

class CubeController():
    def run(self):
        self.freeCubeWindow()

    def renderRubiksCube(self):
        glBegin(GL_QUADS)
        for surface in SURFACES:
            for i,vertex in enumerate(surface):
                glColor3fv(Colors.values()[int((i/8)*6)].rgb)
                glVertex3fv(VERTICES[vertex])
        glEnd()
        glBegin(GL_LINES)
        for edge in EDGES:
            for vertex in edge:
                glVertex3fv(VERTICES[vertex])
        glEnd()

    def freeCubeWindow(self):
        pygame.init()
        window = (800, 600)
        pygame.display.set_mode(window, DOUBLEBUF|OPENGL)
        pygame.display.set_caption("Rubiks Cube")

        gluPerspective(45, window[0]/window[1], 0.1, 50)
        glTranslatef(0.0, 0.0, -5)

        while True:
            mouse_pressed = pygame.mouse.get_pressed()[0] == 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        glTranslatef(-0.2,0,0)
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        glTranslatef(0.2,0,0)
                    if event.key in (pygame.K_UP, pygame.K_w):
                        glTranslatef(0,0.2,0)
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        glTranslatef(0,-0.2,0)
                if event.type == pygame.MOUSEMOTION:
                    if mouse_pressed:
                        glRotatef(event.rel[1], 1, 0, 0)
                        glRotatef(event.rel[0], 0, 1, 0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            self.renderRubiksCube()
            pygame.display.flip()
            pygame.time.wait(10)