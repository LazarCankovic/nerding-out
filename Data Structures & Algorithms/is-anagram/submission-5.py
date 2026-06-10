class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_1, count_2 = {}, {}

        for i in range(len(s)):
            count_1[s[i]] = 1 + count_1.get(s[i], 0)
            count_2[t[i]] = 1 + count_2.get(t[i], 0)
        return count_1 == count_2