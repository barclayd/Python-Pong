import turtle
import random

# setup
wn = turtle.Screen()
wn.title("Arcade Style Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0
ball.dy = 0

# game state
new_game = True

# speed controls

paddle_a_speed = 15
paddle_b_speed = 15

# game controls


def move_paddle_a_up():
    y = paddle_a.ycor()
    if y < 232:
        y += paddle_a_speed
    paddle_a.sety(y)


def move_paddle_a_down():
    y = paddle_a.ycor()
    if y > -225:
        y -= paddle_a_speed
    paddle_a.sety(y)


def move_paddle_b_up():
    y = paddle_b.ycor()
    if y < 232:
        y += paddle_b_speed
    paddle_b.sety(y)


def move_paddle_b_down():
    y = paddle_b.ycor()
    if y > -225:
        y -= paddle_b_speed
    paddle_b.sety(y)


def start_game():
        if new_game:
            ball.dx = random.choice([-1, 1])
            ball.dy = random.choice([-1, 1])


# keybindings

turtle.listen()
turtle.onkeypress(move_paddle_a_up, "w")
turtle.onkeypress(move_paddle_a_down, "s")
turtle.onkeypress(move_paddle_b_up, "Up")
turtle.onkeypress(move_paddle_b_down, "Down")
turtle.onkeypress(start_game, "space")




# Game loop
while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # if ball has moved
    if ball.xcor() != 0 and ball.ycor() !=0:
        new_game = False

    # border checking
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # paddle A and ball collision
    if (ball.xcor() < -330 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1

    # paddle B and ball collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

