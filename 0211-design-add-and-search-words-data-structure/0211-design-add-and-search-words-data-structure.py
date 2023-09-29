class TrieNode:
    def __init__ (self, char):
        self.char = char
        self.children = [0] * 26
        self.isEnding = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode("root")

    def addWord(self, word: str) -> None:
        curr = self.trie
        
        for i in range(len(word)):
            idx = ord(word[i]) - 97
            
            if curr.children[idx] == 0:
                curr.children[idx] = TrieNode(word[i])
            
            if i == len(word) - 1:
                curr.children[idx].isEnding = True
            
            curr = curr.children[idx]
            
        

    def search(self, word: str) -> bool:
        curr = self.trie
        
        def dfs(curr, idx):
            if idx >= len(word):
                if curr.isEnding:
                    return True
                else:
                    return False
            
            if word[idx] != ".": 
                i = ord(word[idx]) - 97
                if curr.children[i] != 0: 
                    curr = curr.children[i] 
                else : 
                    return False
                
                return dfs(curr, idx + 1)
                
            else:
                res = False
                for child in curr.children:
                    if child != 0:
                        res = res or dfs(child, idx + 1)
                
                return res
                
        
        return dfs(curr, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)