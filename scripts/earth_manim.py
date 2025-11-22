from manimlib import *
from pathlib import Path
import numpy as np

class TexturedEarth(ThreeDScene):
    def construct(self):

        # ---------- Load Textures ----------
        img_dir = Path(__file__).parent / "assets" / "raster_images"
        jpgs = sorted(img_dir.glob("*.jpg"))
        if len(jpgs) < 2:
            raise Exception("Need two .jpg textures in assets/raster_images")

        day_texture = str(jpgs[0])
        night_texture = str(jpgs[1])

        # ---------- Earth Sphere ----------
        sphere = Sphere(radius=2, resolution=(30, 30))
        earth = TexturedSurface(sphere, day_texture, night_texture)
        self.add(earth)

        # If Earth looks flipped, you can tweak these:
        # earth.rotate(PI, axis=UP)
        # earth.rotate(PI, axis=RIGHT)

        # ---------- 3D Axes (optional) ----------
        axes = ThreeDAxes()
        axes.set_stroke(width=1.5, color=GREY_D)
        self.add(axes)

        # ---------- CAMERA: INITIAL VIEW ----------
        # Mid-northern, looking at Europe / Africa-ish
        self.camera.theta = -20 * DEGREES   # yaw (around vertical)
        self.camera.phi   = 60 * DEGREES    # pitch (0 = top-down, 90 = side)
        self.camera.distance = 10
        self.camera.frame_center = ORIGIN

        # ---------- EARTH: STATIONARY ----------
        # No updater on Earth – it does NOT spin.
        # (Just comment-out or omit any spin updater.)

        # ---------- CAMERA ORBIT AROUND VERTICAL ----------
        # North axis = UP, so "north star" direction stays up on screen.
        driver = Dot(ORIGIN, fill_opacity=0, stroke_opacity=0)
        self.add(driver)

        def orbit(mob, dt):
            # Camera circles around Earth along the equator, keeping latitude fixed.
            self.camera.frame.rotate(0.10 * dt, axis=UP)

        driver.add_updater(orbit)

        # ---------- Run Animation ----------
        self.wait(12)
