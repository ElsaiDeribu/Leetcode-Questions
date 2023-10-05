class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [0] * 26
        self.total = 0

        
class MapSum:

    def __init__(self):
        self.trie = TrieNode("root")
        self.dic = {}
        

    def insert(self, key: str, val: int) -> None:
                
        add = val

        if key in self.dic:
            add = -self.dic[key] + add
            
        self.dic[key] = val
            
        curr = self.trie
        
        for i in range(len(key)):
            idx = ord(key[i]) - 97
            
            if curr.children[idx] == 0:
                curr.children[idx] = TrieNode(key[i])
             
            curr = curr.children[idx] 
            curr.total += add
        
        
        

    def sum(self, prefix: str) -> int:
        
        curr = self.trie
        
        for i in range(len(prefix)):
            idx = ord(prefix[i]) - 97
            if curr.children[idx] == 0:
                return 0
            
            curr = curr.children[idx] 
        
        return curr.total
        
   

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)