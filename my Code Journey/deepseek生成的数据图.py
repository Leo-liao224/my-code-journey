import matplotlib.pyplot as plt

import numpy as np


# 1. 设置中文字体，防止显示乱码（Windows通常用黑体）

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False


# 2. 模拟一段真实的车辆行驶数据（150分钟，模拟一段长途测试）

time = np.linspace(0, 150, 150)  # 0到150分钟

speed = 80 * np.sin(time * 0.05) + 100 * np.exp(-0.01 * (time - 70)**2) # 模拟加减速和最高时速

battery_soc = 100 - (time / 150) * 35  # 模拟电量从100%掉到65%

motor_temp = 40 + (speed / 100) * 30 + np.random.normal(0, 1, 150) # 速度越快温度越高，带点随机噪音

energy_consumption = (speed / 100) * 15 + np.random.normal(0, 0.5, 150) # 能耗 (kWh/100km)


# 3. 创建多子图布局（2行2列）

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

fig.suptitle('深汕新能源汽车 - 整车动态数据仪表盘', fontsize=20, fontweight='bold', y=0.98)


# 子图1：车速曲线

axs[0, 0].plot(time, speed, color='#2ecc71', linewidth=2.5)

axs[0, 0].set_title('车速 (km/h)', fontsize=14, fontweight='bold')

axs[0, 0].set_xlabel('时间 (分钟)')

axs[0, 0].set_ylabel('速度')

axs[0, 0].grid(True, linestyle='--', alpha=0.6)


# 子图2：电池电量

axs[0, 1].plot(time, battery_soc, color='#3498db', linewidth=2.5)

axs[0, 1].fill_between(time, battery_soc, alpha=0.2, color='#3498db')

axs[0, 1].set_title('电池剩余电量 (SOC %)', fontsize=14, fontweight='bold')

axs[0, 1].set_xlabel('时间 (分钟)')

axs[0, 1].set_ylabel('电量 (%)')

axs[0, 1].grid(True, linestyle='--', alpha=0.6)


# 子图3：电机温度

axs[1, 0].plot(time, motor_temp, color='#e74c3c', linewidth=2.5)
jls_extract_var = linestyle
axs[1, 0].axhline(y=80, color='r', jls_extract_var=':', label='过热警戒线')

axs[1, 0].set_title('电机温度 (°C)', fontsize=14, fontweight='bold')

axs[1, 0].set_xlabel('时间 (分钟)')

axs[1, 0].set_ylabel('温度 (°C)')

axs[1, 0].legend()

axs[1, 0].grid(True, linestyle='--', alpha=0.6)


# 子图4：能耗

axs[1, 1].plot(time, energy_consumption, color='#f39c12', linewidth=2.5)

axs[1, 1].set_title('瞬时能耗 (kWh/100km)', fontsize=14, fontweight='bold')

axs[1, 1].set_xlabel('时间 (分钟)')

axs[1, 1].set_ylabel('能耗')

axs[1, 1].grid(True, linestyle='--', alpha=0.6)


# 4. 自动调整布局并保存/显示

plt.tight_layout(rect=[0, 0, 1, 0.95])

plt.savefig('car_dashboard.png', dpi=300)

print("图表已生成！正在打开窗口...")

plt.show()