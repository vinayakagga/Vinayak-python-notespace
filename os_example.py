'''🧠 Now the PRACTICE TASK (small but real)
🧪 Task: Folder File Scanner

Write a program that:

Takes a folder name as input

If folder does NOT exist → print "Folder not found"

Else:

List all items in it

For each item:

Print name

Print whether it’s a file or folder

Print file extension (if file)

Constraints:

Must use os

Must use os.path

No hardcoded paths

No deleting anything

Example output:
data.csv   | file | .csv
notes.txt  | file | .txt
images     | folder

🎯 Why this task matters

This task teaches:

Path safety

File system traversal

Practical os usage

Real-world scripting'''
import os
folname=input("Please give the folder name for which information is required(leave blkank for current directory)")
genpath=os.getcwd()
abspath=os.path.join(genpath,folname)
if (os.path.isdir(abspath)==True):
    print("folder found")
    print(os.listdir(abspath))
    lis=os.listdir(abspath)
    for items in lis:
        li=os.path.splitext(items)
        if(os.path.isdir(os.path.join(abspath,items))):
            print ("Folder name:  "+li[0])
        else:
            print("File name: "+li[0]+"  Extension:"+li[1])
else:
    print("directory not find")
        


    

