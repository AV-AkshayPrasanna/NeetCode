class WordDictionary:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        return self.dfs(self, word, 0)

    def dfs(self, node, word, i):
        if i == len(word):
            return node.is_end
        ch = word[i]
        if ch == '.':
            for child in node.children.values():
                if self.dfs(child, word, i + 1):
                    return True
            return False
        if ch not in node.children:
            return False
        return self.dfs(node.children[ch], word, i + 1)