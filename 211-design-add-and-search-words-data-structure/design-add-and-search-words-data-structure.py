class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.head = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.head

        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]

        curr.isEnd = True

  

    def search(self, word: str) -> bool:

        def _dfs(idx, curr):
            
                if idx == len(word): return curr.isEnd

                if word[idx] == ".":
                    for child in curr.children.values():
                        if _dfs(idx + 1, child): return True

                    return False

                elif word[idx] not in curr.children: return False

                else: return _dfs(idx + 1, curr.children[word[idx]])


        return _dfs(0, self.head)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)