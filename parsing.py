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
    a. print time

** make compatible for 2.7
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
filename = ""




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


#returns contents of the file. filename = filename + path, bool = if there is a filter or not, o = whats being filtered for
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

def remove_spaces(a):
    a = [i for i in a if i]
    return str(a)





"""
todo:
- allow users to chose their own filters seperated by commas
- stores all bed leveling data and allows the user to choose bed leveling data based on time stamp

bugs:
- when clicking "bed levling" it opens a file dialog behind the bed stats page

"""
filters=[]
def GUI():

    def browse_button():
        global filename
        filename = filedialog.askopenfilename()

    def importcontents (filename):
        global filters
        #if more filters are added, needs to be added to this array
        temp = [w.get(),b.get(),e.get(),e.get(),f.get(),l.get(),q.get()] #pulling chosen filters
        custom = entry1.get()
        cusomArray = custom.split(',')
        for i in range(len(cusomArray)):temp.append(cusomArray[i])

        if w.get()=="WARNING": temp.append("WRN")

        #global filters array for stats
        for i in range(len(temp)): filters.append(temp[i])

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
    entry1 = StringVar()


    button2 = Button(text="Log File...", command=lambda:browse_button()).grid(row=3, column=1, columnspan=2, sticky="w", )

    #check buttons
    cb1 = Checkbutton(r, text='"WARNINGS', variable=w,onvalue="WARNING",offvalue="").grid(row=5, column=0)
    cb2 = Checkbutton(r, text='BED', variable=b,onvalue="bed",offvalue="").grid(row=5, column=1)
    cb3 = Checkbutton(r, text='ERRORS', variable=e, onvalue="ERROR",offvalue="").grid(row=6, column=0)
    cb4 = Checkbutton(r, text='FAILS', variable=f,onvalue="fail",offvalue="").grid(row=6, column=1)
    cb5 = Checkbutton(r, text='LEVEL OUTPUT', variable=l,onvalue="Raw",offvalue="").grid(row=7, column=0)
    cb6 = Checkbutton(r, text='PRINT TIME', variable=q,onvalue="\"printtime\":",offvalue="").grid(row=7,column=1)


    #custom entry row 8
    custom_label = Label(text="Custom Filter (EX:fail,WARN,bed...):").grid(row=8,column=0,sticky="e",pady=(0,15))
    custom_entry = Entry(r, text="Custom filters seperated by commas. Ex: fail,WARN,bed,laser",width=25,textvariable=entry1).grid(row=8,column=1,sticky="w",pady=(0,15))

    # button1 = Button(r, text='Bed leveling', width=25, command=lambda : bed_leveling.graphtoolpath(bed_mesh)).grid(row=8, column=0)
    button1 = Button(r, text='Bed leveling', width=25, command=lambda:searching.stip_bed_values(logfile(filename,False))).grid(row=9, column=0) #array of contents from get_contents
    button2 = Button(r, text='Parse Log With Filters', width=25, command=lambda:importcontents(filename)).grid(row=9, column=1)



    r.mainloop()



    """
    2D plot of the bed of the high and low points along with the 3D projection
    """
def parsed_GUI(contents):
    root=Tk()


    #label
    fontlabel = ('Helvetica', 25, 'bold')
    title_label = Label(root, text=filename + "\n Parsed log:")
    title_label.config(font=fontlabel)
    title_label.grid(row=0,column=0,sticky="news")
    # print("filename: ", filename)

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
    string2 = "\nFilters: " + remove_spaces(filters)
    time.insert(INSERT,string2)

GUI()




