#Import modules
import turtle 

#Variables
cecil = turtle.Turtle() #create Turtle graphics screen, name our turtle
cecil.shape('turtle') #make Cecil look like a turtle

#Window settings
turtle.bgcolor('black') #screen color is now black

#List - order of colors for the hexagon
# Each side of the hexagon is a different color
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']

#Second, create outer FOR LOOP - total number of hexagons to draw
for n in range(36):
#First, inner FOR LOOP draws one hexagon, loops through colors in list
    for i in range(6):
        cecil.color(colors[i]) #use color at position i in the list
        cecil.forward(100)
        cecil.left(60)
    #Finally, code action to take after completing each hexagon
    cecil.right(10)
