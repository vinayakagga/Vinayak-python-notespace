import csv
with open("abc.csv","a+",newline="") as bifil:
    writ=csv.writer(bifil)
    writ.writerow(["topping","onion","caspiscum","mushroom"])
    writ.writerow(["rate","10","20","30"])
    bifil.seek(0)
    reader=csv.reader(bifil)
    for a,b,c,d in reader:
        print(a)
        print(b)
        print(c)
        print(d)
        print("\n")


    