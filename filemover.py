import datetime
import pathlib
from datetime import date
from fnmatch import fnmatch
import os
import re
import shutil


today =  date.today()
week = today.weekday()
if week == 0:
    day = "Mon"
elif week == 1:
    day = "Tue"
elif week == 2:
    day = "Wed"
elif week == 3:
    day = "Thu"
elif week == 4:
    day = "Fri"
elif week == 5:
    day = "Sat"
else:
    day = "Sun"
        
d = today.strftime("%b-%d-%Y")
d= d.split("-")
date = day+', '+d[0]+' '+d[1]+', '+d[2]

global path
global path2
path = '\\'+date
newpath = r"C:\\Users\\victoria\\Desktop\\Coding\\New Test"
#path = '\\Thu, Dec 29, 2023'

try:
    filename = pathlib.Path(r"C:\\Users\\victoria\\Desktop\\Coding\\"+path)
    print("Folder exists")
    try:
        filename2 = 'C:\\Users\\victoria\\Desktop\\Coding\\'+path
       # print("File exists")
        regex = re.compile('(.*xlsx)')
        for root, dirs, files in os.walk(filename):
            for file in files:
                if regex.match(file):
                    print(file)
                    #os.rename(filename2+"\\"+file, newpath+"\\"+file)
                    #os.replace(filename2+"\\"+file, newpath+"\\"+file)
                    shutil.move(filename2+"\\"+file, newpath+"\\"+file)

    except FileNotFoundError:
        print("No New File Found")      #If you have other files with a different extension, try/except will run for that file as well and print "No New File Found"
    finally:
        print("Files are moved to a new folder")
        
except FileNotFoundError:
    print("No New Folder Found")
