class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqlist = {}
        for i in nums:
            if i not in freqlist:
                freqlist[i] = 1
            else:
                freqlist[i] += 1
        maxifreqi = []
        for i in range(k):
            maxi = max(freqlist, key=freqlist.get)
            maxifreqi.append(maxi)
            del freqlist[maxi]
        return maxifreqi
        
        