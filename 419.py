class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        ans = 0
        if len(board) == 0 or len(board[0]) == 0:
            return ans
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    ans += 1 if board[0][0] == 'X' else 0
                    continue
                if i == 0:
                    ans += 1 if board[0][j] == 'X' and board[0][j-1] == '.' else 0
                    continue
                if j == 0:
                    ans += 1 if board[i][0] == 'X' and board[i-1][0] == '.' else 0
                    continue
                if board[i][j] == 'X' and board[i-1][j] == '.' and board[i][j-1] == '.':
                    ans += 1
        return ans
        
# brilliant java solution!!!!  consider '.' is easy
    public int countBattleships(char[][] board) {
        int m = board.length;
        if (m==0) return 0;
        int n = board[0].length;
        
        int count=0;
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (board[i][j] == '.') continue;
                if (i > 0 && board[i-1][j] == 'X') continue;
                if (j > 0 && board[i][j-1] == 'X') continue;
                count++;
            }
        }
        
        return count;
    }
