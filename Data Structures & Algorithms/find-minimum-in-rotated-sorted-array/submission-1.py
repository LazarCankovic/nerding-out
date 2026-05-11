class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            # checking first if the array is already sorted, if yes = done
            if nums[l] < nums[r]:
                res =  min(res, nums[l])
                break
            # if the array is not sorted, we take the middle point
            # set it to min, and then explore the right side and the left
            # if middle >= first from the left, look right, otherwise look left
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res