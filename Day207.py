def linearsearch(arr,num):
    l=len(arr)
    for i in range(len(arr)):
        if arr[i]==num:
            return i
    return -1
    
