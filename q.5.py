import turtle

def draw_square(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    
turtle.speed(1) 

size = int(input("Size of the square:"))
color = input("Color of the square:")

draw_square(size, color)

turtle.mainloop()
