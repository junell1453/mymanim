# 🎬 Manim + uv + VS Code 安装使用指南（Windows）

本文介绍如何在 Windows 上通过 **uv + VS Code** 创建虚拟环境、配置 Python 解释器，并成功安装 **Manim Community Edition (v0.19.0)**。

---

## 一、安装 Python 与 VS Code 插件

### 1. 安装 Python

推荐使用 **Python 3.10 ~ 3.12** 版本（Manim 暂不支持 3.14）。
可直接让 uv 管理版本，稍后执行

### 2. 安装 VS Code 插件

打开 VS Code → 左侧扩展面板（Ctrl + Shift + X）→ 搜索并安装：

* **Python**（ms-python.python）
* **Pylance**（自动依赖）
* **Jupyter**（可选）

启用后，可在命令面板（Ctrl + Shift + P）中看到：

```
Python: Select Interpreter
```

---

## 二、安装与使用 uv 工具

### 1. 安装 uv

**Windows PowerShell：**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

验证安装：

```bash
uv --version
```

---

## 三、创建项目与虚拟环境

在 VS Code 终端中执行：

```bash
# 创建项目
uv init mymanim
cd mymanim

---

## 四、安装 Manim（使用 uv）


```bash
uv python install 3.12
uv venv --python 3.12
uv pip install manim
```

---

## 五、运行 Manim

无需手动激活环境，可直接运行：

```bash
# uv run manim -pql main.py SceneName
manim -pql derivative_parabola.py DerivativeParabola
```


---

## ✅ 推荐最终安装命令（完整流程）

```bash
# 1️⃣ 安装 Python 3.12
uv python install 3.12

# 2️⃣ 创建项目与环境
uv init mymanim
cd mymanim
uv venv --python 3.12

# 3️⃣ 安装 manim
uv pip install manim

# 4️⃣ 启动示例
uv run manim -pql example_scenes.py SquareToCircle

# 或
manim -pql example_scenes.py
```

---
## 问题1：解决 PowerShell 执行策略限制

激活环境时报错：

```
无法加载文件 Activate.ps1，因为在此系统上禁止运行脚本。
```

### 解决办法（推荐安全方案）：

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

然后重新执行：

```powershell
& .venv/Scripts/Activate.ps1
```

成功后命令行前会出现：

```
(.venv) PS .\mymanim>
```

---

## 问题2. 让 VS Code 使用虚拟环境

### 方法 1：自动检测（推荐）

若虚拟环境命名为 `.venv/`，VS Code 通常会自动提示选择解释器。

### 方法 2：手动选择

命令面板（Ctrl + Shift + P） → 输入：

```
Python: Select Interpreter
```

选择 `.venv\Scripts\python.exe`