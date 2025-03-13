from manim import *

class DatabaseSVG(SVGMobject):

    def __init__(self):

        super().__init__(
            file_name="database.svg",
            stroke_width=0,
            fill_color=WHITE,
            stroke_color=WHITE,
            fill_opacity=1,
            stroke_opacity=1,
        )
        
        self.scale(0.5)

        self.set_color(BLUE)

        self.set_fill(opacity=1)

        self.set_stroke(opacity=1)


class Database(VGroup):

    def __init__(self):

        super().__init__()
        
        cylinder_1 = Cylinder(
            radius=1,
            height=0.5,
            fill_color=BLUE_D,
            checkerboard_colors=False,
            fill_opacity=1,
            stroke_color=BLUE_A,
            stroke_width=0.1,
            stroke_opacity=1,
            resolution=(10,10),
        )
        
        cylinder_2 = Cylinder(
            radius=1,
            height=0.5,
            fill_color=BLUE_D,
            checkerboard_colors=False,
            fill_opacity=1,
            stroke_color=BLUE_A,
            stroke_width=0.1,
            stroke_opacity=1,
            resolution=(10,10),
        )

        cylinder_3 = Cylinder(
            radius=1,
            height=0.5,
            fill_color=BLUE_D,
            checkerboard_colors=False,
            fill_opacity=1,
            stroke_color=BLUE_A,
            stroke_width=0.1,
            stroke_opacity=1,
            resolution=(10,10),
        )
        
        # Position cylinders
        cylinder_2.move_to(cylinder_1.get_center() - OUT * 0.7)
        cylinder_3.move_to(cylinder_2.get_center() - OUT * 0.7)

        # Create tops for each cylinder
        cylinder_1_top = Circle(
            radius=1,
            color=BLUE_D,
            fill_color=BLUE_D,
            fill_opacity=0.8,
            shade_in_3d=True,
            stroke_width=0,
        )
        cylinder_1_top.shift(cylinder_1.u_range[1] * IN)

        cylinder_2_top = Circle(
            radius=1,
            color=BLUE_D,
            fill_color=BLUE_D,
            fill_opacity=0.8,
            shade_in_3d=True,
            stroke_width=0,
        )
        cylinder_2_top.shift(cylinder_2.u_range[1] * IN)

        cylinder_3_top = Circle(
            radius=1,
            color=BLUE_D,
            fill_color=BLUE_D,
            fill_opacity=0.8,
            shade_in_3d=True,
            stroke_width=0,
        )
        cylinder_3_top.shift(cylinder_3.u_range[1] * IN)

        # Add all elements to the group
        self.add(cylinder_1, cylinder_2, cylinder_3, cylinder_1_top, cylinder_2_top, cylinder_3_top)

