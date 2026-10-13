class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        other = set(nums)
        length = []
        for i in other:
            temp = []
            if i-1 not in other:
                while i in other:
                    temp.append(i)
                    i += 1
                length.append(len(temp))
        if len(nums) == 0:
            return 0
        else:
            return max(length)