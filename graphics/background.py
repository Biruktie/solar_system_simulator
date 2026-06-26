from OpenGL.GL import *
import random

stars = []

for _ in range(300):

    x = random.uniform(-20, 20)
    y = random.uniform(-20, 20)
    z = random.uniform(-20, 20)

    stars.append((x, y, z))


def draw_stars():

    glDisable(GL_LIGHTING)

    glColor3f(1, 1, 1)

    glPointSize(2)

    glBegin(GL_POINTS)

    for x, y, z in stars:
        glVertex3f(x, y, z)

    glEnd()

    glEnable(GL_LIGHTING)