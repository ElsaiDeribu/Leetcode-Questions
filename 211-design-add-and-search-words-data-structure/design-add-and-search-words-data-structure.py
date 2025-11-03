class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        
    def addWord(self, word: str) -> None:
        node = self.trie

        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()

            node = node.children[w]

        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.trie

        def dfs(node, idx):
            if idx == len(word):
                return node.isEnd

            if word[idx] != ".":
                if word[idx] not in node.children:
                    return False

                return dfs(node.children[word[idx]], idx + 1)

            else:
                res = False
                for child in node.children:
                    res = res or dfs(node.children[child], idx + 1)

                return res

        return dfs(node, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)