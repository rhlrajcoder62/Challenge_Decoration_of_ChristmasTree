import turtle

def position(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def star(size,color):
    turtle.color(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(size)
        turtle.right(144)

    turtle.end_fill()

def light(size,color):
    turtle.color(color)
    turtle.begin_fill()

    turtle.circle(size)

    turtle.end_fill()

turtle.Screen()
turtle.setup(1000,800)
turtle.bgpic('trees.png')

# Begin editing the code below this line ------>

position(350,310)
light(40,'white')

#Diffuced light and star on ground

position(320,-345)
star(50,'white')
position(-240,-285)
light(50,'blue')
position(-150,-300)
light(20,'red')
position(-200,-365)
star(50,'cyan')



# for 1st left treeLength 

position(-316,254)
star(50,'red')

# for 2nd left tree length

position(-371,106)
light(10,'DarkOrchid')

position(-340,110)
star(30,'blue')

position(-275,107)
star(30,'green')

position(-210,110)
light(10,'yellow')


# for 3rd left tree length

position(-420,0)
star(30,'white')


position(-345,-23)
light(10,'purple')

position(-280,-30)
star(30,'skyblue')


position(-220,-21)
light(10,'green')

position(-180,-15)
star(30,'orange')


# for 4th left tree length



position(-486,-177)
star(30,'blue')

position(-420,-180)
light(10,'red')

position(-380,-177)
star(30,'magenta')

position(-320,-185)
light(10,'green')

position(-280,-177)
star(30,'yellow')

position(-200,-190)
light(10,'cyan')

position(-155,-182)
star(30,'Deeppink')

position(-112,-178)
light(10,'orange')


# # for right tree

# # 1st tree length

position(163,330)
star(100,'yellow')

# # 2nd tree length

position(100,100)
light(20,'blue')

position(170,90)
light(20,'magenta')

position(250,82)
light(20,'red')

position(320,112)
light(20,'orange')

# # 3rd tree length

position(30,-67)
star(50,'white')

position(105,-80)
star(50,'orange')

position(220,-85)
star(50,'black')

position(295,-85)
star(50,'violet')

position(365,-65)
star(50,'cyan')


# # 4th tree length

position(-34,-297)
light(20,'yellow')

position(24,-298)
light(20,'blue')


position(92,-320)
light(20,'cyan')

position(170,-320)
light(20,'magenta')

position(240,-320)
light(20,'red')

position(330,-340)
light(20,'orange')

position(417,-320)
light(20,'black')

position(469,-300)
light(20,'purple')





#Make it snow, make it snow, make it snow!
turtle.tracer(0)
turtle.addshape("snowFall.gif")
turtle.speed(0)
turtle.shape("snowFall.gif")
turtle.penup()
turtle.goto(0, 500)
turtle.right(90)


while True :
    turtle.update()
    turtle.forward(0.5)
    if turtle.ycor()<-499:
        turtle.goto(0,500)





