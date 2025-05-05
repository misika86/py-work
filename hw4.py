import math 
import numpy as np
import random

def parabola(x,a,b,c):
    return a*x**2+b*x+c
def sliding(a,b,c,x_initial,x_end,miu,m,g=9.8):
    x=x_initial
    y=parabola(x,a,b,c)
    v=0
    t=0
    dt=0.001
    while x<x_end:
        dy_dx = 2*a*x+b
        theta = math.atan(dy_dx)
        Fy = m*g*math.cos(theta)
        f = miu*Fy
        Fx = m*g*math.sin(theta) - f
        accel = Fx / m
        v = v + accel * dt
        ds = v * dt
        dx = ds * math.cos(theta)
        x = x + dx
        t = t + dt
    return t

h = 8
d = 10
a = random.uniform(-0.1, 0.1)
b = random.uniform(-5, 5)
c = h
x_initial = 0
x_end = d
m = 5
miu = 0.1

time_with_friction = sliding(a,b,c,x_initial,x_end,miu,m)
time_without_friction = sliding(a,b,c,x_initial,x_end,0,m)

print(f"考虑摩擦力时钢块到达终点的时间：{time_with_friction:.2f}秒")
print(f"不考虑摩擦力时钢块到达终点的时间: {time_without_friction:.2f}秒")