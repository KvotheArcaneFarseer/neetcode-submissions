class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        analist = {}
        for anas in strs:
            anagrams = {}
            for chars in anas:
                if chars not in anagrams:
                    anagrams[chars] = 1
                else:
                    anagrams[chars] += 1
            key = tuple(sorted(anagrams.items()))
            if key not in analist:
                analist[key] = [anas]
            else:
                analist[key] += [anas]
        return list(analist.values())

