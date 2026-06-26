from OpenGL.GL import *


def setup_lighting():

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)

    glColorMaterial(
        GL_FRONT_AND_BACK,
        GL_AMBIENT_AND_DIFFUSE
    )

    light_position = [0, 0, 0, 1]
    ambient = [0.2, 0.2, 0.2, 1]
    diffuse = [1, 1, 1, 1]

    glLightfv(
        GL_LIGHT0,
        GL_POSITION,
        light_position
    )

    glLightfv(
        GL_LIGHT0,
        GL_AMBIENT,
        ambient
    )

    glLightfv(
        GL_LIGHT0,
        GL_DIFFUSE,
        diffuse
    )