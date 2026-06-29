class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        mp = defaultdict(list)
        for i in strs:
            m= [0]*26
            for j in i:
                m[ord(j)-ord("a")]+=1
            mp[tuple(m)].append(i)
        return list(mp.values())
        