import turtle

# Create a turtle object
star = turtle.Turtle()

# Loop to draw the star
for _ in range(5):
    star.forward(100)  # Move forward by 100 units
    star.right(144)    # Turn right by 144 degrees

# Keep the window open
turtle.done()
