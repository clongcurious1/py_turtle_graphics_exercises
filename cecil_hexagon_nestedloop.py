import turtle #import module

#add variable
cecil = turtle.Turtle() #name our turtle Cecil
cecil.shape('turtle') #make Cecil look like a turtle

#nested loop - create single shape (inner loop) first
#outer loop - repeat hexagon 36x, each time turning 10 degrees to the right
for n in range (36):
#inner loop - create one hexagon
    for i in range(6):
        cecil.forward(100)
        cecil.left(60)
#turn right 10 degrees before repeating the loop
    cecil.right(10)