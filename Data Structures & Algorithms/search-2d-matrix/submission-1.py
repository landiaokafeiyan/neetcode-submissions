# class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2

            row = m // cols
            col = m % cols#为什么？因为这是商和余数在二维数组坐标中的直接应用

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1

        return False