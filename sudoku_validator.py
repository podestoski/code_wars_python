import math
class Sudoku(object):
    def __init__(self, data):
        self.board = data
        pass
    
    def validate_sudoku(self):
        board_len = len(self.board)
        # validate length
        if(board_len<=0):
            return False

        #validate that √N is an integer
        root = int(math.sqrt(board_len))
        if root * root != board_len:
            return False

        valid_set = set(range(1, board_len + 1))

        #validate that rows have equal lenght s
        for row in self.board:
           if (len(row) != board_len):
              return False
           #Validate that row have valid valiues
           if set(row) != valid_set:
               return False


        #validate columns
        tranpose_board = zip(*self.board)
        for row in tranpose_board:
            if set(row) != valid_set:
               return False

        for row_start in range(0, board_len, root):
            for col_start in range(0, board_len, root):
                block = []
                for r in range(row_start, row_start + root):
                    for c in range(col_start, col_start + root):
                        block.append(self.board[r][c])
                if set(block) != valid_set:
                    return False

        return True
    
    def is_valid(self):
       return self.validate_sudoku()




@test.describe("Validate sudoku")
def validate_sudoku():
    
    # Valid Sudoku
    goodSudoku1 = Sudoku([
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],
    
      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],
      
      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ])
    
    goodSudoku2 = Sudoku([
      [1,4, 2,3],
      [3,2, 4,1],
    
      [4,1, 3,2],
      [2,3, 1,4]
    ])
    
    # Invalid Sudoku
    badSudoku1 = Sudoku([
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ])
    
    badSudoku2 = Sudoku([
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],  
      [1]
    ])
    
    @test.it('should be valid')
    def should_be_valid():
        test.assert_equals(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
        test.assert_equals(goodSudoku2.is_valid(), True, 'Testing valid 4x4')
    
    @test.it ('should be invalid')
    def should_be_invalid():
        test.assert_equals(badSudoku1.is_valid(), False, 'Values in wrong order')
        test.assert_equals(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')