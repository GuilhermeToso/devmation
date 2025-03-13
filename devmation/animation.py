from manim import *
from components.database import DatabaseSVG, Database

class DatabaseAnimation(Scene):

    def construct(self):

        database = DatabaseSVG()

        self.add(database)

        self.wait(1)


class DBAnimation(ThreeDScene):

    def construct(self):

        database = Database()

        self.add(database)
        self.set_camera_orientation(
            phi=75 * DEGREES,
            theta=30 * DEGREES,
        )
        
