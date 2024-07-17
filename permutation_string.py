from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0 
        r = len(s1)
        s1_dict = {}
        s2_dict = {}

        while r < len(s2):
            if s1 == s2:
                return True
            else:
                s1_dict.remove(s1[l])
                l+=1
                s1_dict.add(s1[l])
                s2_dict.remove(s1[r])
                r+=1
                s2_dict.add(s1[l])


s = Solution()
s.checkInclusion("abc", 'asdqfascasdafcab')