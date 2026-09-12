class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        rowtrav = row1
        coltrav = col1
        while rowtrav <= row2:
            while coltrav <= col2:
                total += self.matrix[rowtrav][coltrav]
                coltrav += 1
            rowtrav += 1
            coltrav = col1

        return total

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)