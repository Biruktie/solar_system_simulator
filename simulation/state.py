from objects.planet import Planet

mercury = Planet(
    "Mercury",
    0.03,
    0.2,
    3,
    (0.7, 0.7, 0.7)
)

venus = Planet(
    "Venus",
    0.04,
    0.35,
    2,
    (1.0, 0.6, 0.0)
)

earth = Planet(
    "Earth",
    0.05,
    0.5,
    1,
    (0.0, 0.0, 1.0)
)

mars = Planet(
    "Mars",
    0.04,
    0.7,
    0.8,
    (1.0, 0.3, 0.2)
)

jupiter = Planet(
    "Jupiter",
    0.09,
    1.0,
    0.4,
    (0.8, 0.6, 0.4)
)

saturn = Planet(
    "Saturn",
    0.08,
    1.3,
    0.3,
    (0.9, 0.8, 0.5)
)

uranus = Planet(
    "Uranus",
    0.07,
    1.6,
    0.25,
    (0.6, 0.9, 1.0)
)

neptune = Planet(
    "Neptune",
    0.07,
    1.9,
    0.2,
    (0.3, 0.3, 1.0)
)

planets = [
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]

simulation_speed = 1.0
time_direction = 1
paused = False
selected_planet_index = 0
