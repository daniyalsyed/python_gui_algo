from random import randrange
from time import sleep
from Tkinter import *



root = Tk()
canvas = Canvas(root, bg='white', width='800', height='400')
label1 = Label( root, text="Enter length of array : ")
E1 = Entry(root, bd =5)


iterations = 0
iter_text = canvas.create_text(100, 350, text=str("Iterations : "+str(iterations)))
ndigits = 0
digits = [0,0]
tdelta1, tdelta2 = .7, .1
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
    global digits
    global items

    digits[i], digits[i+1] = digits[i+1], digits[i]
    canvas.move(items[i], xdelta, 0)
    canvas.move(items[i+1], -xdelta, 0)
    items[i], items[i+1] = items[i+1], items[i]


def bubsort():
    print "Sort digits and animate."

    count = 1
    for stop in reversed(range(1, ndigits)):
        # stop = index of position whose entry will be determined.
        count +=1
        canvas.itemconfigure(iter_text, text=str("Iterations : "+str(count)))
        canvas.update()
        for i in range(stop):
            count +=1
            canvas.itemconfigure(iter_text, text=str("Iterations : "+str(count)))
            canvas.update()
            swap_needed = digits[i] > digits[i+1]
            color(i, swap_needed)
            if swap_needed:
                swap(i)
                color(i, False)

def start_ss():


    global ndigits 
    global digits
    global items

    ndigits = int(E1.get())
    digits = [randrange(10) for _ in range(ndigits)]

    # Create display items and pause.
    items = [canvas.create_text(xstart + xdelta*i, y, text=str(digit))
             for i, digit in enumerate(digits)]

    canvas.update()
    bubsort()


start_sort = Button(root, text ="Start ", command = start_ss)



label1.pack()
E1.pack()
start_sort.pack(side =BOTTOM)

canvas.pack()


root.mainloop()
