class Planet:

    def __init__(
            self,
            name,
            radius,
            orbit_radius,
            orbit_speed,
            color
    ):

        self.name = name
        self.radius = radius

        self.orbit_radius = orbit_radius

        self.orbit_speed = orbit_speed

        self.rotation = 0

        self.rotation_speed = 2

        self.angle = 0

        self.color = color

        self.scale_factor = 1.0

    def update(self, simulation_speed, time_direction):
        self.angle += (
            self.orbit_speed *
            simulation_speed *
            time_direction
        )
        self.rotation += (
            self.rotation_speed *
            simulation_speed *
            time_direction
        )
        