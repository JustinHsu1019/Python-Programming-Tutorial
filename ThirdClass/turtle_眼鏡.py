import turtle

screen = turtle.Screen()
screen.title("眼鏡")

circle = turtle.Turtle()
circle.shape("circle")

distance = 10

for _ in range(36):
    circle.forward(distance)
    circle.right(10)

circle.forward(115)

for _ in range(36):
    circle.forward(distance)
    circle.right(10)

turtle.done()
