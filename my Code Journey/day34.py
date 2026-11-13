# 匿名函数
data = ["c","c++","python","java","javascript","php","go","ruby"]
print(data)

data.sort(key=lambda x: len(x))
print(data)



# 案例
# n的阶乘
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n-1)

result = jc(10)
print(result)






# 电商订单计算器
def calc_order_cost(*args, coupon, score, express):
    """
    计算电商订单成本

    :param args: 商品价格列表
    :param coupon: 优惠券金额
    :param score: 积分
    :param express: 运费
    :return: 订单总成本
    """

    # 1.计算商品总金额
    total_price = [goods[1] * goods[2] for goods in args]
    total_cost = sum(total_price)
        

    # 2.减去优惠券金额
    if total_cost >= 5000 and coupon <= total_cost:
        total_cost -= coupon

    # 3.扣除积分抵扣（假设每个积分抵扣1元）
    if total_cost >= 5000 and score // 100 <= total_cost:
        total_cost -= score // 100

    # 4.加上运费
    total_cost += express

    return total_cost


# 示例调用
result = calc_order_cost(("键盘",299,1), ("显示器",599,1), coupon=500, score=1000, express=50)
print(result)
