'''🔥 MINI APP TASK 2: Simple Expense Tracker (CLI App)

This is a real-world style app.

🧠 APP IDEA

You are building a personal expense tracker.

Each expense has:

a category (string)

an amount (integer)

You will store everything in a dictionary.

📦 DATA MODEL (MANDATORY)

Use one dictionary only:

expenses = {
    "food": [120, 80, 200],
    "travel": [50, 300]
}


Meaning:

key → category

value → list of expenses in that category

❌ No parallel lists
❌ No classes
❌ No files
❌ No imports

📋 FEATURES (REQUIRED)
1️⃣ Add expense

Input category

Input amount

If category exists → append amount

Else → create new category

2️⃣ Display all expenses

Format:

Category: food
Expenses: [120, 80, 200]
Total: 400

3️⃣ Total expense (overall)

Calculate total of all categories

Must use a function that returns the total

4️⃣ Highest spending category

Find category with maximum total expense

Handle tie case (multiple categories)

5️⃣ Remove a category

Input category name

If exists → remove it

Else → print "Category not found"

6️⃣ Exit app
📟 MENU (MANDATORY)
1. Add expense
2. Display expenses
3. Total expense
4. Highest spending category
5. Remove category
6. Exit

🧩 FUNCTION RULES (STRICT)

You must write functions for:

add expense

display expenses

total expense

highest category

remove category

Each function must:

Either mutate OR return

Not both

⚠️ CONSTRAINTS (IMPORTANT)

❌ No dictionaries inside dictionaries

❌ No shortcuts like max(expenses, key=...)

✅ Use loops explicitly

✅ Use .items(), .append(), .pop()'''
data={}

def addexp():
    a=input("What is the category")
    if (a in data.keys()):
        data[a].append(int(input("Please enter the amount")))
    else:
        data[a]=[int(input("Please enter the value"))]

def disp():
    for nam , itm in data.items():
        print("Category:"+nam)
        print("rate:"+str(itm))
def tot():
    a=0
    for s in data.values():
        a+=sum(s)
    return a
def maxi():
    a=0
    c=""
    for b,s in data.items():
        if a<sum(s) :
            c=b
            a=sum(s)
    return c
def remov():
    a=input("please enter the cateory to be removed")
    if a in data :
        data.pop(a)
    else:
        print("category not found in data")

while True :
    print("Please enter 1 to enter a category\nPlease enter 2 to display expenses\nPlease enter 3 to get the total expenses\nPlease enter 4 to know the highest category\nPlease enter 5 to remove a category\nPlease enter 6 to exit\n")
    a=int(input("Please enter the selection"))
    if a==1:
        addexp()
    elif a==2:
        disp()
    elif a==3:
        print("the total expenditure is"+ str(tot()))
    elif a==4:
        print("the highest category is "+ str(maxi()))
    elif a==5 :
        remov()
    elif a==6:
        break
    else:
        print("Invalid selection please enter the number again")
    print("\n\n\n")



        


