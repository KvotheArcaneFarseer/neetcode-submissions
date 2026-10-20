class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        overall = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            if nums[i] > 0:
                return overall
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                while j < k:
                    total = nums[i] + nums[j] + nums[k]
                    if total < 0:
                        j += 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                    elif total > 0:
                        k -= 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    else:
                        overall.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
        return overall