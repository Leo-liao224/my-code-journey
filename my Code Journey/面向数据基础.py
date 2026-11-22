""" class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("已添加完毕")



C1 = Car("红色","BMW","X7",8000000)
print(C1.__dict__)

C2 = Car("白色","奔驰","E300",400000)
print(C2.__dict__)

 """




class Car:
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("已添加完毕")


    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中....")

    def total_cost(self,discount,rate):

        total_cost = self.price * discount + self.price * rate
        return total_cost

    def __str__(self):
        return f"{self.color}{self.brand}{self.name}{self.price}"
    
    def __eq__(self,other):
        return self.color == other.color and self.brand == other.brand


C1 = Car("红色","BMW","X7",8000000)
print(C1.__dict__)


C1.running()


total = C1.total_cost(0.000001,0.0001)
print("费用为",total)

