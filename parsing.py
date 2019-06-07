"""
filters:
    - INFO
    - WARNING
    - bed info

todo:
1. parse log for bed levling array =
2. parse log to total print time perlog aquiered
3. warning >> "WRN"
4. change the filter algorithm.
    a. current - O(n^k)
5. determine how long te printer has been printing
6. generat statistics of the printer




"""


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore
from tkinter import filedialog
import re

import searching
import bed_leveling #for some reason this fails however it still works
from mpl_toolkits.mplot3d import axes3d
from tkinter import *
bed_mesh = np.array([[11.0, 60.0, 0.1604], [33.0, 60.0, 0.1591], [55.0, 60.0, 0.1538], [77.0, 60.0, 0.1708], [99.0, 60.0, 0.1818], [121.0, 60.0, 0.1846], [143.0, 60.0, 0.1923], [165.0, 60.0, 0.1913], [187.0, 60.0, 0.1941], [209.0, 60.0, 0.2007], [231.0, 60.0, 0.21], [253.0, 60.0, 0.2183], [275.0, 60.0, 0.2109], [297.0, 60.0, 0.2041], [319.0, 60.0, 0.2095], [319.0, 95.0, 0.2069], [297.0, 95.0, 0.2086], [275.0, 95.0, 0.2192], [253.0, 95.0, 0.2321], [231.0, 95.0, 0.2293], [209.0, 95.0, 0.2208], [187.0, 95.0, 0.2176], [165.0, 95.0, 0.2137], [143.0, 95.0, 0.2146], [121.0, 95.0, 0.2053], [99.0, 95.0, 0.1996], [77.0, 95.0, 0.1906], [55.0, 95.0, 0.1743], [33.0, 95.0, 0.17], [11.0, 95.0, 0.1726], [11.0, 130.0, 0.1891], [33.0, 130.0, 0.1863], [55.0, 130.0, 0.1898], [77.0, 130.0, 0.2005], [99.0, 130.0, 0.2081], [121.0, 130.0, 0.2151], [143.0, 130.0, 0.2224], [165.0, 130.0, 0.2151], [187.0, 130.0, 0.2161], [209.0, 130.0, 0.215], [231.0, 130.0, 0.2246], [253.0, 130.0, 0.2288], [275.0, 130.0, 0.2221], [297.0, 130.0, 0.2096], [319.0, 130.0, 0.2024], [319.0, 165.0, 0.1972], [297.0, 165.0, 0.2102], [275.0, 165.0, 0.2239], [253.0, 165.0, 0.2381], [231.0, 165.0, 0.2335], [209.0, 165.0, 0.2293], [187.0, 165.0, 0.2328], [165.0, 165.0, 0.2324], [143.0, 165.0, 0.2387], [121.0, 165.0, 0.2334], [99.0, 165.0, 0.227], [77.0, 165.0, 0.2201], [55.0, 165.0, 0.2101], [33.0, 165.0, 0.2044], [11.0, 165.0, 0.2012], [11.0, 200.0, 0.2008], [33.0, 200.0, 0.1952], [55.0, 200.0, 0.1894], [77.0, 200.0, 0.1912], [99.0, 200.0, 0.1958], [121.0, 200.0, 0.2009], [143.0, 200.0, 0.2027], [165.0, 200.0, 0.1937], [187.0, 200.0, 0.1945], [209.0, 200.0, 0.1886], [231.0, 200.0, 0.1989], [253.0, 200.0, 0.2], [275.0, 200.0, 0.1868], [297.0, 200.0, 0.1742], [319.0, 200.0, 0.1624], [319.0, 235.0, 0.1535], [297.0, 235.0, 0.1644], [275.0, 235.0, 0.1739], [253.0, 235.0, 0.1923], [231.0, 235.0, 0.2007], [209.0, 235.0, 0.1972], [187.0, 235.0, 0.2032], [165.0, 235.0, 0.2], [143.0, 235.0, 0.2127], [121.0, 235.0, 0.2092], [99.0, 235.0, 0.2084], [77.0, 235.0, 0.2053], [55.0, 235.0, 0.2019], [33.0, 235.0, 0.2036], [11.0, 235.0, 0.2095], [11.0, 270.0, 0.2439], [33.0, 270.0, 0.2284], [55.0, 270.0, 0.2231], [77.0, 270.0, 0.2229], [99.0, 270.0, 0.2214], [121.0, 270.0, 0.2222], [143.0, 270.0, 0.221], [165.0, 270.0, 0.2033], [187.0, 270.0, 0.2019], [209.0, 270.0, 0.1888], [231.0, 270.0, 0.1874], [253.0, 270.0, 0.1818], [275.0, 270.0, 0.1744], [297.0, 270.0, 0.1661], [319.0, 270.0, 0.1504]])
bed_mesh = np.array([[11.0, 60.0, 0.25], [33.0, 60.0, 0.1517], [55.0, 60.0, 0.1491], [77.0, 60.0, 0.1678], [99.0, 60.0, 0.1801], [121.0, 60.0, 0.1832], [143.0, 60.0, 0.1929], [165.0, 60.0, 0.1922], [187.0, 60.0, 0.1948], [209.0, 60.0, 0.1994], [231.0, 60.0, 0.2077], [253.0, 60.0, 0.215], [275.0, 60.0, 0.2069], [297.0, 60.0, 0.1993], [319.0, 60.0, 0.2039], [319.0, 95.0, 0.2013], [297.0, 95.0, 0.25], [275.0, 95.0, 0.2148], [253.0, 95.0, 0.2282], [231.0, 95.0, 0.2259], [209.0, 95.0, 0.2181], [187.0, 95.0, 0.2155], [165.0, 95.0, 0.2115], [143.0, 95.0, 0.2131], [121.0, 95.0, 0.2042], [99.0, 95.0, 0.1979], [77.0, 95.0, 0.188], [55.0, 95.0, 0.1728], [33.0, 95.0, 0.1689], [11.0, 95.0, 0.1717], [11.0, 130.0, 0.1886], [33.0, 130.0, 0.1865], [55.0, 130.0, 0.1895], [77.0, 130.0, 0.1991], [99.0, 130.0, 0.2072], [121.0, 130.0, 0.2136], [143.0, 130.0, 0.2208], [165.0, 130.0, 0.2132], [187.0, 130.0, 0.2144], [209.0, 130.0, 0.2136], [231.0, 130.0, 0.2215], [253.0, 130.0, 0.2257], [275.0, 130.0, 0.2163], [297.0, 130.0, 0.2036], [319.0, 130.0, 0.1969], [319.0, 165.0, 0.1909], [297.0, 165.0, 0.2045], [275.0, 165.0, 0.2179], [253.0, 165.0, 0.2323], [231.0, 165.0, 0.2298], [209.0, 165.0, 0.2251], [187.0, 165.0, 0.2293], [165.0, 165.0, 0.2292], [143.0, 165.0, 0.2362], [121.0, 165.0, 0.2318], [99.0, 165.0, 0.2253], [77.0, 165.0, 0.2187], [55.0, 165.0, 0.2092], [33.0, 165.0, 0.2044], [11.0, 165.0, 0.2008], [11.0, 200.0, 0.2025], [33.0, 200.0, 0.1966], [55.0, 200.0, 0.1901], [77.0, 200.0, 0.1917], [99.0, 200.0, 0.1962], [121.0, 200.0, 0.2], [143.0, 200.0, 0.2023], [165.0, 200.0, 0.1923], [187.0, 200.0, 0.1935], [209.0, 200.0, 0.1864], [231.0, 200.0, 0.196], [253.0, 200.0, 0.1968], [275.0, 200.0, 0.1835], [297.0, 200.0, 0.1694], [319.0, 200.0, 0.1563], [319.0, 235.0, 0.149], [297.0, 235.0, 0.16], [275.0, 235.0, 0.1702], [253.0, 235.0, 0.1885], [231.0, 235.0, 0.1985], [209.0, 235.0, 0.1951], [187.0, 235.0, 0.2], [165.0, 235.0, 0.1988], [143.0, 235.0, 0.2122], [121.0, 235.0, 0.2092], [99.0, 235.0, 0.2075], [77.0, 235.0, 0.207], [55.0, 235.0, 0.2024], [33.0, 235.0, 0.2068], [11.0, 235.0, 0.2111], [11.0, 270.0, 0.247], [33.0, 270.0, 0.2312], [55.0, 270.0, 0.226], [77.0, 270.0, 0.2257], [99.0, 270.0, 0.2229], [121.0, 270.0, 0.2225], [143.0, 270.0, 0.2208], [165.0, 270.0, 0.2038], [187.0, 270.0, 0.2006], [209.0, 270.0, 0.1874], [231.0, 270.0, 0.1855], [253.0, 270.0, 0.1793], [275.0, 270.0, .25], [297.0, 270.0, 0.1623], [319.0, 270.0, 0.1457]])

#returns filtered contents
def display_filters(contents,filter):
    tempC = []
    for i in range(len(contents)):
        for a in range(len(filter)):
            if filter[a].lower() in contents[i].lower():
                # print(contents[i])
                tempC.append(contents[i])
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

def logfile(filename,bool,o="null"):
    if bool == True: #if given  filter
        with open(filename,'r') as u:
            x = u.readlines()
        return display_filters(x,o)

    else:
        with open(filename, 'r') as f:
            x = f.readlines()
        return x

def displayContents(contents):
    for i in range(len(contents)):
        print(contents[i])



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


    #could concat this into an array of string int's in the future
    w=StringVar()
    b=StringVar()
    e=StringVar()
    f=StringVar()
    l=StringVar()
    q=StringVar()

    def browse_button():
        global filename
        filename = filedialog.askopenfilename()

    def importcontents (filename):
        #if more filters are added, needs to be added to this array
        temp = [w.get(),b.get(),e.get(),e.get(),f.get(),l.get(),q.get()]
        if w.get()=="WARNING": temp.append("WRN")

        temp = [x for x in temp if x]
        print("[INFO] Filters: ",temp)

        #determines if there are filters selected
        try:
            if not temp:
                contents = logfile(filename,False,temp)
            else:
                contents = logfile(filename,True,temp)
        except:
            contents =[]

        parsed_GUI(contents)




    button2 = Button(text="Log File...", command=browse_button).grid(row=3, column=1, columnspan=2, sticky="w", )

    #check buttons
    cb1 = Checkbutton(r, text='WARNINGS', variable=w,onvalue="WARNING",offvalue="").grid(row=5, column=0)
    cb2 = Checkbutton(r, text='BED', variable=b,onvalue="bed",offvalue="").grid(row=5, column=1)
    cb3 = Checkbutton(r, text='ERRORS', variable=e, onvalue="ERROR",offvalue="").grid(row=6, column=0)
    cb4 = Checkbutton(r, text='FAILS', variable=f,onvalue="fail",offvalue="").grid(row=6, column=1)
    cb5 = Checkbutton(r, text='LEVEL OUTPUT', variable=l,onvalue="Raw",offvalue="").grid(row=7, column=0)
    cb6 = Checkbutton(r, text='PRINT TIME', variable=q,onvalue="\"printtime\":",offvalue="").grid(row=7,column=1)

    button1 = Button(r, text='Bed leveling', width=25, command=lambda : bed_leveling.graphtoolpath(bed_mesh)).grid(row=8, column=0)
    button2 = Button(r, text='Parse Log With Filters', width=25, command=lambda:importcontents(filename)).grid(row=8, column=1)



    r.mainloop()

def parsed_GUI(contents):
    root=Tk()
    #size of second window


    #label
    fontlabel = ('Helvetica', 25, 'bold')
    title_label = Label(root, text=filename + "\n Parsed log:")
    title_label.config(font=fontlabel)
    title_label.grid(row=0,column=0,sticky="news")
    print("filename: ", filename)

    # label2 = Label(root, text="Parsed Log: ")
    # label2.config(font=fontlabel)
    # label2.grid(row=0, column=1,columnspan=2,sticky="news")
    label1 = Label(root,text="statistics: ")
    label1.config(font=fontlabel)
    label1.grid(row=0, column=4,columnspan=4,sticky="news")

    #need to display filtered contents
    t = Text(root) #height =50,width=190)
    for i in range(len(contents)):
        try:
            t.insert(INSERT,">>"+contents[i])
            t.insert(INSERT,"\n")
        except:
            continue

    t.config(relief=GROOVE, borderwidth=2)
    t.grid(row=1, column=0, columnspan=4, sticky="news")
    time = Text(root,relief=GROOVE,borderwidth=2)
    string1 = "printing time: " + str(searching.printtime(contents))+ " Hours"
    time.insert(INSERT,string1)
    time.grid(row=1,column=4,columnspan=4,stick="n")


GUI()




