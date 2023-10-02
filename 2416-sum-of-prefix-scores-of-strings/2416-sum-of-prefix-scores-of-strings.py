class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = [0] * 26
        self.prefixOf = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = TrieNode("root")
        
        
        def insert(word): 
            curr = trie
            for i in range(len(word)):
                idx = ord(word[i]) - 97
                
                if curr.children[idx] == 0:
                    curr.children[idx] = TrieNode(word[i])
                
                curr = curr.children[idx] 
                curr.prefixOf += 1
                
                 
        for word in words:
            insert(word)
            
        def calc(word):
            total = 0
            curr = trie
            
            for i in range(len(word)):
                idx = ord(word[i]) - 97 
                curr = curr.children[idx]
                total += curr.prefixOf
                
            return total
        
        
        for i in range(len(words)):
            words[i] = calc(words[i])
            
            
        return words
                
            
            
        
                
                
                
                
        
                    
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        