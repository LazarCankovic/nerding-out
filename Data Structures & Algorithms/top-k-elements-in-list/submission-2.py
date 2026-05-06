class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # create a list of buckets
        freq = [[] for num in range(len(nums) + 1)]

        # fill in the count dictionary:
        # num: num_count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # fill in the buckets where the index is num_count
        # because that way we have the position of the 
        # most frequent one at the end
        # the values are the actual numbers
        for num, num_count in count.items():
            freq[num_count].append(num)

        res = []

        # loop through the length of he freq backwards
        # for the biggest count, take out the value
        # and append it to the res, since k >= 1
        # then check if the size of res == k, if yes return res
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []



