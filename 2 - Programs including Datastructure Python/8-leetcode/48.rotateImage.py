class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if(j > i):
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            left_col = 0
            right_col = cols-1
            while(left_col < right_col):
                matrix[i][left_col], matrix[i][right_col] = matrix[i][right_col], matrix[i][left_col]
                left_col += 1
                right_col -= 1
