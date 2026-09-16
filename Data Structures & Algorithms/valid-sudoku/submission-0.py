class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxDict = {i: set() for i in range(9)}
        colDict = {i: set() for i in range(9)}
        for rowIndex, row in enumerate(board):
            rowSet = set()
            for colIndex, num in enumerate(row):
                if num != ".":
                    if num in rowSet or num in colDict[colIndex] or num in boxDict[self.boxNumber(rowIndex, colIndex)]:
                        return False
                    else:
                        rowSet.add(num)
                        colDict[colIndex].add(num)
                        boxDict[self.boxNumber(rowIndex, colIndex)].add(num)
        return True

    def boxNumber(self, row, col):
        colToAdd = col // 3
        rowToAdd = (row // 3) * 3
        return colToAdd + rowToAdd



        