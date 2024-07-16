class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        for i in range (0,len(digits)):
            s+=int(digits[i])*(10**(len(digits)-i-1))
            print(s)
        s+=1
        arr=[]
        for j in str(s):
            arr.append(int(j))
        return arr
            

