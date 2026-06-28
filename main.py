from OpenGL.GL import *
from OpenGL.GLUT import *

from simulation.updater import update
from simulation.updater import get_moon_angle
from simulation.state import planets
from simulation.controls import keyboard

from objects.orbit import draw_orbit
from objects.window import reshape

from graphics.renderer import draw_planet, draw_earth_system, draw_sun
from graphics.background import draw_stars

from graphics.camera import setup_camera
from graphics.lighting import setup_lighting
from graphics.hud import draw_hud


def display():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    light_position = [0, 0, 0, 1]

    glLightfv(
        GL_LIGHT0,
        GL_POSITION,
        light_position
    )

    setup_camera()

    draw_stars()

    draw_sun()

    for planet in planets:
        draw_orbit(planet.orbit_radius)
        if planet.name != "Earth":
            draw_planet(planet)

    draw_earth_system(get_moon_angle())

    draw_hud()

    glutSwapBuffers()


def init():

    glClearColor(0, 0, 0, 1)

    glEnable(GL_DEPTH_TEST)

    setup_lighting()


glutInit()

glutInitDisplayMode(
    GLUT_DOUBLE |
    GLUT_RGB |
    GLUT_DEPTH
)

glutInitWindowSize(
    800,
    600
)

glutCreateWindow(
    b"3D Solar System"
)

init()

glutDisplayFunc(
    display
)

glutReshapeFunc(
    reshape
)

glutKeyboardFunc(keyboard)

glutTimerFunc(
    16,
    update,
    0
)

glutMainLoop()
