#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle
import math
import random

def drawField(sideLength):
    perimeter = turtle.Turtle()     # Instantiate turtle object 
    perimeter.hideturtle()          # I never want to show perimeter turtle 
    perimeter.degrees()             # Make sure perimeter works in degrees
    perimeter.speed(0)              # Max speed
    perimeter.color(0,0,0)          # Black pen and fill
    perimeter.penup()               # Raise pen before resetting position
    perimeter.setposition(0,0)      # Go to origin
    perimeter.setheading(90)        # Face up to begin
    perimeter.pendown()             # Return pen to canvas
    for i in range(4):              # Draw a 144 by 144 square
        perimeter.forward(sideLength)      
        perimeter.right(90)

    # Draw flags
    flagsPos = [0.832978, 0.499645, 0.168218]
    for flagPos in flagsPos:
        perimeter.penup()
        perimeter.setposition(sideLength*flagPos, sideLength)
        perimeter.setheading(-90)
        perimeter.pendown()
        perimeter.forward(0.076759*sideLength)


def ultrasounds(pose, sideLength, colors):
    sound = turtle.Turtle()     # Instantiate turtle object 
    sound.hideturtle()          # I never want to show sound turtle
    sound.degrees()             # Make sure sound works in degrees
    sound.speed(0)              # Max speed
    sound.color("#080808")      # Gray pen and fill
    sound.penup()               # Raise pen before resetting position

    distances = []
    offsets = [(0, colors[0]), (90, colors[1]), (180, colors[2]), (270, colors[3])]
    
    # Draw four perpendicular lines representing ultra sound sensor reading
    for offset, color in offsets:
        sound.color(color)
        sound.setposition(pose["x"],pose["y"])
        sound.setheading(pose["orientation"]+offset)
        sound.pendown()             # Return pen to canvas
        # Draw the line until in perimeter border
        while 0 < sound.xcor() < sideLength and 0 < sound.ycor() < sideLength:
            sound.forward(1)
        # Raise pen in preparation for next iteration
        sound.penup()
        # Save current distance to wall
        distances.append(sound.distance(pose["x"], pose["y"]))

    
    return distances


def main():
    # Your code starts here ---------------------------------------------------

    fieldWidth = 144

    tests = []
    for i in range(10):
        pose = []
        pose.append(random.randint(1,fieldWidth))
        pose.append(random.randint(1,round(fieldWidth*0.9)))
        pose.append(90)
        tests.append(pose)

    print(tests)


    for x, y, o in tests:
        robot = turtle.Turtle()
        robot.degrees()
        robot.speed(0)
        colors = ["#FE2712", "#FEFE33","#0247FE", "#66B032"]

        pose = {"x":x, "y":y, "orientation":o}

        # Draw field
        drawField(fieldWidth)

        # Set robot pose
        robot.penup()
        robot.setposition(pose["x"], pose["y"])
        robot.setheading(pose["orientation"])
        robot.pendown()

        # Draw ultrasound readings lines and retrieve their distances
        front, left, back, right = ultrasounds(pose, fieldWidth, colors)


        #  flagsPos = [0.832978, 0.499645, 0.168218]

        # Work on formula here -------------------------------------------------
        pose["orientation"] = math.atan2((0.923241*fieldWidth-back),(fieldWidth*0.832978-left))
        pose["orientation"] =  math.degrees(pose["orientation"])
        print(pose["orientation"])
        # Work on formula here -------------------------------------------------

        robot.setheading(pose["orientation"])
        while 0 < robot.xcor() < fieldWidth and 0 < robot.ycor() < fieldWidth:
            robot.forward(50)

    turtle.done()


    # Your code ends here -----------------------------------------------------


if __name__ == "__main__":
    main()

