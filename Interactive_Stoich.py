# github password
# cho6=Y_QuP&ipUc#L5+n
import tkinter as tk
import re
import time
import random
import Periodic_Table as PT
import Stoich_Equations as SE


## Menu with Buttons
# def FuncCall(option):
#   if option == 1:
#     SE.Stoich("MassVol",3)
#
# def Cons(event):
#   Single = tk.Button(win, text = "Single Element", command = FuncCall(1))
#   Compound = tk.Button(win, text = "Compound")
#   Other = tk.Button(win, text = "Volume of something else")
#   Single.grid(column = 0, row = 2)
#   Compound.grid(column = 1, row = 2)
#   Other.grid(column = 2, row = 2)
#
# def MassCons(event):
#   Vol.grid_remove()
#   Part.grid_remove()
#   Mass2Vol = tk.Button(win, text = "Going to Volume")
#   Mass2Part = tk.Button(win, text = "Going to Particles")
#   Mass2Mol = tk.Button(win, text = "Going to Moles")
#   Mass2Vol.grid(column = 0, row = 1)
#   Mass2Part.grid(column = 1, row = 1)
#   Mass2Mol.grid(column = 2, row = 1)
#   Mass2Vol.bind("<Button-1>",Cons)
#
# def VolCons(event):
#   Mass.grid_remove()
#   Part.grid_remove()
#   pass
#
# def PartCons(event):
#   Vol.grid_remove()
#   Mass.grid_remove()
#   pass
#
# win = tk.Tk()
# win.title("Interactive stoichiometry")
# win.geometry("600x400")
# Mass = tk.Button(win, text = "Starting with Mass",)
# Vol = tk.Button(win, text = "Starting with Volume")
# Part = tk.Button(win, text = "Starting with Particles")
# Mass.grid(column = 0, row = 0)
# Vol.grid(column = 1, row = 0)
# Part.grid(column = 2,row = 0)
# Mass.bind("<Button-1>",MassCons)
# Vol.bind("<Button-1>",VolCons)
# Part.bind("<Button-1>",PartCons)
# win.mainloop()

## Drop Down menu attempt

def button_conversion(Con1, Con2, Con3, Con4):  # convert options into conversion type in the SE.Stoichfunction
    if Con2 == "Starting Mass":

        if Con3 == "Going to Volume":  ##########

            if Con1 == "Element":

                if Con4 == "Same Element":
                    return 1

                elif Con4 == "Different Element":
                    return 3

                elif Con4 == "Different Compound":
                    return 4
                else:
                    print("INVALID RESPONSE")
                    return

            elif Con1 == "Compound":

                if Con4 == "Same Compound":
                    return 2

                elif Con4 == "Different Compound":
                    return 5

                elif Con4 == "Different Element":
                    return 6
                else:
                    print("INVALID RESPONSE")
                    return

        elif Con3 == "Going to Mass":  ##########

            if Con1 == "Element":

                if Con4 == "Different Element":
                    return 7
                elif Con4 == "Different Compound":
                    return 8
                else:
                    print("INVALID RESPONSE")
                    return

            elif Con1 == "Compound":

                if Con4 == "Different Element":
                    return 9
                elif Con4 == "Different Compound":
                    return 10
                else:
                    print("INVALID RESPONSE")
                    return

        elif Con3 == "Going to Particles":  ##########
            if Con1 == "Element":

                if Con4 == "Same Element":
                    return 11
                elif Con4 == "Different Element":
                    return 13
                elif Con4 == "Different Compound":
                    return 14
                else:
                    print("INVALID RESPONSE")
                    return

            elif Con1 == "Compound":

                if Con4 == "Same Compound":
                    return 12
                elif Con4 == "Different Element":
                    return 15
                elif Con4 == "Different Compound":
                    return 16
                else:
                    print("INVALID RESPONSE")
                    return


def screen_control():  # testing to see if tk.button() functions and gets correct data
    startSub.delete(0, tk.END)
    startVal.delete(0, tk.END)
    endSub.delete(0, tk.END)

    startSub.insert(0, "Enter " + first.get())
    startVal.insert(0, "Enter " + second.get())
    if fourth.get() in ["Same Element", "Same Compound"]:
        endSub.insert(0, "N/A")
    else:
        endSub.insert(0, "Enter " + fourth.get())

    startSub.pack()
    startVal.pack()
    endSub.pack()
    button2.pack()
    startSub.place(x=175, y=0)
    startVal.place(x=175, y=30)
    endSub.place(x=175, y=90)
    button2.place(x=210, y=120)


def split(word):
    return [char for char in word]


def compound_elements(list):
    Elements = []
    Subscripts = []
    index = []
    remove = []
    if list[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        list.pop(0)
    for x in range(len(list)):
        if list[x] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            index.append(x)
            Subscripts.append(list[x])
        elif (len(list)-x) > 1:
            if (list[x].isupper()) & (list[x+1].islower()):
                fLetter = list[x]
                sLetter = list[x+1]
                ele = fLetter + sLetter
                Elements.append(ele)
            else:
                Elements.append(list[x])
        else:
            Elements.append(list[x])

    for x in range(len(Elements)):
        if Elements[x].islower():
            remove.append(Elements[x])
    for x in range(len(remove)):
        Elements.remove(remove[x])
    return [Elements, Subscripts, index]


def call_stoich():
    Con1 = first.get()
    Con2 = second.get()
    Con3 = third.get()
    Con4 = fourth.get()
    x = split(startSub.get())
    y = split(endSub.get())
    index = []
    index2 = []
    coefficient = [1]
    coefficient2 = [1]
    if Con1 == "Element": # for the first element/compound
        if x[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            coefficient = [int(x[0])]
        Substance = startSub.get()
        if x[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            subscript = [int(x[-1])]
        else:
            subscript = 1
        SubstanceGrams = float(startVal.get())
    elif Con1 == "Compound":
        if x[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            coefficient = [int(x[0])]
        Substance = startSub.get()
    SubstanceGrams = float(startVal.get())
    Substance = compound_elements(x)
    subscript = Substance[1]
    index = Substance[2]
    if len(subscript) == 0:
        subscript.append(1)

    if Con4 == "Different Element": # for the second element/compound
        if y[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            coefficient2 = [int(x[0])]
        Substance2 = endSub.get()
        if y[-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            subscript2 = [int(y[-1])]
        else:
            subscript2 = 1
    elif Con4 == "Different Compound":
        if y[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            coefficient2 = [int(y[0])]
        Substance2 = endSub.get()
    SubstanceGrams = float(startVal.get())

    Substance = compound_elements(x)
    subscript = Substance[1]
    index = Substance[2]

    Substance2 = compound_elements(y)
    subscript2 = Substance2[1]
    index2 = Substance2[2]

    if len(subscript) == 0:
        subscript.append(1)
    if len(subscript2) == 0:
        subscript2.append(1)
    Answer = SE.Stoich(Con2, button_conversion(Con1, Con2, Con3, Con4), Substance[0], SubstanceGrams, coefficient, subscript,
                  index, Substance2[0], coefficient2, subscript2, index2)
    if Con4 == "Same Element" or Con4 == "Same Compound":
        Sub = startSub.get()
    else:
        Sub = endSub.get()

    output(Answer[0], Answer[1], Sub)

def output(Answer, Contype, Substance):
    if Contype == 1:  # ending in weight
        text = ("You have " + str(Answer) + " grams of " + Substance)
    elif Contype == 2:  # ending in liters
        text = ("You have " + str(Answer) + " liters of " + Substance)
    elif Contype == 3:  # ending in particles
        text = ("You have " + format(Answer, ".3E") + " particles of " + Substance)
    else:  # ending in moles
        text = ("You have " + str(Answer) + " moles of " + Substance)
    label = tk.Label(text=text)
    label.pack()
    label.place(x=15, y=150)

Options1 = ["Element", "Compound"]
Options2 = ["Starting Mass", "Starting Volume", "Starting Particles"]
Options3 = ["Going to Mass", "Going to Volume", "Going to Particles"]
Options4 = ["Same Element", "Same Compound", "Different Element", "Different Compound"]

win = tk.Tk()
win.geometry("400x400")

startSub = tk.Entry(win)

startVal = tk.Entry(win)

endSub = tk.Entry(win)
first = tk.StringVar(win)
first.set(Options1[0])

second = tk.StringVar(win)
second.set(Options2[0])

third = tk.StringVar(win)
third.set(Options3[0])

fourth = tk.StringVar(win)
fourth.set(Options4[0])

fir = tk.OptionMenu(win, first, *Options1)
sec = tk.OptionMenu(win, second, *Options2)
thi = tk.OptionMenu(win, third, *Options3)
fou = tk.OptionMenu(win, fourth, *Options4)

fir.pack()
sec.pack()
thi.pack()
fou.pack()
fir.place(x=15, y=0)
sec.place(x=0, y=30)
thi.place(x=0, y=60)
fou.place(x=0, y=90)

button = tk.Button(win, text="okay", command=screen_control)
button.pack()
button2 = tk.Button(win, text="Run", command=call_stoich)
button.place(x=35, y=120)
win.mainloop()
