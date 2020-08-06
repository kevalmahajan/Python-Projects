'''
This is the solution to the code-a-thon question
The problem statement is 
Code-a-thon Question
Schedulers and File handling
Read all the files in a specific folder and store in JSON Format with Date created, Date Modified ,File Name , File Extension and File Size.
Create a scheduler that scans the folder every 1 min and adds any new files to the JSON File. 
'''


import json #to work with or to convert into json data
import os # to interact with operating system
import os.path
import time # to excess time
import sys # to excess the variables used by interpreter
from datetime import datetime # to get date and time

# format_bytes==> function to convert file size from bytes to kb,mb,gb and tb
def format_bytes(size):
    # 2**10 = 1024
    power = 2**10
    n = 0
    pl = {0 : '', 1: 'k', 2: 'm', 3: 'g', 4: 't'}
    while size > power:
        size /= power
        n += 1
    s='%f %sb' %(size,pl[n]) 
    return s


''' file_details ==> function to get info such as file name, 
    file extensions,file size,
    last modified datetime and created datetime
'''
def file_details(name):
    path='E:/'+name   # adding path + the file from the path
    
    last_m=("Last modified: %s" % time.ctime(os.path.getmtime(path))) #using os module to get last modified time
    
    last_c=("Created: %s" % time.ctime(os.path.getctime(path))) #using os module to get file creation time
    
    statinfo = os.stat(path)   #os.stat returns stats of the file
    size= "File Size : %s" %format_bytes(statinfo.st_size)  #extracting size from the stats 
    #statinfo.st_size returns size of the file in bytes
    ex=name.split(".")
#    print(ex[-1])
    ext = "File Extension : .%s" %ex[-1]    #spilting the name of the file by dot
    return name,last_c,last_m,ext,size


try:
    while True:
        f = open("FileDetails.txt", "a+")   #open a text file for the info to be saved
        entries = os.listdir('E:/')         #change the path of which the file details are required
        details=[]
        for i in range(0,len(entries)):
            a=file_details(entries[i])
            details.append(a)
            
        json_conv=json.dumps(details,indent=4)   #conversion of list to json 
        print(json_conv)
        
        # writing the detials collected to the text file 
        f.write(json_conv)
        print()
        print(datetime.now().strftime('Last checked time - %H:%M:%S , Date - %Y-%m-%d '))
        
        # writing the last time and date when the file is checked into the text file
        f.write(datetime.now().strftime('\nLast checked time - %H:%M:%S , Date - %Y-%m-%d '))
        f.write("\n")
        f.close()
        
        
        time.sleep(60)   # giving a break to program of 1 min
        #after one min it will scan the folder again for details
except KeyboardInterrupt:
    print("Quitting the program.")
except:  
    raise



 


