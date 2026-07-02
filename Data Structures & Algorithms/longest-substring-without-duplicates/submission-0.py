class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        mp={}
        maxi=0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(l,mp[s[r]]+1)
            mp[s[r]]=r
            maxi=max(maxi,r-l+1)
        return maxi

        
