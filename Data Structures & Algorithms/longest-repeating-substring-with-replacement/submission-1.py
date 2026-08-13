class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxWindow = 0
        l = 0

        for r in range(len(s)):
            # for each letter grab the count
            count[s[r]] = 1 + count.get(s[r], 0)
            # while the window size - the count of the letter is > k, move the left pointer
            # and remove that letters count from the dict
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            maxWindow = max(maxWindow, (r - l + 1))
        return maxWindow