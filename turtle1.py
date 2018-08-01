import turtle

finn = turtle.Turtle()
def up():
   finn.up()
def down():
   finn.down()
def left():
   finn.left()
def right():
   finn.right()
finn.onkeypress(up, "w")
finn.onkeypress(down, "s")
finn.onkeypress(left, "a")
finn.onkeypress(right, "d")
turtle.listen()
turtle.mainloop()
