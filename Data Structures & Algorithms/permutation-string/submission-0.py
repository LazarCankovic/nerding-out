class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = {}

        for c in s1:
            count1[c] = 1 + count1.get(c, 0)

        count2 = {}

        for right in range(len(s2)):
            # char getting in from the right, add to the count2
            c = s2[right]
            count2[c] = 1 + count2.get(c, 0)
            # now that we have a built out dict, check for the window
            if right >= len(s1): # keep the window fixed
                # take out the first element
                left_char = s2[right - len(s1)]
                count2[left_char] -= 1
                # to make the dicts equal, remove the ones with count 0
                if count2[left_char] == 0:
                    del count2[left_char]
            if count1 == count2:
                return True
        return False

