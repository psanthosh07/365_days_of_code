class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s=nums
        nums.extend(s)

        return nums
