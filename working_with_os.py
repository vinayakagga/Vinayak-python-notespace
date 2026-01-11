import os
print(os.getcwd())
print(os.listdir())
os.chdir("tempo")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())