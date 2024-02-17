from turtle import *

speed(30)
#we want to paint a house

#step 1: draw a square
width(6)
color("purple")




forward(300)
left(90)

forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(100)
color("pink")

left(90)
forward(130)    #height of the door
right(90)
forward(70)
right(90)
forward(130)
end_fill()
penup()
goto(300,200) 
pendown

color("yellow")
begin_fill()
left(220)
forward(240)
left(100)
forward(240)
end_fill()



exitonclick()