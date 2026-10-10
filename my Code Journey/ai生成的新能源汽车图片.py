import matplotlib.pyplot as plt

# 设置中文字体，防止乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ================= 1. 定义变量（必须放在最前面！） =================
initial_range = 500          # 初始标称续航：500 km
total_mileage = 100000       # 总行驶里程：10万公里
step = 1000                  # 每 1000 公里记录一次数据点

# ================= 2. 生成模拟数据 =================
# 生成从 0 到 100000 的里程列表，步长为 1000
mileage_list = list(range(0, total_mileage + 1, step))

# 模拟电池健康度 (SOH) 衰减。
# 行业内通常认为，电池衰减是非线性的（前几年慢，后面快），且 SOH 降到 80% 就需要退役。
# 我们用一个稍微带点非线性的公式来模拟
soh_list = [100 - 8 * (m / 10000) ** 1.5 for m in mileage_list]

# 计算实际续航（实际续航 = 初始续航 * 当前的电池健康度）
actual_range_list = [initial_range * (soh / 100) for soh in soh_list]

# ================= 3. 开始画图 =================
plt.plot(mileage_list, actual_range_list, marker='o', color='#e74c3c', linewidth=2, markersize=3)

# 添加图表信息
plt.title('新能源汽车电池寿命与续航衰减曲线', fontsize=15)
plt.xlabel('行驶里程 (km)', fontsize=12)
plt.ylabel('实际预估续航 (km)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

# 保存图片并显示
plt.savefig('battery_degradation.png')
plt.show()