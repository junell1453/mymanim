# -*- coding: utf-8 -*-
from manim import *
import numpy as np

class DerivativeParabola(Scene):
    """
    演示二次函数 f(x)=x^2 的切线与导数变化
    """

    def construct(self):
        # 坐标轴
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 9, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True, "stroke_width": 2},
            x_axis_config={
                "numbers_to_include": np.arange(-4, 5, 1),
                "font_size": 28,
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 10, 1),
                "font_size": 28,
            },
        ).to_edge(DOWN * 0.3)

        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")
        axes.add(x_label, y_label)

        # 原函数 y = x^2
        parabola = axes.plot(lambda x: x ** 2, color=BLUE)
        parabola_label = axes.get_graph_label(parabola, label="y = x^2", x_val=2, direction=LEFT)

        # 导函数 y = 2x
        derivative_graph = axes.plot(lambda x: 2 * x, color=GREEN)
        deriv_label = axes.get_graph_label(derivative_graph, label="y = 2x", x_val=2, direction=UR)

        # 可调变量
        x_tracker = ValueTracker(-3.0)
        h_tracker = ValueTracker(3)

        # 移动点
        moving_point = always_redraw(
            lambda: Dot(
                axes.c2p(x_tracker.get_value(), x_tracker.get_value() ** 2),
                color=YELLOW,
                radius=0.06,
            )
        )

        # 切线：手动计算
        def get_tangent_line():
            x0 = x_tracker.get_value()
            slope = 2 * x0  # f'(x) = 2x
            y0 = x0 ** 2
            # y = slope * (x - x0) + y0
            line_func = lambda x: slope * (x - x0) + y0
            # 取较长的区间
            return axes.plot(line_func, x_range=[x0 - 2, x0 + 2], color=YELLOW)

        tangent_line = always_redraw(get_tangent_line)
        # tangent_line = get_tangent_line()

        # 割线
        def get_secant_line():
            x = x_tracker.get_value()
            h = h_tracker.get_value()
            x1 = x + h
            y0 = x ** 2
            y1 = x1 ** 2
            return Line(
                axes.c2p(x, y0),
                axes.c2p(x1, y1),
                color=RED,
                stroke_width=3
            )

        secant_line = always_redraw(get_secant_line)

        # 计算割线斜率
        def secant_slope_val():
            x = x_tracker.get_value()
            h = h_tracker.get_value()
            if abs(h) < 1e-8:
                return 2 * x
            return ((x + h) ** 2 - x ** 2) / h

        # 数值显示
        x_display = DecimalNumber(x_tracker.get_value(), num_decimal_places=2)
        x_display.add_updater(lambda m: m.set_value(x_tracker.get_value()))
        x_text = VGroup(Text("x = "), x_display).arrange(RIGHT, buff=0.1)
        x_text.to_corner(UL).shift(LEFT * 0.5)

        tangent_slope_display = DecimalNumber(2 * x_tracker.get_value(), num_decimal_places=3)
        tangent_slope_display.add_updater(lambda m: m.set_value(2 * x_tracker.get_value()))
        tangent_label = VGroup(Text("切线斜率 m = "), tangent_slope_display).arrange(RIGHT, buff=0.1)
        tangent_label.next_to(x_text, DOWN, aligned_edge=LEFT)

        secant_slope_display = DecimalNumber(secant_slope_val(), num_decimal_places=3)
        secant_slope_display.add_updater(lambda m: m.set_value(secant_slope_val()))
        secant_label = VGroup(Text("割线斜率 ≈ "), secant_slope_display).arrange(RIGHT, buff=0.1)
        secant_label.next_to(tangent_label, DOWN, aligned_edge=LEFT)

        # 场景开始
        self.add(axes)
        self.play(Create(parabola), run_time=1.5)
        self.play(Create(derivative_graph), run_time=1.0)
        self.play(FadeIn(parabola_label), FadeIn(deriv_label))
        self.wait(0.5)

        # 添加点与切线
        self.play(FadeIn(moving_point), FadeIn(tangent_line))
        self.play(FadeIn(x_text), FadeIn(tangent_label))
        self.wait(0.5)

        # 1️⃣ x 从左到右移动
        # self.play(x_tracker.animate.set_value(3.0), run_time=6, rate_func=there_and_back_with_pause)
        # self.wait(0.5)

        # 2️⃣ 割线出现
        self.play(FadeIn(secant_line), FadeIn(secant_label))
        self.play(h_tracker.animate.set_value(0.6), run_time=1.5)
        self.wait(0.4)
        self.play(h_tracker.animate.set_value(0.25), run_time=1.2)
        self.play(h_tracker.animate.set_value(0.06), run_time=1.2)
        self.play(h_tracker.animate.set_value(0.02), run_time=1.0)
        self.wait(0.8)

        # 不同位置上演示
        for x_pos in [-2,-1, 0,1, 2.0]:
            self.play(x_tracker.animate.set_value(x_pos), h_tracker.animate.set_value(3), run_time=1.2)
            self.play(h_tracker.animate.set_value(0.05), run_time=1.0)
            self.wait()

        # 3️⃣ x 从左到右连续移动，对比导函数
        self.play(x_tracker.animate.set_value(3.0), run_time=6, rate_func=smooth)
        self.wait()

        # 淡出割线与标签
        self.play(FadeOut(secant_line), FadeOut(secant_label))
        self.wait(0.5)

        # 收尾
        self.play(FadeOut(x_text), FadeOut(tangent_label), FadeOut(moving_point))
        self.wait(0.6)
