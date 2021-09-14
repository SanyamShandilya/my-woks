q = open("DATA.txt","r")
w = q.readlines()
for i in w:
    if "print" in i:
        print(i)
