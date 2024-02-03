#Return the factorial of the number N
def factorial(N):
    res=1
    for i in range(2,N+1):
        res*=i
    return res
        
