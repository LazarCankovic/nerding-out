class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in n_dict:
                return [n_dict[diff], i]
            n_dict[n] = i
        return