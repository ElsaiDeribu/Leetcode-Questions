class TrieNode():
    def __init__(self, isEnd = False):
        self.children = {}
        self.isEnd = isEnd


class Trie:

    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()

            curr = curr.children[letter]

        curr.isEnd = True
        

    def search(self, word: str) -> bool:
        curr = self.head
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for letter in prefix:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)