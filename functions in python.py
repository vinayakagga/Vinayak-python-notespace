'''🧠 MINI APP TASK: Student Score Manager (CLI App)

You will build a menu-driven command-line app.

This app must use:

variables

lists

loops

conditions

functions

safe mutation vs return

input/output

❌ No dictionaries
❌ No files
❌ No imports

📌 APP DESCRIPTION

The app manages student scores using lists.

Data rules

Student names → list of strings

Student marks → list of integers

Same index = same student

Example:

names = ["A", "B"]
marks = [80, 90]

📋 FEATURES (REQUIRED)
1️⃣ Add student

Input student name

Input marks

Store both

2️⃣ Display all students

Format:

Name: A | Marks: 80
Name: B | Marks: 90

3️⃣ Calculate average marks

Use a function

Return the average

Do NOT print inside the function

4️⃣ Find highest scorer

Print student name + marks

Use loop logic (no shortcuts)

5️⃣ Remove a student

Input name

If name exists → remove name and marks

Else → print "Student not found"

6️⃣ Exit app
📟 MENU (MANDATORY)

The app must run in a loop like:

1. Add student
2. Display students
3. Average marks
4. Highest scorer
5. Remove student
6. Exit

🧩 FUNCTION REQUIREMENTS (IMPORTANT)

You must use functions for:

Adding student

Displaying students

Calculating average

Finding highest scorer

Removing student

Each function should:

Either mutate OR return

Not do both

⚠️ CONSTRAINTS (STRICT)

❌ No dictionaries

❌ No global mutation inside functions unless intentional

❌ No shortcuts like max(zip())

✅ Use loops explicitly

✅ Use .append(), .remove(), .pop()'''
students=[]
marks=[]
subj=("physics","chemistry","maths")
le=0
avg=0
highest=0
inp=0
def addstu():
    students.append(input("Enter a the name of the student"))
    pcm=[]
    for x in range (3):
        pcm.append(int(input("please enter the marks of "+ subj[x])))
    marks.append(pcm)

def disp():
    le=len(students)
    if(le!=0):
        for i in range(le):
            print("Student" + students[i])
            for j in range(3):
                print("The marks of"+subj[j]+"are" + str(marks[i][j]))
    else:
        print("enter a student first")
def avgmarks ():
    le=len(students)
    if(le!=0):
        for i in range(le):
            print("The student"+ students[i] +"has avg marks"+ str(sum(marks[i])/3) )
            
    else:
        print("Please add a student first")
def highe():
    tops=[]
    le=len(students)
    if(le!=0):
        highest=sum(marks[0])
        for i in range(le):
            if (highest<sum(marks[i])):
                highest=sum(marks[i])
                tops=[i]
            elif(highest==sum(marks[i])):
                tops.append(i)
    for j in range (len(tops)):
        print(str(students[tops[j]]) + "scored :" + str(sum(marks[tops[j]])) )
def rem():
    name=input("enter the name of student which has to be removed")
    if(students.count(name)!=0):
        marks.pop(students.index(name))
        students.remove(name)
    else:
        print("student not found")

while True:
    inp=int(input("To add a student press 1\nTo print student2 press 2\nTo print avg of students press 3\nTo print topper students press 4\nTo remove a student press 5\nTo exit the program enter 6"))
    if (inp==1):
        addstu()
    elif(inp==2):
        disp()
    elif(inp==3):
        avgmarks()
    elif(inp==4):
        highe()
    elif(inp==5):
        rem()
    elif(inp==6):
        break
    else:
        print("The input is invalid do again")



