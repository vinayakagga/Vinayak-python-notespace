'''🔥 TASK: List Operations Challenge
Problem Statement

Write a Python program that:

Takes 5 integers from the user and stores them in a list

Prints the original list

Appends a number 99 at the end

Inserts 50 at index 2

Removes the first occurrence of a number entered by the user

If the number is not present, print "Number not found"

Sorts the list in ascending order

Reverses the list

Prints:

Final list

Length of list

Maximum element

Minimum element

Sum of all elements

Constraints (important)

Use list methods only where applicable

Use loops for input

Use if condition for remove logic

Do not use advanced features

Do not hardcode the list'''
a=[]
b=0
for i in range(5):
    num=int(input("provide numbers"))
    a.append(num)
print(a)
a.append(99)
a.insert(2,50)
b=int(input("please enter the no. to be removed"))
if a.count(b)==0:
    print("no. not in list")
else:
    a.remove(b)
print(a)
a.sort()
print(a)
a.reverse()
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

