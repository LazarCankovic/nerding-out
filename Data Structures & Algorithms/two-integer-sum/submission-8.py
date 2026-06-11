class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in num_map:
                return [num_map[difference], i]
            num_map[n] = i