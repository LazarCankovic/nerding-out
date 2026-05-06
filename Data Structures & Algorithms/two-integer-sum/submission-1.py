class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in my_dict:
                return [my_dict[difference], i]
            my_dict[n] = i
        return []