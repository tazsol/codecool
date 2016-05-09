mylist = [0]
opened = [0]
for i in range(1,101):
    mylist.append(0)

for n in range(1,101):
    for k in range (1,101):
        if( k%n == 0):
            mylist[k] = mylist[k]+1

for j in range(1,101):
    if( mylist[j]%2 == 1):
        opened.append(j)

print ("The following doors are open:", opened[1:])
