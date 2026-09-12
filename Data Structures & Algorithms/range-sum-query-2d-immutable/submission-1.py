class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.sumMatrix = [[0] * len(row) for row in self.matrix]
        for ri, row in enumerate(matrix):
            rowSum = 0
            for ci, ele in enumerate(row):
                rowSum += ele
                if ri > 0:
                    self.sumMatrix[ri][ci] = self.sumMatrix[ri - 1][ci] + rowSum
                else:
                    self.sumMatrix[ri][ci] = rowSum
                


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.sumMatrix[row2][col2]
        if row1 > 0:
            topRec = self.sumMatrix[row1 - 1][col2]
        else:
            topRec = 0
        if col1 > 0:
            leftRec = self.sumMatrix[row2][col1 - 1]
        else:
            leftRec = 0
        if row1 > 0 and col1 > 0:
            finalAns = self.sumMatrix[row1 - 1][col1 - 1]
        else:
            finalAns = 0
        return finalAns - topRec - leftRec + bottomRight 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)