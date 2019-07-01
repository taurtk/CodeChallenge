# coding: utf-8
# Your code here!
a=[1,1,2,2,2,3,4,5]
i=0
a.sort()
while i<len(a):
    if a[i]==a[i-1]:
        print(a[i])
    i=i+1
    

