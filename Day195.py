class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        val = {")":"(", "}":"{", "]":"["}
        
        for i in s:
            if i in val.values()  :
                l.append(i)
            else:
                if not l or val[i]!=l.pop():
                    return False
        
        return not l
