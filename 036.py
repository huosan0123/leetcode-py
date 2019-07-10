class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            string = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in string:
                    return False
                string.append(board[i][j])
            
            string = []
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in string:
                    return False
                string.append(board[j][i])
            
        for i in range(3):
            for j in range(3):
                string = []
                for x in range(i*3, (i+1)*3):
                    for y in range(j*3, (j+1)*3):
                        if board[x][y] != '.'  and board[x][y] in string:
                            return False
                        string.append(board[x][y])
            
        return True
