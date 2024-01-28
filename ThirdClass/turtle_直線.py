import turtle
import time

# ============================================================

screen = turtle.Screen()
screen.title("滾動的方塊")

square = turtle.Turtle()
square.shape("square")

# 定義方塊滾動的距離和速度
distance = 10
speed = 0.1  # 控制滾動的速度，數值越小速度越快

# 使用 while 迴圈來使方塊不斷向前滾動
while True:
    square.forward(distance)
    time.sleep(speed)  # 使用 time 模塊的 sleep 函數來控制速度

turtle.done()
