from cx_Freeze import setup, Executable

# 这里填写主程序脚本
executables = [Executable("wzs.py")]

# 设置参数
setup(
    name="MyAppwzs",  # 应用的名称
    version="1.0",  # 版本号
    description="My Python Application",
    executables=executables
)
