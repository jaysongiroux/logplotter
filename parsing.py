"""
todo:
6. generat statistics of the printer
    a. print time (X)
8. needs to be better at looking for bed leveling data. always takes way too long.

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
            tempcontent =[]
            numOfFilters = len(o)
            for line in u:
                for i in range(numOfFilters):
                    if o[i].lower() in line.lower():
                        # print(o[i])
                        tempcontent.append(line)
                    else: continue
            # without applying any filters, a log file is dumped into X
        u.close() #new to manage memory
        return tempcontent
    #this is when there is no filters
    else:
        with open(filename, 'r') as f:

            x = f.readlines()
        f.close() #new to manage memory
        return x

# def displayContents(contents):
#     for i in range(len(contents)):
#         print(contents[i])

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
        temp = [w.get(),b.get(),e.get(),e.get(),f.get(),l.get(),q.get(),p.get()] #pulling chosen filters
        custom = entry1.get() #custom filters
        cusomArray = custom.split(',') #splittinf for multiple filters

        #adding custom filter
        for i in range(len(cusomArray)):
            temp.append(cusomArray[i])

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
    # r.geometry('500x400')
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
    p=StringVar()

    bedLevelFilter = ["Raw bed readings"]

    entry1 = StringVar()


    button2 = Button(text="Log File...", command=lambda:browse_button()).grid(row=3, column=0, columnspan=2, sticky="ew",padx=(5,5))

    #check buttons
    cb1 = Checkbutton(r, text='"WARNINGS', variable=w,onvalue="WARNING",offvalue="").grid(row=5, column=0,sticky="w")
    cb2 = Checkbutton(r, text='BED', variable=b,onvalue="bed",offvalue="").grid(row=5, column=1,sticky="w")
    cb3 = Checkbutton(r, text='ERRORS', variable=e, onvalue="ERROR",offvalue="").grid(row=6, column=0,sticky="w")
    cb4 = Checkbutton(r, text='FAILS', variable=f,onvalue="fail",offvalue="").grid(row=6, column=1,sticky="w")
    cb5 = Checkbutton(r, text='LEVEL OUTPUT', variable=l,onvalue="Raw",offvalue="").grid(row=7, column=0,sticky="w")
    cb6 = Checkbutton(r, text='PRINT TIME', variable=q,onvalue="\"printTime\":",offvalue="").grid(row=7,column=1,sticky="w")
    cb7 = Checkbutton(r, text='Print Job initialization', variable=p,onvalue="Print Job initialization",offvalue="").grid(row=8,column=0,sticky="w")

    #custom entry row 8
    custom_label = Label(text="Custom Filter (EX:fail,WARN,bed...):").grid(row=9,column=0,sticky="e",pady=(0,15))
    custom_entry = Entry(r, text="Custom filters seperated by commas. Ex: fail,WARN,bed,laser",width=25,textvariable=entry1).grid(row=9,column=1,sticky="w",pady=(0,15))

    # button1 = Button(r, text='Bed leveling', width=25, command=lambda : bed_leveling.graphtoolpath(bed_mesh)).grid(row=8, column=0)
    button1 = Button(r, text='Bed leveling', width=25, command=lambda:searching.stip_bed_values(logfile(filename,True,bedLevelFilter))).grid(row=10, column=0) #array of contents from get_contents
    button2 = Button(r, text='Parse Log With Filters', width=25, command=lambda:importcontents(filename)).grid(row=10, column=1)

    def quickInfo(filename):
        tempa = ["\"printTime\":"]
        a = logfile(filename,True, tempa)
        abc = searching.printtime(a)
        printTimeLabelInfo = Label(r, text=abc).grid(row=12, column=1, sticky="news", pady=(5, 5))

    #include information below the buttons to submit.
    QuickInfoButton = Button(r,text="Quick Info", width=25, command=lambda:quickInfo(filename)).grid(row=11,column=0,sticky="news",pady=(15,0),columnspan=2)
    printtimeLabel = Label(r,text='Print Time: ').grid(row=12,column=0,sticky="news",pady=(5,5))
    r.mainloop()

def parsed_GUI(contents):
    root=Tk()

    fontlabel = ('Helvetica', 25, 'bold')
    title_label = Label(root, text=filename + "\n Parsed log:")
    title_label.config(font=fontlabel)
    title_label.grid(row=0,column=0,sticky="news")
    label1 = Label(root,text="statistics: ")
    label1.config(font=fontlabel)
    label1.grid(row=0, column=4,columnspan=4,sticky="news")

    #need to display filtered contents
    t = Text(root) #height =100,width=190)
    for i in range(len(contents)):
        try:
            t.insert(INSERT,">>"+contents[i])
            t.insert(INSERT,"\n")
        except:
            continue

    t.config(relief=GROOVE, borderwidth=2,height=75)
    t.grid(row=1, column=0, columnspan=4, sticky="news")
    time = Text(root,relief=GROOVE,borderwidth=2,height=75)
    string1 = "printing time: " + str(searching.printtime(contents))+ " Hours"
    time.insert(INSERT,string1)
    time.grid(row=1,column=4,columnspan=4,stick="n")
    string2 = "\nFilters: " + remove_spaces(filters)
    time.insert(INSERT,string2)

GUI()





