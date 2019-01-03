import turtle

wn = turtle.Screen()
wn.title("Arcade Style Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Game loop
while True:
    wn.update()
