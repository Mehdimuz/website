from manim import *

class RotatingGlobe(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        globe = Sphere(
            radius=2,
            resolution=(30, 30),
            checkerboard_colors=None,   # 🔑 turn OFF checkerboard
            fill_color=BLUE_E,
            fill_opacity=1.0,
            stroke_width=0,
        )

        self.add(globe)
        self.play(Rotate(globe, angle=2 * PI, axis=UP), run_time=6, rate_func=linear)
        self.wait()
