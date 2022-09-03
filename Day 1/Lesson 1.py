from turtle import *
#drawing a house
width(7)

#drawing a square

color("brown")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#drawing a door

begin_fill()
forward(70)
color("orange")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

#drawing a roof

penup()
goto(200, 200)
pendown()

begin_fill()
color("green")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

color ("brown")
left(30)
forward(70)
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
end_fill()

penup()
goto(200, 200)
pendown()
left(180)
color("brown")
forward(70)
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()




exitonclick()