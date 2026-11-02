import tkinter
root = tkinter.Tk()
root.resizable(False, False)
myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)
shape1 = myCanvas.create_rectangle(20, 20, 100, 100, fill="blue")
xx =yy = 3
shape2 = myCanvas.create_oval(400, 300, 480, 380, fill="red")
xx2, yy2 = -4, 3
#initialize the constants xx, yy
def hay_colision(a, b):
    ax1, ay1, ax2, ay2 = myCanvas.bbox(a)
    bx1, by1, bx2, by2 = myCanvas.bbox(b)
    return ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1
def move_shape():
    global xx, yy, xx2, yy2

    myCanvas.move(shape1, xx, yy)
    myCanvas.move(shape2, xx2, yy2)

    (x1, y1, x2, y2) = myCanvas.bbox(shape1)
    if x1 <= 0 or x2 >= 800:
        xx = -xx
    if y1 <= 0 or y2 >= 600:
        yy = -yy


    (a1, b1, a2, b2) = myCanvas.bbox(shape2)
    if a1 <= 0 or a2 >= 800:
        xx2 = -xx2
    if b1 <= 0 or b2 >= 600:
        yy2 = -yy2


    if hay_colision(shape1, shape2):
        myCanvas.create_text(400, 300, text="GAME OVER",
                             font=("Arial", 40, "bold"), fill="black")
        return   # al hacer return NO se vuelve a llamar a after(), y todo se detiene

    myCanvas.after(30, move_shape)
"""def move_shape():
    global xx, yy
    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, xx, yy)
    myCanvas.move(shape2, xx2, yy2)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xx = -xx
    if y1 <= 0 or y2 >= 600:
        yy = -yy
    #call the function recursively
    myCanvas.after(30, move_shape)"""


#in the main program call the function move_shape()
myCanvas.after(10,move_shape())
myCanvas.pack()
root.mainloop()