from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_forward(self):
        for snake_seg in range(len(self.segments)-1, 0, -1):
            x = self.segments[snake_seg - 1].xcor()
            y = self.segments[snake_seg - 1].ycor()
            self.segments[snake_seg].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # def my_create_snake(self):
    #     for i in range(0, 3):
    #         new_snake_square = Turtle()
    #         new_snake_square.shape("square")
    #         new_snake_square.speed("slowest")
    #         new_snake_square.penup()
    #         new_snake_square.setposition((0 + (i * -20)), 0)
    #         new_snake_square.color("white")
    #         self.segments.append(new_snake_square)

    # def my_move_forward(self):
    #     previous_position = ()
    #     for snake_segment in self.segments:
    #         temp_position = snake_segment.pos()
    #         if previous_position == ():
    #             snake_segment.forward(20)
    #         else:
    #             snake_segment.goto(previous_position)
    #         previous_position = temp_position
