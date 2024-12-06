import csv


f=open('lists.txt',"r")
lines=f.readlines()
values1=[] 
values2=[]
imajackoff = 0
for x in lines:
    values1.append(int(x.split('   ')[1]))
    values2.append(int(x.split('   ')[0]))
f.close()

values1.sort()
values2.sort()

for x in range(len(values1)):
    imajackoff += abs(values1[x]-values2[x])

print(imajackoff)