class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dicti={}
        for i in nums:
            if i in dicti:
                return True
            dicti[i]=1
        return False
