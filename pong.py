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

# game welcome

welcome_message = " Arcade Pong (2 player game)"
welcome_pen = turtle.Turtle()
welcome_pen.speed(0)
welcome_pen.color("blue")
welcome_pen.penup()
welcome_pen.setposition(0, 100)
welcome_pen.write(welcome_message, False, align="center", font=("Verdana", 36, "bold"))
welcome_pen.hideturtle()

intro_message = "Press Space to Begin"
intro_pen = turtle.Turtle()
intro_pen.speed(0)
intro_pen.color("white")
intro_pen.penup()
intro_pen.setposition(0, 50)
intro_pen.write(intro_message, False, align="center", font=("Verdana", 24, "bold"))
intro_pen.hideturtle()


# scoring

paddle_a_score_count = 0
paddle_a_score_message = "Player A: %s" % paddle_a_score_count
paddle_a_score = turtle.Turtle()
paddle_a_score.speed(0)
paddle_a_score.color("red")
paddle_a_score.penup()
paddle_a_score.setposition(-100, 270)
paddle_a_score.hideturtle()


paddle_b_score_count = 0
paddle_b_score_message = "Player B: %s" % paddle_b_score_count
paddle_b_score = turtle.Turtle()
paddle_b_score.speed(0)
paddle_b_score.color("blue")
paddle_b_score.penup()
paddle_b_score.setposition(100, 270)
paddle_b_score.hideturtle()

# speed controls

paddle_a_speed = 30
paddle_b_speed = 30

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
    if y < 236:
        y += paddle_b_speed
    paddle_b.sety(y)


def move_paddle_b_down():
    y = paddle_b.ycor()
    if y > -212:
        y -= paddle_b_speed
    paddle_b.sety(y)


def start_game():
        if new_game:
            ball.dx = random.choice([-4, 4])
            ball.dy = random.choice([-4, 4])
            welcome_pen.clear()
            intro_pen.clear()


# keybindings

turtle.listen()
turtle.onkeypress(move_paddle_a_up, "w")
turtle.onkeypress(move_paddle_a_down, "s")
turtle.onkeypress(move_paddle_b_up, " Up")
turtle.onkeypress(move_paddle_b_down, "Down")
turtle.onkeypress(start_game, "space")




# Game loop
while True:
    wn.update()

    if new_game == False and paddle_a_score_count == 0 and paddle_b_score_count == 0:
        paddle_a_score.write(paddle_a_score_message, False, align="center", font=("Verdana", 18, "normal"))
        paddle_b_score.write(paddle_b_score_message, False, align="center", font=("Verdana", 18, "normal"))

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # if ball has moved
    if ball.xcor() != 0 and ball.ycor() !=0:
        new_game = False

    # border checking
    if ball.xcor() > 390:
        paddle_a_score_count += 1
        paddle_a_score.clear()
        paddle_a_score_message = "Player A: %s" % paddle_a_score_count
        paddle_a_score.write(paddle_a_score_message, False, align="center", font=("Verdnana", 18, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        paddle_b_score_count += 1
        paddle_b_score_message = "Player B: %s" % paddle_b_score_count
        paddle_b_score.clear()
        paddle_b_score.write(paddle_b_score_message, False, align="center", font=("Verdnana", 18, "normal"))
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

