class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqlist = {}
        final = []
        for i in nums:
            if i not in freqlist:
                freqlist[i] = 1
            else:
                freqlist[i] += 1
        bucket = [[] for i in range(max(freqlist.values()) + 1)]
        for number, freq in freqlist.items():
            bucket[freq].append(number)
        for i in range(len(bucket)-1, 0, -1):
            if len(final) < k:
                for b in bucket[i]:
                    final.append(b)
            if len(final) == k:
                return final
        