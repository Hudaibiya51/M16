import turtle

# Setup the screen
sc = turtle.Screen()
sc.bgcolor("Orange")

# Create turtle object
board = turtle.Turtle()

# Increase speed
board.speed(3)

# First Triangle (Upward)
for _ in range(3):
    board.forward(100)
    board.left(120)

# Move to the correct position for the second triangle
board.penup()
board.left(180)  # Flip direction
board.forward(50)  # Move to the center
board.pendown()

# Second Triangle (Downward)
for _ in range(3):
    board.forward(100)
    board.right(120)

# Keep the window open
turtle.done()
