"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.
The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""

class Sudoku(object):
    def __init__(self, data):
        self.sudokuList = data

    def validate_sudoku_size(self):
        if not (len(self.sudokuList)**(1/2)).is_integer():
            return False
        for row in self.sudokuList:
            if not (len(row)**(1/2)).is_integer():
                return False
        return True

    def validate_integer_at_sudoku(self):
        for row in self.sudokuList:
            for cell in row:
                print(cell)
                if isinstance(cell, str) or isinstance(cell, bool) or cell > len(row) or cell < 1:
                    return False
            print()
        return True
    
    @staticmethod
    def validate_row(square, row: list):
        if row.count(square) > 1:
            return False
        return True

    @staticmethod
    def validate_column(square, column: list):
        if column.count(square) > 1:
            return False
        return True

    @staticmethod
    def validate_sector(square, sector: list):
        if sector.count(square) > 1:
            return False
        return True

    def validate_sudoku_rules(self):
        for row in self.sudokuList:
            for indexSquare, square in enumerate(row):
                self.validate_row(square, row)
                self.validate_column(square, [self.sudokuList[index][indexSquare] for index in range(len(row))])
                print([print(self.sudokuList[index][indexSquare]) for index in range(len(row))])
                
        return True

    def is_valid(self):
        if self.sudokuList != [] and self.sudokuList != 0:
            return (self.validate_integer_at_sudoku() and self.validate_sudoku_size())
        return False

goodSudoku1 = Sudoku([
[7, 8, 4,   1, 5, 9,   3, 2, 6] ,
[5, 3, 9,   6, 7, 2,   8, 4, 1] ,
[6, 1, 2,   4, 3, 8,   7, 5, 9] ,

[9, 2, 8,   7, 1, 5,   4, 6, 3] ,
[3, 5, 7,   8, 4, 6,   1, 9, 2] ,
[4, 6, 1,   9, 2, 3,   5, 8, 7] ,

[8, 7, 6,   3, 9, 4,   2, 1, 5] ,
[2, 4, 3,   5, 6, 1,   9, 7, 8] ,
[1, 9, 5,   2, 8, 7,   6, 3, 4] 
])

print(goodSudoku1.is_valid())


"""
[
[1, 2, 3,   4, 5, 6,   7, 8, 9], 
[2, 3, 1,   5, 6, 4,   8, 9, 7], 
[3, 1, 2,   6, 4, 5,   9, 7, 8], 

[4, 5, 6,   7, 8, 9,   1, 2, 3], 
[5, 6, 4,   8, 9, 7,   2, 3, 1], 
[6, 4, 5,   9, 7, 8,   3, 1, 2], 

[7, 8, 9,   1, 2, 3,   4, 5, 6], 
[8, 9, 7,   2, 3, 1,   5, 6, 4], 
[9, 7, 8,   3, 1, 2,   6, 4, 5]
]

[
[7, 8, 4,   1, 5, 9,   3, 2, 6] ,
[5, 3, 9,   6, 7, 2,   8, 4, 1] ,
[6, 1, 2,   4, 3, 8,   7, 5, 9] ,

[9, 2, 8,   7, 1, 5,   4, 6, 3] ,
[3, 5, 7,   8, 4, 6,   1, 9, 2] ,
[4, 6, 1,   9, 2, 3,   5, 8, 7] ,

[8, 7, 6,   3, 9, 4,   2, 1, 5] ,
[2, 4, 3,   5, 6, 1,   9, 7, 8] ,
[1, 9, 5,   2, 8, 7,   6, 3, 4] 
]"""