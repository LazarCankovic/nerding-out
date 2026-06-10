class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = []
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                sol.append(l + 1)
                sol.append(r + 1)
                return sol
        
