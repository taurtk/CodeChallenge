a=[1,1,2,2,2,3,4,5]
i=0
b=set()

while i<len(a):
    if a[i] in b:
        print(a[i])
    else:
        b.add(a[i])
    i=i+1
