class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i, n in enumerate(nums):
            comp = target - n

            if comp in num:
                return [num[comp],i]
            num[n] = i
        return  []           