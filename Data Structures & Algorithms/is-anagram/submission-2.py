class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # creating a dictionary to have a 1:1 mapping
        # letter : count

        count_s, count_t = {}, {}

        for i in range(len(s)):
            # fill the dictionary with counts
            # add 1, and check if that letter exists previousely
            # if it does not, default value is 0
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # compare the dictionaries
        return count_s == count_t
