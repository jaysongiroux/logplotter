"""
filters:
    - INFO
    - WARNING
    - bed info

todo:
1. parse log for bed levling array =




"""


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore
from tkinter import filedialog

import bed_leveling #for some reason this fails however it still works
from mpl_toolkits.mplot3d import axes3d
from tkinter import *
filter = ["","","","",""]  #need a better way of doing this
bed_mesh = np.array([[11.0, 60.0, 0.1604], [33.0, 60.0, 0.1591], [55.0, 60.0, 0.1538], [77.0, 60.0, 0.1708], [99.0, 60.0, 0.1818], [121.0, 60.0, 0.1846], [143.0, 60.0, 0.1923], [165.0, 60.0, 0.1913], [187.0, 60.0, 0.1941], [209.0, 60.0, 0.2007], [231.0, 60.0, 0.21], [253.0, 60.0, 0.2183], [275.0, 60.0, 0.2109], [297.0, 60.0, 0.2041], [319.0, 60.0, 0.2095], [319.0, 95.0, 0.2069], [297.0, 95.0, 0.2086], [275.0, 95.0, 0.2192], [253.0, 95.0, 0.2321], [231.0, 95.0, 0.2293], [209.0, 95.0, 0.2208], [187.0, 95.0, 0.2176], [165.0, 95.0, 0.2137], [143.0, 95.0, 0.2146], [121.0, 95.0, 0.2053], [99.0, 95.0, 0.1996], [77.0, 95.0, 0.1906], [55.0, 95.0, 0.1743], [33.0, 95.0, 0.17], [11.0, 95.0, 0.1726], [11.0, 130.0, 0.1891], [33.0, 130.0, 0.1863], [55.0, 130.0, 0.1898], [77.0, 130.0, 0.2005], [99.0, 130.0, 0.2081], [121.0, 130.0, 0.2151], [143.0, 130.0, 0.2224], [165.0, 130.0, 0.2151], [187.0, 130.0, 0.2161], [209.0, 130.0, 0.215], [231.0, 130.0, 0.2246], [253.0, 130.0, 0.2288], [275.0, 130.0, 0.2221], [297.0, 130.0, 0.2096], [319.0, 130.0, 0.2024], [319.0, 165.0, 0.1972], [297.0, 165.0, 0.2102], [275.0, 165.0, 0.2239], [253.0, 165.0, 0.2381], [231.0, 165.0, 0.2335], [209.0, 165.0, 0.2293], [187.0, 165.0, 0.2328], [165.0, 165.0, 0.2324], [143.0, 165.0, 0.2387], [121.0, 165.0, 0.2334], [99.0, 165.0, 0.227], [77.0, 165.0, 0.2201], [55.0, 165.0, 0.2101], [33.0, 165.0, 0.2044], [11.0, 165.0, 0.2012], [11.0, 200.0, 0.2008], [33.0, 200.0, 0.1952], [55.0, 200.0, 0.1894], [77.0, 200.0, 0.1912], [99.0, 200.0, 0.1958], [121.0, 200.0, 0.2009], [143.0, 200.0, 0.2027], [165.0, 200.0, 0.1937], [187.0, 200.0, 0.1945], [209.0, 200.0, 0.1886], [231.0, 200.0, 0.1989], [253.0, 200.0, 0.2], [275.0, 200.0, 0.1868], [297.0, 200.0, 0.1742], [319.0, 200.0, 0.1624], [319.0, 235.0, 0.1535], [297.0, 235.0, 0.1644], [275.0, 235.0, 0.1739], [253.0, 235.0, 0.1923], [231.0, 235.0, 0.2007], [209.0, 235.0, 0.1972], [187.0, 235.0, 0.2032], [165.0, 235.0, 0.2], [143.0, 235.0, 0.2127], [121.0, 235.0, 0.2092], [99.0, 235.0, 0.2084], [77.0, 235.0, 0.2053], [55.0, 235.0, 0.2019], [33.0, 235.0, 0.2036], [11.0, 235.0, 0.2095], [11.0, 270.0, 0.2439], [33.0, 270.0, 0.2284], [55.0, 270.0, 0.2231], [77.0, 270.0, 0.2229], [99.0, 270.0, 0.2214], [121.0, 270.0, 0.2222], [143.0, 270.0, 0.221], [165.0, 270.0, 0.2033], [187.0, 270.0, 0.2019], [209.0, 270.0, 0.1888], [231.0, 270.0, 0.1874], [253.0, 270.0, 0.1818], [275.0, 270.0, 0.1744], [297.0, 270.0, 0.1661], [319.0, 270.0, 0.1504]])


#returns filtered contents
def display_filters(contents):
    tempC = []
    for i in range(len(contents)):
        for a in range(len(filter)):
            if filter[a] in contents[i]:
                # print(contents[i])
                tempC.append(contents[i])
            elif "ABCXYZ" in contents[i]:
                continue
            else: continue
    return tempC


def x_data(data):
    tempX =  [i[0] for i in data]
    return tempX


def y_data(data):
    tempY = [i[1] for i in data]
    return  tempY


def z_data(data):
    tempz = [i[2] for i in data]
    return tempz

def logfile(filename):
    with open(filename, 'r') as f:
        x = f.readlines()
    return x

def displayContents(contents):
    for i in range(len(contents)):
        print(contents[i])

def set_filters(a,b,c,d,e):
    global filters
    if a==0: filter[0]="ABCXYZ"
    if a==1: filter[0]="WARNING"
    if b==0: filter[1]="ABCXYZ"
    if b==1: filter[1]="bed"
    if c==1: filter[2]="ERROR"
    if c==0: filter[2]="ABCXYZ"
    if d==0: filter[3]="ABCXYZ"
    if d==1: filter[3]="fail"
    if e==0: filter[4]="ABCXYZ"
    if e==1: filter[4]="Raw"



filename = ""


def GUI():
    print(Fore.WHITE + "[INFO] Starting...")

    r = Tk()
    r.geometry('500x400')
    labelfont = ('Helvetica', 20, 'bold')
    r.title('Log Utility')
    title = Label(r, text="Parsing Logs & Bed Levling utility")
    title.config(font=labelfont)
    title.grid(row=0, column=0, columnspan=2, sticky="n", pady=(5, 15))

    w= IntVar()
    b=IntVar()
    e = IntVar()
    f=IntVar()
    l=IntVar()

    def set_textbox():
        print("setting")


    def browse_button():
        global filename
        filename = filedialog.askopenfilename()

    def importcontents (filename):
        #check boxes var's
        tempW = w.get()
        tempB = b.get()
        tempE = e.get()
        tempF = f.get()
        tempL= l.get()
        print(tempW,tempB,tempE,tempF,tempL)
        set_filters(tempW,tempB,tempE,tempF,tempL)
        print(filter)
        # set_filters()
        contents = logfile(filename)
        displayContents(display_filters(contents))
        parsed_GUI(display_filters(contents))



#var.get for checkbutton

    button2 = Button(text="Log File...", command=browse_button).grid(row=3, column=1, columnspan=2, sticky="w", )

    cb1 = Checkbutton(r, text='WARNINGS', variable=w).grid(row=5, column=0)
    cb2 = Checkbutton(r, text='BED', variable=b).grid(row=5, column=1)
    cb3 = Checkbutton(r, text='ERRORS', variable=e).grid(row=6, column=0)
    cb4 = Checkbutton(r, text='FAILS', variable=f).grid(row=6, column=1)
    cb5 = Checkbutton(r, text='LEVEL OUTPUT', variable=l).grid(row=7, column=1)


    button1 = Button(r, text='Bed leveling', width=25, command=lambda : bed_leveling.graphtoolpath(bed_mesh)).grid(row=8, column=0)
    button2 = Button(r, text='Parse Log With Filters', width=25, command=lambda:importcontents(filename)).grid(row=8, column=1)



    r.mainloop()

def parsed_GUI(contents):
    root=Tk()
    root.geometry('700x400')

    #label
    fontlabel = ('Helvetica', 15, 'bold')
    label2 = Label(root, text="Parsed Log: ")
    label2.config(font=fontlabel)
    label2.grid(row=0, column=0,columnspan=2,sticky="n")


    #need to display filtered contents
    t = Text(root,height =50,width=190)
    for i in range(len(contents)):
        try:
            t.insert(INSERT,">>"+contents[i])
            t.insert(INSERT,"\n")
        except:
            continue

    t.grid(row=1,column=0,columnspan=2,sticky="n")

GUI()




