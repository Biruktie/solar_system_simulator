from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import simulation.state as state


def draw_text(x, y, text):

    glMatrixMode(GL_PROJECTION)

    glPushMatrix()
    glLoadIdentity()

    gluOrtho2D(
        0,
        800,
        0,
        600
    )

    glMatrixMode(GL_MODELVIEW)

    glPushMatrix()
    glLoadIdentity()

    glDisable(GL_LIGHTING)

    glColor3f(
        1,
        1,
        1
    )

    glRasterPos2f(
        x,
        y
    )

    for char in text:

        glutBitmapCharacter(
            GLUT_BITMAP_9_BY_15,
            ord(char)
        )

    glEnable(GL_LIGHTING)

    glPopMatrix()

    glMatrixMode(GL_PROJECTION)

    glPopMatrix()

    glMatrixMode(GL_MODELVIEW)


def draw_hud():

    draw_text(
        10,
        580,
        "+/- : Speed Control"
    )

    draw_text(
        10,
        560,
        "P : Pause/Resume"
    )

    draw_text(
        10,
        540,
        "R : Reverse Time"
    )

    draw_text(
        10,
        520,
        "1-8 : Select Planet"
    )

    draw_text(
        10,
        500,
        "[ ] : Scale Planet"
    )

    draw_text(
        10,
        470,
        f"Speed: {state.simulation_speed:.1f}"
    )

    selected = state.planets[
        state.selected_planet_index
    ]

    draw_text(
        10,
        450,
        f"Selected: {selected.name}"
    )

    status = (
        "Paused"
        if state.paused
        else "Running"
    )

    draw_text(
        10,
        430,
        f"Status: {status}"
    )
