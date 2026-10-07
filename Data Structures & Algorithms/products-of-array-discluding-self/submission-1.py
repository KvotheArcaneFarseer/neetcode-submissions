class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = []
        leftpast = 1
        rightpast = 1
        for i in range(len(nums)):
            if i != 0:
                leftpast *= nums[i-1]
            prod.append(leftpast)
        for i in range(len(nums), 0,-1):
            if i != len(nums):
                rightpast *= nums[i]
            prod[i-1] *= rightpast
        return prod
        