li = []
leng = 0
def inp():
    x = input("Enter anything you want to add or enter 'end' to stop giving inputs: ").lower()
    if x == "end":
        exit
        
    else:
        li.append(x)
        inp()
inp()
for i in li:
    i = 1
    leng += i
print("The length of the list you made is: ",leng)