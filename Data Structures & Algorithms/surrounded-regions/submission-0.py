class Solution:
    def solve(self, board):
        m, n = len(board), len(board[0])
        st = [(i, j) for i in range(m) for j in range(n) if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == "O"]
        for i, j in st:
            board[i][j] = "S"
        while st:
            x, y = st.pop()
            for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= a < m and 0 <= b < n and board[a][b] == "O":
                    board[a][b] = "S"
                    st.append((a, b))
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "S" else "X"