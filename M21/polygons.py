import turtle

# Setup screen
sc = turtle.Screen()
sc.bgcolor("Green")

# Create turtle object
board = turtle.Turtle()

# Draw Triangle
for _ in range(3):
    board.forward(100)
    board.left(120)

# Move turtle to a new position for the square
board.penup()  # Lift pen to prevent drawing while moving
board.forward(150)  # Move forward to separate the shapes
board.pendown()  # Put pen down to start drawing again

# Draw Square
for _ in range(4):
    board.forward(100)
    board.left(90)

# Keep window open
turtle.done()
