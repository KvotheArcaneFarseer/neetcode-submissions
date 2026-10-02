class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        others = {}
        for index, chare in enumerate(nums):
            if target - chare not in others:
                others[chare] = index
            else:
                return [others[target-chare], index]
        