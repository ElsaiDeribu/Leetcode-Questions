class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.trie
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            
            node = node.children[w]

        node.isend = True

        

        

    def search(self, word: str) -> bool:

        node = self.trie

        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return False

        return node.isend 
        

    def startsWith(self, prefix: str) -> bool:

        node = self.trie

        for w in prefix:
            if w in node.children:
                node = node.children[w]
            else:
                return False

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)