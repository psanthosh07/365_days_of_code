class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range (0,len(nums)-1):
            for j in range(1,len(nums)):
                    if nums[i]+nums[j]==target:
                        a.append(i)
                        a.append(j)
                        return a

        
