import turtle

#create the turtle graphics window
#cecil is our turtle name
cecil = turtle.Turtle()

#make your turtle look like a turtle
cecil.shape('turtle')

#red square
cecil.begin_fill() #start filling the shape
cecil. color('red') #use color red

for i in range(4):
    cecil.forward(100)
    cecil.left(90)
cecil.end_fill() #stop filling the shape


