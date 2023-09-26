class Trie:

    def __init__(self):
        self.tree = [0] * 27

    def insert(self, word: str) -> None:
        
        curr = self.tree
        
        for i in range(len(word)):
            
            idx = ord(word[i]) - 97
            
            if curr[idx] == 0:
                curr[idx] =  [0] * 27
                
            if i == len(word) - 1:
                curr[idx][-1] = 1
                
            curr = curr[idx]
            
            
    def search(self, word: str) -> bool:
        
        curr = self.tree
        
        for i in range(len(word)):
            
            idx = ord(word[i]) - 97
            
            if curr[idx] == 0:
                return False
    
            curr = curr[idx]
        
        return True if curr[-1] == 1 else False

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.tree
        
        for i in range(len(prefix)):
        
            idx = ord(prefix[i]) - 97
            
            if curr[idx] == 0:
                return False
    
            curr = curr[idx]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)