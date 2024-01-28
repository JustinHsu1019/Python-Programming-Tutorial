import turtle
import time

# ============================================================

screen = turtle.Screen()
screen.title("滾動的圓圈")

circle = turtle.Turtle()
circle.shape("circle")

# 定義圓圈滾動的距離和速度
distance = 10
speed = 0.1  # 控制滾動的速度，數值越小速度越快

# 使用 while 迴圈來使圓圈不斷繞圓滾動
while True:
    circle.forward(distance)
    circle.right(10)
    time.sleep(speed)  # 使用 time 模塊的 sleep 函數來控制速度

turtle.done()
