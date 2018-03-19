import turtle

'''This Code will drwaing python logo'''

#screen settings
window = turtle.Screen()
window.bgcolor("White")

#turtle Settingse
python = turtle.Turtle()
python.hideturtle()

'''Start Draw blue python '''
#color Control
python.color("#0C9DBF","#0C9DBF")
python.begin_fill()
#position Specification
python.up()
python.setpos(-150,0)
python.down()
#Move and draw
#python.speed(1)
python.forward(40)
python.left(90)
python.forward(40)
python.right(10)
for i in range(10):
    python.forward(10)
    python.right(8)
python.forward(60)
python.left(10)
for i in range(10):
    python.forward(5)
    python.left(8)
python.forward(60)
python.left(10)
for i in range(10):
    python.forward(5)
    python.left(8)

for i in range(5):
    python.forward(10)
    python.left(1)

#python.left(10)
for i in range(11):
    python.forward(5)
    python.left(8)
python.forward(40)
python.left(90)
python.forward(60)
python.right(90)
python.forward(10)
python.right(90)
python.forward(100)

python.left(10)
for i in range(15):
    python.forward(10)
    python.left(7)

python.forward(28)
python.end_fill()

#Drwa Blue python eye
#color Control
python.color("#ffffff","#ffffff")
python.begin_fill()
#position Specification
python.up()
python.setpos(-45,180)
python.down()
python.circle(10)
python.end_fill()
'''End Draw blue python '''

'''Start Draw Yellow python '''
#color Control
python.color("#F8B721","#F8B721")
python.begin_fill()
#position Specification
python.up()
python.setpos(100,145)
python.down()
python.right(117)
python.forward(40)
python.left(90)
python.forward(40)
python.right(10)
for i in range(10):
    python.forward(10)
    python.right(8)
python.forward(60)
python.left(10)
for i in range(10):
    python.forward(5)
    python.left(8)
python.forward(60)
python.left(10)
for i in range(10):
    python.forward(5)
    python.left(8)

for i in range(5):
    python.forward(10)
    python.left(1)

#python.left(10)
for i in range(11):
    python.forward(5)
    python.left(8)
python.forward(40)
python.left(90)
python.forward(60)
python.right(90)
python.forward(10)
python.right(90)
python.forward(100)
python.left(10)
for i in range(15):
    python.forward(10)
    python.left(7)

python.forward(28)
python.end_fill()

#Drwa Blue python eye
#color Control
python.color("#ffffff","#ffffff")
python.begin_fill()
#position Specification
python.up()
python.setpos(-20,-40)
python.down()
python.circle(10)
python.end_fill()
'''End Draw Yellow python '''


window.exitonclick()
