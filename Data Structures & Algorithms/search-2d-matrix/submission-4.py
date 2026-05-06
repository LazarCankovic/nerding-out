class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_bucket, r_bucket = 0, len(matrix) - 1
        while l_bucket <= r_bucket:
            mid_index = (l_bucket + r_bucket) // 2
            mid_bucket = matrix[mid_index]
            l_pos, r_pos = 0, len(mid_bucket) - 1

            if mid_bucket[l_pos] > target:
                r_bucket = mid_index - 1
            elif mid_bucket[r_pos] < target:
                l_bucket = mid_index + 1
            else:
                while l_pos <= r_pos:
                    mid = (l_pos + r_pos) // 2
                    if mid_bucket[mid] < target:
                        l_pos = mid + 1
                    elif mid_bucket[mid] > target:
                        r_pos = mid - 1
                    else:
                        return True
                return False
        return False