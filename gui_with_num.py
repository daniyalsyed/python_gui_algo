from random import randrange
from time import sleep
import Tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, bg='white', width='800', height='400')
canvas.pack()

ndigits = 10
digits = [randrange(10) for _ in range(ndigits)]
tdelta1, tdelta2 = .8, .2
xstart = 300
xdelta = 25
y = 80

def color(i, swap):
    "Temporarily color digits i and i+i according to swap needed."
    x = xstart + xdelta * i
    dcolor = 'Red' if swap else 'green'
    canvas.itemconfigure(items[i], fill=dcolor)
    canvas.itemconfigure(items[i+1],fill=dcolor)
    canvas.update()
    sleep(tdelta1)
    canvas.itemconfigure(items[i], fill='Black')
    canvas.itemconfigure(items[i+1], fill='Black')
    canvas.update()
    sleep(tdelta2)

def swap(i):
    digits[i], digits[i+1] = digits[i+1], digits[i]
    canvas.move(items[i], xdelta, 0)
    canvas.move(items[i+1], -xdelta, 0)
    items[i], items[i+1] = items[i+1], items[i]


def bubsort():
    "Sort digits and animate."
    for stop in reversed(range(1, ndigits)):
        # stop = index of position whose entry will be determined.
        for i in range(stop):
            swap_needed = digits[i] > digits[i+1]
            color(i, swap_needed)
            if swap_needed:
                swap(i)
                color(i, False)

# Create display items and pause.
items = [canvas.create_text(xstart + xdelta*i, y, text=str(digit))
         for i, digit in enumerate(digits)]
canvas.update()
sleep(tdelta1)

bubsort()
