from OpenGL.GL import *
from OpenGL.GLU import *


def reshape(width, height):

    if height == 0:
        height = 1

    glViewport(
        0,
        0,
        width,
        height
    )

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    gluPerspective(
        45,
        width / height,
        0.1,
        100
    )

    glMatrixMode(GL_MODELVIEW)