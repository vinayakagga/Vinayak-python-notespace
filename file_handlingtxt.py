with open("vina.txt","a+") as fil:
    fil.write("text is here\nyayay!!")
    fil.seek(0)
    for u in fil:
        print(u.strip("\n"))
    print(fil.tell())
fil.close()


        