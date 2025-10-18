# -*- coding: utf-8 -*-
from manim import *
import numpy as np

class CinematicCylinderPath(ThreeDScene):
    def construct(self):
        # 设置初始相机角度
        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES, zoom=1.2)

        # 圆柱与截面
        cylinder = Cylinder(radius=2, height=3, color=BLUE, fill_opacity=0.5)
        plane = Square(side_length=4, fill_color=RED, fill_opacity=0.4)
        plane.rotate(PI / 4, axis=RIGHT)
        plane.shift(OUT * 0.3)
        self.add(cylinder, plane)

        # ===== 椭圆路径定义 =====
        num_points = 200
        a, b = 7, 5  # 椭圆长短轴
        path_points = [
            np.array([
                a * np.cos(t),
                b * np.sin(t),
                2 + 0.8 * np.sin(t / 1.5)  # z方向波动
            ])
            for t in np.linspace(0, 2 * PI, num_points)
        ]

        # 路径曲线
        path_curve = VMobject(color=YELLOW)
        path_curve.set_points_smoothly(path_points)
        self.add(path_curve)

        # ===== 轨迹小球（相机位置指示） =====
        camera_marker = Sphere(radius=0.15, color=YELLOW).move_to(path_points[0])
        self.add(camera_marker)

        # ===== 相机沿路径移动 =====
        self.smooth_camera_path(path_points, camera_marker, run_time=10)

        self.wait(2)

    def smooth_camera_path(self, points, marker, run_time=10):
        """相机沿路径平滑移动，动态调整仰角与缩放，并同步移动小球"""
        n = len(points)
        base_phi = 60 * DEGREES
        phi_amp = 10 * DEGREES
        base_zoom = 1.2
        zoom_amp = 0.2

        for i, pos in enumerate(points):
            progress = i / n
            phi = base_phi + phi_amp * np.sin(2 * PI * progress)
            zoom = base_zoom + zoom_amp * np.sin(4 * PI * progress)
            theta = np.degrees(np.arctan2(pos[1], pos[0]))

            # 移动小球
            marker.move_to(pos)

            # 更新相机角度
            self.set_camera_orientation(phi=phi, theta=theta * DEGREES, zoom=zoom)
            self.wait(run_time / n)
