class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for num in range(len(nums) + 1 )]

        # created the dict of n : cnt
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []
        for bucket in range(len(freq) - 1, 0, -1):
            for n in freq[bucket]:
                res.append(n)
                if len(res) == k:
                    return res


