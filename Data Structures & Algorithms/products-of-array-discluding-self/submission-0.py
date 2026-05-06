class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output array, making sure it's the same size
        output = [1] * len(nums)

        # start prefix at 1, because there is nothing before
        # the first element in an array
        prefix = 1
        for i in range(len(nums)):
            # set the first element to 1, and the rest later
            # will be updated by mult the number at that index
            # from nums
            output[i] = prefix
            prefix *= nums[i]
        
        # start sufix at 1, because there is nothing after
        # the last element in an array
        sufix = 1
        for i in range(len(nums) - 1, -1, -1):
            # multiply by the suffix to combine the left and 
            # right product without modifying nums[i]
            output[i] *= sufix
            sufix *= nums[i]
        return output
