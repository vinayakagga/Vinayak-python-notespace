'''🔥 TASK: Number Analyzer (Till Loops Only)
Problem Statement

Write a Python program that:

Takes one number n from the user

If n is less than or equal to 0, print:

Invalid input


and stop the program

If n is greater than 0:

Print all numbers from 1 to n (using a for loop)

Count how many of them are even

Count how many of them are odd

Finally print:

Even count: X
Odd count: Y'''
num=int(input("Please enter a number"))
eve=0
if num<=0:
    print("invalid out")
else:
    for i in range(1,num+1):
        print(i)
        if i%2==0 :
            eve+=1
    print("even numbers are ")
    print(eve)
    print("odd number numbers are")
    print(num-eve+1)


