class Solution:

    def encode(self, strs: List[str]) -> str:
        combined = ""
        for i in strs:
            combined += str(len(i))+ "#" + i
        return combined
    def decode(self, s: str) -> List[str]:
        org = []
        i = 0
        while i < len(s):
            change = ''
            while s[i] != '#':
                change += s[i]
                i += 1
            change = int(change)
            org.append(str(s[i+1: i + 1 + change]))
            i = i + 1 + change
        return org

