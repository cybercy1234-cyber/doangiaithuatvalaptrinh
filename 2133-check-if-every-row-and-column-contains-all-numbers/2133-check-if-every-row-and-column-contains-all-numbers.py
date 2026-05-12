class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)

        need = set(range(1, n + 1))

        # kiểm tra từng hàng
        for row in matrix:
            if set(row) != need:
                return False

        # kiểm tra từng cột
        for col in range(n):

            column = []

            for row in range(n):
                column.append(matrix[row][col])

            if set(column) != need:
                return False

        return True