pos = 0
def binsearch(list,num):
    i = 0
    u = len(list)-1
    while i<=u:
        mid = (i+u)//2
        if(list[mid]==num):
            globals()["pos"]=mid
            return True
        else:
            if (list[mid]<num):
                i = mid + 1
            else:
                u = mid - 1
li = [1,2,3,4,4,4,5,6,7,8,9,10]
num = 5
if binsearch(li,num):
    print(num," is found at ",pos)
else:
    print("none")