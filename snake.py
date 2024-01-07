import turtle
import time
import random

delay = 0.1
score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Up"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Motivational message display
motivational_display = turtle.Turtle()
motivational_display.speed(0)
motivational_display.color("white")
motivational_display.penup()
motivational_display.hideturtle()
motivational_display.goto(0, 230)

# Motivational messages
motivational_messages = [
    "Great job! Keep it up!",
    "You're doing fantastic!",
    "Amazing! Keep going!",
    "You're a snake master!",
    "Incredible moves! Keep it rolling!",
]

# Functions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random location
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score
        score += 10
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Display a motivational message
        motivational_display.clear()
        motivational_display.write(random.choice(motivational_messages), align="center", font=("Courier", 12, "normal"))

    # Move the end segments first in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for a collision with the border
    if head.xcor() > 290:
        head.setx(-290)
    elif head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)
    elif head.ycor() < -290:
        head.sety(290)

    # Check for head collisions with body segments
    for segment in segments:
        if head.distance(segment) < 20:
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Up"

            # Hide the segments
            for seg in segments:
                seg.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)
