import os
import robosuite as suite
from robosuite.controllers import load_controller_config
import matplotlib.pyplot as plt

os.environ['MUJOCO_GL'] = 'egl'

controller_config = load_controller_config(default_controller="OSC_POSE")

env = suite.make(
    env_name="Lift",
    robots="Panda",
    controller_configs=controller_config,
    has_renderer=False,
    has_offscreen_renderer=True,
    use_camera_obs=True,
    camera_names="frontview",
    camera_heights=256,
    camera_widths=256,
    horizon=200,
    control_freq=20,
    renderer="mujoco",  # 明确指定渲染器
)

obs = env.reset()
img = obs["frontview_image"]

plt.imshow(img)
plt.title("MuJoCo+robosuite 渲染测试")
plt.axis("off")
plt.show()





# import robosuite as suite
# from robosuite.controllers import load_controller_config
# import matplotlib.pyplot as plt
# import numpy as np

# controller_config = load_controller_config(default_controller="OSC_POSE")

# env = suite.make(
#     env_name="Lift",
#     robots="Panda",
#     controller_configs=controller_config,
#     has_renderer=False,
#     has_offscreen_renderer=True,
#     use_camera_obs=True,
#     camera_names="frontview",
#     camera_heights=512,  # 提高分辨率
#     camera_widths=512,
#     horizon=200,
#     control_freq=20,
# )

# # 重置环境
# obs = env.reset()

# # 检查图像数据
# img = obs["frontview_image"]
# print(f"图像形状: {img.shape}")
# print(f"数据类型: {img.dtype}")
# print(f"数值范围: [{img.min()}, {img.max()}]")

# # 如果是浮点数需要转换
# if img.dtype == np.float32 or img.dtype == np.float64:
#     img = (img * 255).astype(np.uint8)

# plt.figure(figsize=(8, 8))
# plt.imshow(img)
# plt.title("MuJoCo+robosuite 渲染测试")
# plt.axis("off")
# plt.tight_layout()
# plt.show()





# import sys
# print("Python版本:", sys.version)

# try:
#     import mujoco
#     print("MuJoCo版本:", mujoco.__version__)
# except:
#     print("MuJoCo未安装或导入失败")

# try:
#     import robosuite
#     print("Robosuite版本:", robosuite.__version__)
# except:
#     print("Robosuite版本未知")

# import os
# print("MUJOCO_GL环境变量:", os.environ.get('MUJOCO_GL', '未设置'))
# print("操作系统:", os.name)

# try:
#     import OpenGL
#     print("PyOpenGL已安装")
# except:
#     print("PyOpenGL未安装")


# import robosuite
# import os

# # 检查robosuite安装路径
# robosuite_path = os.path.dirname(robosuite.__file__)
# print(f"Robosuite路径: {robosuite_path}")

# # 检查模型和资产路径
# models_path = os.path.join(robosuite_path, "models")
# assets_path = os.path.join(robosuite_path, "models", "assets")

# print(f"\n模型路径存在: {os.path.exists(models_path)}")
# print(f"资产路径存在: {os.path.exists(assets_path)}")

# # 检查纹理文件
# if os.path.exists(assets_path):
#     textures_path = os.path.join(assets_path, "textures")
#     if os.path.exists(textures_path):
#         print(f"\n纹理文件:")
#         for f in os.listdir(textures_path)[:10]:
#             print(f"  - {f}")
#     else:
#         print("\n警告: 未找到纹理目录!")

# # 检查机器人模型
# robots_path = os.path.join(models_path, "robots")
# if os.path.exists(robots_path):
#     print(f"\n机器人模型:")
#     for robot in os.listdir(robots_path)[:5]:
#         print(f"  - {robot}")