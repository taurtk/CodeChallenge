# coding: utf-8
# Your code here!
st=input().split()
n=len(st)
for i in range(0,n-1):
    for j in range(i+1,n-1):
        if st[i]==st[j]:
            del(st[j])
            break
for i in range(len(st)):
    print(st[i],end=" ")
