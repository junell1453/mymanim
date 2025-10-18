from manim import *

class MovingCircle(Scene):
    def construct(self):
        circle = Circle(color=BLUE).shift(LEFT * 2)
        text = Text("你好世界").scale(0.6).to_corner(UR)

        # 不使用 add_fixed_in_frame_mobjects（v0.19.0 兼容性差）
        self.add(text)

        self.play(Create(circle))
        self.play(circle.animate.shift(RIGHT * 4), run_time=2)
        self.wait()
