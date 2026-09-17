class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix) # number of rows
        cols = len(matrix[0]) # number of columns
        t = rows * cols
        l = 0
        r = t - 1

        while l <= r:
            mid = (l + r) // 2 # midpoint
            i = mid // cols
            j = mid % cols

            mid_num = matrix[i][j]
            if target == mid_num:
                return True
            elif target < mid_num:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

        # Time : O(log(m*n))
        # Space: O(1)