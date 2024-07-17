from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        l = 0 
        r = len(s1)

        for i in range(l,r):
            s1_count[s1[i]] += 1
            s2_count[s2[i]] += 1
        if s1_count != s2_count:
            s1_count += 1
            l+=1
            r+=1
            

        


print(s.checkInclusion("abc","lecabee"))