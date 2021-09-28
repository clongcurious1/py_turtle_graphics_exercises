#modules
import turtle

#create our turtle and our window
cecil = turtle.Turtle() 
#screen color
turtle.bgcolor('black')
#make Cecil look like a turtle
cecil.shape('turtle')

#drawing colors LIST - each side of hexagon is different color
colors = ['red', 'green', 'orange', 'blue', 'yellow', 'purple']

#THIRD - repeat the inner loop and turn a set number of times
for n in range(36):
#FIRST - inner loop - create one shape and turn
    for i in range(6): #looping 6x
        cecil.color(colors[i]) #loop through each color in the list 
        cecil.forward(100) #draw 100 steps moving forward
        cecil.left(60) #turn 60 degrees to the left
#SECOND - motion to take before repeating the loop
    cecil.right(10) #turn 10 degrees to the right, then start next loop

#hexagons complete
#prepare to draw 36 circles outside the boundary of the hexagons
cecil.penup()
cecil.color('white')
#draw 36 circles to match 36 hexagons
for i in range(36):
    cecil.forward(220)
    cecil.pendown()
    cecil.circle(5)
    cecil.penup()
    cecil.backward(220)
    cecil.right(10)
#hide turtle to finish drawing
cecil.hideturtle()
