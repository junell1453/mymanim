# -*- coding: utf-8 -*-
from manim import *

class NorGateDemo(Scene):
    """
    兼容 Manim Community v0.19.0
    2输入NOR门逻辑演示动画
    """

    def construct(self):
        # 颜色定义
        HIGH_COLOR = RED
        LOW_COLOR = GRAY
        GATE_COLOR = WHITE

        # 绘制NOR门形状
        gate_body = VMobject(stroke_color=GATE_COLOR, stroke_width=4)
        gate_body.set_points_as_corners(
            [LEFT * 2 + DOWN * 1.5, LEFT * 2 + UP * 1.5, ORIGIN + UP * 1.5]
        )
        arc = ArcBetweenPoints(
            start=LEFT * 2 + DOWN * 1.5,
            end=ORIGIN + DOWN * 1.5,
            angle=-PI / 1.3,
            color=GATE_COLOR,
            stroke_width=4
        )
        gate_shape = VGroup(arc, gate_body)

        # 小圆（表示NOR的NOT）
        circle_radius = 0.15
        not_circle = Circle(radius=circle_radius, color=GATE_COLOR, stroke_width=4)
        not_circle.next_to(ORIGIN + RIGHT * 0.2, RIGHT, buff=0)

        gate = VGroup(gate_shape, not_circle)
        gate.move_to(ORIGIN)

        # 输入/输出线
        input1_line = Line(LEFT * 4, gate.get_left() + UP * 0.7, color=LOW_COLOR, stroke_width=6)
        input2_line = Line(LEFT * 4, gate.get_left() + DOWN * 0.7, color=LOW_COLOR, stroke_width=6)
        output_line = Line(not_circle.get_right(), RIGHT * 4, color=LOW_COLOR, stroke_width=6)

        # 标签
        label_a = Text("A", font_size=32).next_to(input1_line, LEFT)
        label_b = Text("B", font_size=32).next_to(input2_line, LEFT)
        label_y = Text("Y", font_size=32).next_to(output_line, RIGHT)

        # 输出灯泡
        bulb = Circle(radius=0.2, stroke_width=3, color=WHITE)
        bulb.set_fill(color=BLACK, opacity=1)
        bulb.next_to(output_line, RIGHT, buff=0.2)

        # 添加所有元素
        self.add(input1_line, input2_line, output_line, gate, label_a, label_b, label_y, bulb)

        # 输入状态序列 (A, B)
        states = [(0, 0), (0, 1), (1, 0), (1, 1)]

        # 更新灯泡颜色与信号颜色
        def update_lines(a_val, b_val):
            # 输出 = not (A or B)
            y_val = 1 if (a_val == 0 and b_val == 0) else 0

            # 设置颜色
            input1_line.set_color(HIGH_COLOR if a_val else LOW_COLOR)
            input2_line.set_color(HIGH_COLOR if b_val else LOW_COLOR)
            output_line.set_color(HIGH_COLOR if y_val else LOW_COLOR)

            bulb.set_fill(HIGH_COLOR if y_val else BLACK, opacity=1)
            return y_val

        # 动画展示输入变化
        text_state = Text("", font_size=32).to_edge(DOWN)

        self.play(Write(text_state))

        for a_val, b_val in states:
            y_val = update_lines(a_val, b_val)
            # 状态文字更新
            new_text = Text(f"A={a_val}, B={b_val} → Y={y_val}", font_size=32).to_edge(DOWN)
            self.play(Transform(text_state, new_text), run_time=0.8)
            self.wait(1.5)

        # 结束动画
        self.wait(1)
        self.play(FadeOut(text_state), FadeOut(bulb))
        self.wait(0.5)
