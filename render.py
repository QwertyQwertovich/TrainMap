#реализовано при помощи Яндекс.Расписание
from random import randint
from tkinter import *
from PIL import Image, ImageTk
api = "29a0fe51-dbc1-4d92-bcab-bb2c68daa9c9"
def qqq(event):
    print("Mouse clicked:", event.x, event.y)

class Station:
    def __init__(self, name, x, y, code):
        self.name = name
        self.x = x
        self.y = y
        self.code = code

stations = [Station("Фин", 877, 592, "038205"),
            Station("Лан", 848, 516, "037405"),
            Station("Удел", 848, 516, "037405"),
            Station("Озер", 835, 475, "038417"),
            Station("Шув", 815, 412, "038506"),
            Station("Парг", 778, 343, "038510"),
            Station("Лев", 737, 287, "038807"),
            Station("Пес", 667, 268, "038811"),
            Station("Диб", 647, 260, "038826"),
            Station("Бел", 532, 217, "039208"),
            Station("Солн", 647, 260, "039212"),
            Station("Реп", 392, 160, "039227"),
            Station("Ком", 325, 135, "039231"),
            Station("Зел", 217, 93, "039301")]
root = Tk()
width = 1000
height = 623
canvas = Canvas(root, width=width, height=height)
canvas.bind("<Button-1>", qqq)
canvas.pack()
pilImage = Image.open("b.png")
image1 = ImageTk.PhotoImage(pilImage)
canvas.create_image(0, 0, image=image1, anchor=NW)
root.mainloop()