class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        result=""
        for i in range(max(a,b)):
            if i < a:
                result+=word1[i]
            
            if i<b:
                result+=word2[i]
        
        return result
                
            
        
