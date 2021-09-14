pos = 1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals() ['pos'] = i
            return True
        i += 1
    return False

li =[1,2,3,4,5,6,7,8,9]
num = 7
if search(li,num):
    print(num," is found at ",pos," index.")
else:
    print("None")