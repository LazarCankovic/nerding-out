class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if the number before n is not in the set ======= start of seq
            if (n - 1) not in numSet:
                length = 0
                # if it is a start of a sequence keep looking for numbers after
                while (n + length) in numSet:
                    length += 1
                # once done, find the max of the size of sequences    
                longest = max(length, longest)
        return longest