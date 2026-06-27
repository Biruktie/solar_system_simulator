from OpenGL.GL import *
from OpenGL.GLUT import *
import math
from simulation.state import earth
from objects.orbit import draw_orbit


def draw_planet(planet):

    glPushMatrix()

    glRotatef(
        planet.angle,
        0,
        1,
        0
    )

    glTranslatef(
        planet.orbit_radius,
        0,
        0
    )

    glRotatef(
        planet.rotation,
        0,
        1,
        0
    )

    glScalef(
        planet.scale_factor,
        planet.scale_factor,
        planet.scale_factor
    )

    glColor3f(
        planet.color[0],
        planet.color[1],
        planet.color[2]
    )

    glutSolidSphere(
        planet.radius,
        20,
        20
    )

    if planet.name == "Saturn":
        draw_saturn_ring()

    glPopMatrix()


def draw_saturn_ring():

    glBegin(GL_LINE_LOOP)

    for i in range(100):
        angle = math.radians(i * 3.6)

        x = 0.12 * math.cos(angle)
        z = 0.12 * math.sin(angle)

        glVertex3f(x, 0, z)

    glEnd()


def draw_earth_system(moon_angle):
    glPushMatrix()

    # Earth revolution
    glRotatef(
        earth.angle,
        0,
        1,
        0
    )

    glTranslatef(
        earth.orbit_radius,
        0,
        0
    )

    glRotatef(
        earth.rotation,
        0,
        1,
        0
    )

    glScalef(
        earth.scale_factor,
        earth.scale_factor,
        earth.scale_factor
    )

    glColor3f(*earth.color)

    glutSolidSphere(
        earth.radius,
        20,
        20
    )

    draw_orbit(0.1)

    glPushMatrix()

    glRotatef(
        moon_angle,
        0,
        1,
        0
    )

    glTranslatef(
        0.1,
        0,
        0
    )

    glColor3f(
        0.8,
        0.8,
        0.8
    )

    glutSolidSphere(
        0.02,
        15,
        15
    )

    glPopMatrix()

    glPopMatrix()


def draw_sun():

    glDisable(GL_LIGHTING)

    glColor3f(
        1.0,
        1.0,
        0.0
    )

    glutSolidSphere(
        0.1,
        30,
        30
    )

    glEnable(GL_LIGHTING)