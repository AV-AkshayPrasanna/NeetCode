class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Build trie; each node is a dict, with "$" holding the complete word
        root = {}
        for w in words:
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
            node["$"] = w

        m, n = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent[ch]

            if "$" in node:
                res.append(node.pop("$"))

            board[r][c] = "#"  # mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
                    dfs(nr, nc, node)
            board[r][c] = ch  # restore

            # prune exhausted branch
            if not node:
                del parent[ch]

        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, root)

        return res