import math#求平方根
initial_height = 100#初始高度设定为100米
g = 9.8#重力加速度设定为9.8m/s2
def calculate_height_10th():#定义计算第十次落地反弹的高度函数
    tenth_rebound_height = initial_height / (2 ** 10)#计算第十次落地反弹的高度
    total_distance = initial_height#初始距离为初始高度
    for i in range(1, 10):#计算前九次反弹的上下运动的距离
        total_distance += 2 * (initial_height / (2 ** i))
    total_time = math.sqrt(2 * initial_height / g)#第一次下落的时间，自由落体运动时间t=根号(2h/g)
    for i in range(1,10):#计算前九次反弹的时间
        height = initial_height / (2 ** i)#第n次反弹的高度是初始高度除以2的n次方
        total_time += math.sqrt(2 * height / g)
    print(f"小球第10次落下并反弹回最高点时，反弹高度为：{tenth_rebound_height:.2f}米")
    print(f"小球在第10次落地时，共经过了{total_distance:.2f}米")
    print(f"小球在第10次落地时，共经过了{total_time:.2f}秒")
calculate_height_10th()#计算第十次落地反弹的高度，经过的总路程和总时间
def calculate_height_nth(n):#定义计算第n次落地反弹的高度的函数
    nth_rebound_height = initial_height / (2 ** n)#计算第n次落地反弹的高度
    total_distance = initial_height#初始化总距离为初始高度
    for i in range(1, n):#计算前n-1次反弹上下运动的总距离
        total_distance += 2 * (initial_height / (2 ** i))
    total_time = math.sqrt(2 * initial_height / g)#第一次下落的时间，根据自由落体运动公式t=根号(2h/g)
    for i in range(1,n):#计算前n-1次反弹所需要的时间
        height = initial_height / (2 ** i)
        total_time += math.sqrt(2 * height / g)
    print(f"小球第{n}次落下并反弹回最高点时，反弹高度为：{nth_rebound_height:.2f}米")
    print(f"小球在第{n}次落地时，共经过了{total_distance:.2f}米")
    print(f"小球在第{n}次落地时，共经过了{total_time:.2f}秒")

calculate_height_nth(10)

