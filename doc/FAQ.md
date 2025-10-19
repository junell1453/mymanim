# 🎬 Manim Community v0.19.0 常见问题与解决方案整理

作者：朱致远
环境：Windows + PowerShell + Manim Community v0.19.0
虚拟环境：`(mymanim)`

---

## 📘 1. Manim 基本信息

运行：

```bash
uv pip show manim
```

输出类似：

```
Name: manim
Version: 0.19.0
Location: D:\bupt\mymanim\.venv\Lib\site-packages
```

说明安装成功。
若命令行执行 `manim` 提示无法识别，需激活虚拟环境或将其路径加入系统环境变量。

---

## ⚙️ 2. 常见运行命令

```bash
manim -pql my_scene.py ClassName
```

说明：

* `-p`：渲染完成后自动播放；
* `-q`：渲染质量（`l` = low，`h` = high）；
* `my_scene.py`：脚本文件；
* `ClassName`：场景类名。

---

## 🚨 3. 常见错误与修复

### 3.1 ❌ `There are no scenes inside that module`

**原因：** 文件中没有定义继承自 `Scene` 或其子类的类。
**解决：** 确保代码中有类似：

```python
from manim import *

class MovingCircle(Scene):
    def construct(self):
        self.play(Create(Circle()))
```

---

### 3.2 ⚠️ `RuntimeWarning: Couldn't find ffmpeg`

**原因：** 未安装 ffmpeg 或未加入 PATH。
**解决：**

1. 安装 ffmpeg（推荐 Windows 包管理器 chocolatey）：

   ```bash
   choco install ffmpeg
   ```
2. 或手动下载后将 ffmpeg 的 `bin` 目录加入系统环境变量。

---

### 3.3 ❌ `AttributeError: 'ThreeDCamera' object has no attribute 'frame'`

**原因：** 旧版本 Manim 的 3D 相机接口变化。
**解决：** 使用新版接口：

```python
self.set_camera_orientation(phi=60*DEGREES, theta=45*DEGREES)
```

并避免直接访问 `self.camera.frame`。

---

### 3.4 ❌ `UnicodeDecodeError: 'gbk' codec can't decode byte ...`

**原因：** Python 在 Windows 上默认使用 GBK 读取文件，但脚本文件为 UTF-8。
**解决：**

1. 在文件开头添加：

   ```python
   # -*- coding: utf-8 -*-
   ```
2. 或运行：

   ```bash
   chcp 65001
   ```

   让 PowerShell 切换到 UTF-8 模式。

---

### 3.5 ❌ `AttributeError: 'MovingCircle' object has no attribute 'add_fixed_in_frame_mobjects'`

**原因：**

* `Scene` 类没有此方法；
* 或在 v0.19.0 版本中 `MovingCameraScene` 的接口兼容性不同。

**解决方式：**

#### ✅ 方法一（最简洁）

直接去掉固定元素：

```python
class MovingCircle(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        text = Text("Moving Circle").to_corner(UR)
        self.add(text, circle)
```

#### ✅ 方法二（带固定标签）

```python
class MovingCircle(MovingCameraScene):
    def construct(self):
        circle = Circle(color=BLUE)
        text = Text("Moving Circle").scale(0.6)
        try:
            self.add_fixed_in_frame_mobjects(text)
        except AttributeError:
            self.add(text)
        text.to_corner(UR)

        self.play(Create(circle))
        self.play(circle.animate.shift(RIGHT * 4), run_time=2)
```

---

### 3.6 ❌ `AttributeError: 'Camera' object has no attribute 'frame'`

**原因：** `Scene` 使用的相机是 `Camera`，没有 `.frame` 属性。
**解决：** 使用 `MovingCameraScene` 或删除 `.frame` 相关操作。

---

### 3.7 ❌ `AttributeError: property 'camera' of 'MovingCircle' object has no setter`

**原因：** 不可手动重新赋值 `self.camera`。
**错误写法：**

```python
self.camera = MovingCamera()  # ❌
```

**正确做法：** 直接使用现有相机实例。

---

