from OpenGL.GLU import *


def setup_camera():

    gluLookAt(
        0,
        2.5,
        5,
        0,
        0,
        0,
        0,
        1,
        0
    )
