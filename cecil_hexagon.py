import turtle #import module

cecil = turtle.Turtle() #create our turtle window
cecil.shape('turtle') #make Cecil look like a turtle

#fill shape with a color
cecil.begin_fill() #start filling the shape
cecil.color('purple') #use fill color purple

#use loop to make geometric pattern
#repeat 6 times - move forward, then turn
for i in range(6):
    cecil.forward(100)
    cecil.left(60)
cecil.end_fill() #stop coloring


