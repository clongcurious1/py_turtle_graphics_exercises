#import module
import turtle

#name our turtle, create window
cecil = turtle.Turtle()
#make Cecil look like a turtle
cecil.shape('turtle')
#background screen color is black
turtle.bgcolor('black')

colors = ['white', 'red', 'yellow', 'blue']

#outerloop_draw 6 squares with space between each one
for n in range(6):      
#inner loop_draw 1 square then skip ahead before next loop
    for i in range(4):
        cecil.color(colors[i])
        cecil.forward(20)
        cecil.right(90)
#before next loop
    cecil.penup()
    cecil.forward(30)
    cecil.pendown()
    