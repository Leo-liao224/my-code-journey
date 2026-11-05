# --------------------------- 字典 常见操作 ---------------------------

dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询

print(dict1["涛哥"]) # 根据key获取value
print(dict1.get("涛哥")) # 根据key获取value

print(dict1.keys()) # 获取所有的key
print(dict1.values()) # 获取所有的value
print(dict1.items()) # 获取所有的键值对 key:value

# 删除

score = dict1.pop("许立国")
print(score)
print(dict1)

for k in dict1.keys():
    print(f"{k}:{dict1[k]}")

for k, v in dict1.items():
    print(f"{k}:{v}")




# 案例：
# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
# 具体功能如下：
#     1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#     2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#     3. 删除购物车：要求用户输入要删除的购物车商品名称，根据名称删除购物车中的商品。
#     4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：XXX，商品价格：XXX，商品数量：XXX"。
#     5. 退出购物车

# 结构：shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
# """

shopping_cart = {}
menu = """
######### 购物车管理系统 ##########
#          1. 添加购物车             #
#          2. 修改购物车             #
#          3. 删除购物车             #
#          4. 查询购物车             # 
#          5. 退出购物车             #
#####################################
"""

print("欢迎使用购物车管理系统")

while True:
    # 1. 制作菜单
    print(menu)


    # 2. 执行具体的操作
    choice = input("请输入操作编号(1-5):")


    match choice:
        case "1": # 添加购物车
            goods_name = input("请输入商品名称:")
            goods_price = float(input("请输入商品价格:"))
            goods_num = int(input("请输入商品数量:"))
            

            # 如果商品已经存在购物车中，则更新数量和价格
            if goods_name in shopping_cart:
                print(f"{goods_name}已存在购物车中")
            else:
                print(f"{goods_name}已添加到购物车中")
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
        case "2": # 修改购物车
            goods_name = input("请输入要修改的商品名称:")
            goods_price = float(input("请输入要修改的商品价格:"))
            goods_num = int(input("请输入要修改的商品数量:"))

            if goods_name not in shopping_cart:
                print(f"{goods_name}不存在购物车中")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print(f"{goods_name}已修改购物车信息")
        case "3": # 删除购物车
            goods_name = input("请输入要删除的商品名称:")
            if goods_name in shopping_cart:
                del shopping_cart[goods_name]
                print(f"{goods_name}已从购物车中删除")
            else:
                print(f"{goods_name}不存在购物车中")
        case "4": # 查询购物车
           for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
        case "5": # 退出购物车
            print("感谢使用购物车管理系统")
            break
        case _:
            print("无效的操作编号")
