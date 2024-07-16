class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r=s[::-1]
        count=0
        for i in r:
            if i==" ":
                if count==0:
                    continue
                break
            count+=1
            print(i)
            
        return count
        
