import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor('green')

# Create a turtle instance
t = turtle.Turtle()
t.shape("turtle")

# Draw blue square
t.pencolor("blue")
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw yellow rectangle
t.penup()
t.goto(15, 23)
t.pendown()
t.pencolor("yellow")
for _ in range(2):
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)

# Draw white triangle
t.penup()
t.goto(-23, 52)
t.pendown()
t.pencolor('white')

for _ in range(3):
    t.forward(100)
    t.right(120)

# Keep the window open
turtle.done()
