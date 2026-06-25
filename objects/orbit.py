from OpenGL.GL import *
import math

def draw_orbit(radius):

    glBegin(GL_LINE_LOOP)

    for i in range(100):

        angle = 2 * math.pi * i / 100

        x = radius * math.cos(angle)
        z = radius * math.sin(angle)

        glVertex3f(x, 0, z)

    glEnd()