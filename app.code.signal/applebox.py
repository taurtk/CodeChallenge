def appleBoxes(k):
    lst= [i*i for i in range(2,k+1) if i%2==0]
    lst1= [i*i for i in range(1,k+1) if i%2!=0]
    a=sum(lst)
    b=sum(lst1)
    
    return a-b