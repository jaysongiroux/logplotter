contents = ["""|2019-05-27T13:36:31.685Z| [LOG] Jobstream updating latest status: {"status":2,"last_status_update":{"plasticVolume":0,"printTime":172.78,"timing":{"Downloading":6.47,"DownloadComplete":0.061,"Validating":0.437,"NeedsDetails":0.014,"Detailing":0.259,"NeedsCompatibility":0.087,"CheckingCompatibility":0.079,"Uninitialized":0.009,"Initializing":0.664,"CheckingOpticalOnStart":0.007,"CheckingVacuum":0.006,"CheckingBedLevel":49.625,"Ready":0.06,"Printing":172.779,"RunningPurgeLine":0.677,"Pausing":5.526,"Paused":72699.772,"Canceling":1.591},"layer":0,"lineNumber":34,"versions":{"slicer":"v3.3.0-rc.1","matterhorn":"87b3d44","flounder":"fbb850c","agni":"deee845"},"reason":"touchscreen","runtime":{"session":"f1cb2fa2-1719-44dd-a4c9-145cd4350c39","print":7,"pause":3,"util":null}}} <logger.js:41:23>""",
            """|2019-04-04T03:21:23.511Z| [LOG] Jobstream updating latest status: {"status":1,"last_status_update":{"plasticVolume":22699.716127435007,"printTime":27220.13,"timing":{"Downloading":2.219,"DownloadComplete":0.059,"Validating":0.462,"NeedsDetails":0.014,"Detailing":0.212,"NeedsCompatibility":0.062,"CheckingCompatibility":0.038,"Uninitialized":0.005,"Initializing":0.402,"CheckingOpticalOnStart":0.007,"CheckingVacuum":0.006,"CheckingBedLevel":48.67,"Ready":0.051,"Printing":27220.129,"RunningPurgeLine":337.185,"RunningBeadScan":139.833},"layer":1250,"lineNumber":553587,"fiberLength":0,"info":{},"runtime":{"session":"7ecdf27c-88eb-4e10-88cd-3d97b0a91b9b","print":3,"pause":null,"util":null}}} <logger.js:41:23>""",
            """|2019-04-04T03:21:23.511Z| [LOG] Jobstream updating latest status: {"status":1,"last_status_update":{"plasticVolume":22699.716127435007,"printTime":27220.13,"timing":{"Downloading":2.219,"DownloadComplete":0.059,"Validating":0.462,"NeedsDetails":0.014,"Detailing":0.212,"NeedsCompatibility":0.062,"CheckingCompatibility":0.038,"Uninitialized":0.005,"Initializing":0.402,"CheckingOpticalOnStart":0.007,"CheckingVacuum":0.006,"CheckingBedLevel":48.67,"Ready":0.051,"Printing":27220.129,"RunningPurgeLine":337.185,"RunningBeadScan":139.833},"layer":1250,"lineNumber":553587,"fiberLength":0,"info":{},"runtime":{"session":"7ecdf27c-88eb-4e10-88cd-3d97b0a91b9b","print":3,"pause":null,"util":null}}} <logger.js:41:23>""",
            """|2019-06-04T20:57:56.646Z| [LOG] Raw bed readings: [[11.0, 60.0, -0.069], [33.0, 60.0, -0.0557], [55.0, 60.0, -0.0465], [77.0, 60.0, -0.029], [99.0, 60.0, -0.021], [121.0, 60.0, -0.009], [143.0, 60.0, -0.0023], [165.0, 60.0, -0.0012], [187.0, 60.0, 0.004], [209.0, 60.0, 0.0012], [231.0, 60.0, 0.0056], [253.0, 60.0, -0.004], [275.0, 60.0, -0.0177], [297.0, 60.0, -0.0437], [319.0, 60.0, -0.0674], [319.0, 95.0, -0.05], [297.0, 95.0, -0.0254], [275.0, 95.0, 0.0026], [253.0, 95.0, 0.0202], [231.0, 95.0, 0.0288], [209.0, 95.0, 0.028], [187.0, 95.0, 0.0286], [165.0, 95.0, 0.0264], [143.0, 95.0, 0.0258], [121.0, 95.0, 0.0196], [99.0, 95.0, 0.0079], [77.0, 95.0, -0.0039], [55.0, 95.0, -0.0213], [33.0, 95.0, -0.0353], [11.0, 95.0, -0.0474], [11.0, 130.0, -0.0526], [33.0, 130.0, -0.0419], [55.0, 130.0, -0.0281], [77.0, 130.0, -0.0095], [99.0, 130.0, 0.0044], [121.0, 130.0, 0.0162], [143.0, 130.0, 0.0231], [165.0, 130.0, 0.0223], [187.0, 130.0, 0.0254], [209.0, 130.0, 0.0216], [231.0, 130.0, 0.0215], [253.0, 130.0, 0.0121], [275.0, 130.0, -0.0083], [297.0, 130.0, -0.0363], [319.0, 130.0, -0.0623], [319.0, 165.0, -0.0767], [297.0, 165.0, -0.0483], [275.0, 165.0, -0.019], [253.0, 165.0, 0.0019], [231.0, 165.0, 0.0159], [209.0, 165.0, 0.016], [187.0, 165.0, 0.0204], [165.0, 165.0, 0.0181], [143.0, 165.0, 0.0193], [121.0, 165.0, 0.0129], [99.0, 165.0, 0.0008], [77.0, 165.0, -0.016], [55.0, 165.0, -0.0327], [33.0, 165.0, -0.0464], [11.0, 165.0, -0.058], [11.0, 200.0, -0.0533], [33.0, 200.0, -0.0445], [55.0, 200.0, -0.0336], [77.0, 200.0, -0.017], [99.0, 200.0, -0.0044], [121.0, 200.0, 0.0086], [143.0, 200.0, 0.014], [165.0, 200.0, 0.0105], [187.0, 200.0, 0.0121], [209.0, 200.0, 0.0077], [231.0, 200.0, 0.0064], [253.0, 200.0, -0.0057], [275.0, 200.0, -0.0232], [297.0, 200.0, -0.0546], [319.0, 200.0, -0.0789], [319.0, 235.0, -0.0747], [297.0, 235.0, -0.0486], [275.0, 235.0, -0.0209], [253.0, 235.0, -0.0011], [231.0, 235.0, 0.0088], [209.0, 235.0, 0.0047], [187.0, 235.0, 0.0115], [165.0, 235.0, 0.0116], [143.0, 235.0, 0.0165], [121.0, 235.0, 0.0137], [99.0, 235.0, 0.0047], [77.0, 235.0, -0.009], [55.0, 235.0, -0.0246], [33.0, 235.0, -0.0356], [11.0, 235.0, -0.045], [11.0, 270.0, -0.0284], [33.0, 270.0, -0.0226], [55.0, 270.0, -0.0164], [77.0, 270.0, -0.0011], [99.0, 270.0, 0.009], [121.0, 270.0, 0.0177], [143.0, 270.0, 0.0212], [165.0, 270.0, 0.0149], [187.0, 270.0, 0.0164], [209.0, 270.0, 0.0117], [231.0, 270.0, 0.0135], [253.0, 270.0, 0.0028], [275.0, 270.0, -0.0139], [297.0, 270.0, -0.0451], [319.0, 270.0, -0.0658]] <logger.js:41:23>"""]

filter = ["ERROR","WRN"]


#pretty sure contents are a 1d array, will have ot check moving forwaRD

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
    return "{} days, {} hours, {} minutes, {} seconds" .format(days[0], hours[0], minutes[0], round(minutes[1],2))


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

    print(num)
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
    a= reverse_contents(a)
    result=[]
    print("original: ",a)
    for i in range(len(a)): #0...1
        result.append([x.strip() for x in a[i].split(':')])

    print("result",result)


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

    print("shapper: ", shapper[0])
    s=shapper[0]

    a = ast.literal_eval(s)
    a = np.array(a)

    print("a",a)

    bed_leveling.graphtoolpath(a)

    return a








