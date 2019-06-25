def addBorder(picture):
    n=len(picture)
    a=len(picture[0])
    b=len(picture[n-1])
    lst=[]
    str="**"
    for i in range(0,a):
        str+="*"
    lst.append(str)
    for i in range(0,n):
        
        lst.append("*"+picture[i]+"*")
    lst.append(str)
    return lst
        
        
        