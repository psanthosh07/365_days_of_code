class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        s=''
        for i in A:
            if i.islower():
                s+=i.upper()
            elif i.isupper():
                s+=i.lower()
            else:
                s+=i
        return s
                
            
