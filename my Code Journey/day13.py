# while 循环
"""import time
i = 0
while i < 100:
    print("人生苦短,我用python")
    time.sleep(0.05)
    i += 1
else:
    print("循环结束")

"""

# while 1到100的偶数的和
total = 0
i = 1
while i <= 100:
    if i % 2 == 0: # 偶数
        total += i
    i += 1
print(f"1到100的偶数之和:{total}")