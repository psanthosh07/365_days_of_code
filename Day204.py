def getSecondOrderElements(n: int,  a: [int]) -> [int]:

    maxi=a[0]
    secmax=-1
    mini=a[0]
    secmini=max(a)

    for i in range(0,n):
        if a[i]>maxi:
            secmax=maxi
            maxi=a[i]
        elif a[i]!=maxi and a[i]>secmax:
            secmax=a[i]
        if mini>a[i]:
            secmini=mini
            mini=a[i]
        elif(a[i]!=mini and a[i]<secmini):
            secmini=a[i]
    
    return secmax,secmini
