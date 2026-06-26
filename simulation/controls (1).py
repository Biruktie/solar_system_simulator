import simulation.state as state

def keyboard(key, x, y):
    if key == b'+':
        state.simulation_speed += 0.2
        print(
            "Speed:",
            round(state.simulation_speed, 1)
        )
    elif key == b'-':
        state.simulation_speed = max(
            0.2,
            state.simulation_speed - 0.2
        )
        print(
            "Speed:",
            round(state.simulation_speed, 1)
        )
    elif key == b'r':
        state.time_direction *= -1
        print("Reverse Time")
    elif key == b'p':
        state.paused = not state.paused
        if state.paused:
            print("Paused")
        else:
            print("Resumed")

    elif key == b'1':
        state.selected_planet_index = 0

    elif key == b'2':
        state.selected_planet_index = 1

    elif key == b'3':
        state.selected_planet_index = 2

    elif key == b'4':
        state.selected_planet_index = 3

    elif key == b'5':
        state.selected_planet_index = 4

    elif key == b'6':
        state.selected_planet_index = 5
    elif key == b'7':
        state.selected_planet_index = 6
    elif key == b'8':
        state.selected_planet_index = 7
    elif key == b']':

        planet = state.planets[
            state.selected_planet_index
        ]

        planet.scale_factor += 0.1

        print(
            planet.name,
            "scaled to",
            round(planet.scale_factor, 1)
        )
    elif key == b'[':

        planet = state.planets[
            state.selected_planet_index
        ]

        planet.scale_factor = max(
            0.2,
            planet.scale_factor - 0.1
        )

        print(
            planet.name,
            "scaled to",
            round(planet.scale_factor, 1)
        )