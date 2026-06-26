from OpenGL.GLUT import *
import simulation.state as state
from simulation.state import planets

moon_angle = 0


def update(value):
    global moon_angle

    if not state.paused:
        for planet in planets:
            planet.update(
                state.simulation_speed,
                state.time_direction
            )

        moon_angle += (
            4 *
            state.simulation_speed *
            state.time_direction
        )

    glutPostRedisplay()

    glutTimerFunc(16, update, 0)


def get_moon_angle():
    return moon_angle
