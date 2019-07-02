
"""
the display filters method in parsing.py will return the filtered content.
this method will have to take that content and strip it up into specific numbers from the print time

first try will be by splitting it up with commas


"""

import numpy as np
import bed_leveling
import ast
from datetime import datetime, timedelta

def sectoday(q):
    days = divmod(q, 86400)
    hours = divmod(days[1], 3600)
    minutes = divmod(hours[1], 60)
    return "{} days, {} hours\n{} minutes, {} seconds" .format(days[0], hours[0], minutes[0], round(minutes[1],2))


def printtime(a): #a = contents to be search, f=array of filtered words
    #this will be determining print time for the printer given the logs
    result=[]
    for i in range(len(a)): #0...1
        result.append([x.strip() for x in a[i].split(',')])

    final=[]
    for i in range(len(result)):
        for p in range(len(result[i])):
            # print(result[i][p])
            if result[i][p].find("\"printTime\":")>=0:
                final.append(result[i][p])

    #print seperated by ":"
    num = []
    for i in range(len(final)):
        num.append([x.strip() for x in final[i].split(':')])

    #print(num)
    times=[]
    #reshaping the 2d array into a 1D array without the first element
    for i in range(len(num)):
        times.append(num[i][1])
        # print("times",times)


    floatTimes = []
    for i in range(len(times)):
        floatTimes.append([x.strip() for x in times[i].split(' ')])

    floatTimes=np.array(floatTimes).astype(np.float)
    summ = np.sum(floatTimes)

    return sectoday(summ)
    #
    # return hours




"""
How does this handle log files with multiple sets of datapoints?
    - designed: take the last datapoints published to the logfile and use them in the 
    - its currently grabbing the first array in the log file
        -> FIX: now takes the most recent dataset however should be made more efficient
    
    work flow >> analyze >> chose which raw data to use >> graphs
    work flow >> grabs last raw bed data >> displays
    
"""
def reverse_contents(a): #this method is used for flipping the array of information for raw bed levling
    b= np.flip(a)
    return b

def stip_bed_values(a):
    a=reverse_contents(a)
    result=[]

    for i in range(len(a)): #0...1
        result.append([x.strip() for x in a[i].split(':')])

    #print("result",result)


    final =[]

    for i in range(len(result)):
        for p in range(len(result[i])):
            if result[i][p].find("Raw bed readings")>=0:
                final.append(result[i][p+1])
    logger=[]
    for i in range(len(final)):
        logger.append([x.strip() for x in final[i].split('<')])

    shapper = []
    # reshaping the 2d array into a 1D array without the first element
    for i in range(len(logger)):
        shapper.append(logger[i][0])


    #print("shapper: ", shapper[0])
    s=shapper[0]

    a = ast.literal_eval(s)
    a = np.array(a)

    print("a",a)

    bed_leveling.graphtoolpath(a)

    return a








