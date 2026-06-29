class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0]*26
        for n in s:
            freq[ord(n) - ord('a')]+=1
        for n in t:
            freq[ord(n)-ord('a')]-=1
        for num in freq:
            if num!=0:
                return False
        return True
        