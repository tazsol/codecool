import math
mylist = [0]
n=1
for i in range(1,101):
    if (math.sqrt(i) == math.ceil(math.sqrt(i))):
        mylist.append(i)
print("The following doors are open:", mylist[1:])
