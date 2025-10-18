from manim import *
import numpy as np

class CylinderFrustum(ThreeDScene):
    def construct(self):
        # 参数：底面半径 r1, 顶面半径 r2, 高度 h
        r1 = 1.2
        r2 = 0.5
        h = 2.0

        # 辅助：侧面参数化 (u = theta, v = [0..1] height fraction)
        def side_point(u, v):
            theta = u
            z = v * h
            r = r1 + (r2 - r1) * v  # 线性过渡半径 => 截体
            return np.array([r * np.cos(theta), r * np.sin(theta), z])

        # 侧面 (参数 u in [0, TAU], v in [0,1])
        side = Surface(
            lambda u, v: side_point(u, v),
            u_range=[0, TAU],
            v_range=[0, 1],
            resolution=(64, 24),
        )
        side.set_fill(TEAL, opacity=0.6)
        side.set_stroke(width=0.5)
        side.set_shade_in_3d(True)

        # 上端盘 (z = h, radius = r2)
        top_disk = Surface(
            lambda u, v: np.array([r2 * v * np.cos(u), r2 * v * np.sin(u), h]),
            u_range=[0, TAU],
            v_range=[0, 1],
            resolution=(64, 8),
        )
        top_disk.set_fill(BLUE_D, opacity=0.7)
        top_disk.set_stroke(width=0.5)
        top_disk.set_shade_in_3d(True)

        # 下端盘 (z = 0, radius = r1)
        bottom_disk = Surface(
            lambda u, v: np.array([r1 * v * np.cos(u), r1 * v * np.sin(u), 0]),
            u_range=[0, TAU],
            v_range=[0, 1],
            resolution=(64, 8),
        )
        bottom_disk.set_fill(ORANGE, opacity=0.7)
        bottom_disk.set_stroke(width=0.5)
        bottom_disk.set_shade_in_3d(True)

        # 三维坐标轴，便于观察方向
        axes = ThreeDAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            z_range=[-0.5, 2.5, 1],
            x_length=4,
            y_length=4,
            z_length=3,
        )

        # 初始相机角度（斜视）
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        # self.add(axes)  # 先把 axes 加入（不做动画）
        self.wait(0.5)

        # 绘制截体（先侧面，再两个端面）
        self.play(Create(side), run_time=2)
        self.play(Create(top_disk), Create(bottom_disk), run_time=1.5)
        self.wait(0.8)

        # self.move_camera(phi=70 * DEGREES, theta=-90 * DEGREES, run_time=2)
        # self.wait(0.8)

        # self.move_camera(phi=70 * DEGREES, theta=0 * DEGREES, run_time=2)
        # self.wait(0.8)

        # self.move_camera(phi=90 * DEGREES, theta=-45 * DEGREES, run_time=2)
        # self.wait(0.8)

        # self.move_camera(phi=60 * DEGREES, theta=-30 * DEGREES, run_time=2)
        # self.wait(0.8)

        # self.begin_ambient_camera_rotation(rate=0.4)
        # self.wait(6)
        # self.stop_ambient_camera_rotation()

        # 缩放并给出一个说明标签（可选）
        label = MathTex(r"\text{Cylinder Frustum (Hello)}").scale(0.7)
        label.to_corner(UR)
        self.add_fixed_in_frame_mobjects(label)
        self.wait(1)
