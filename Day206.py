def moveZeros(n: int,  a: [int]) -> [int]:
    count=0
    temp=[]
    for i in a:
        if i!=0:
            temp.append(i)
        else:
            count+=1
        
    for i in range(count):
        temp.append(0)
    return temp
