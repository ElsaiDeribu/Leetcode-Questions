class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.index = -1

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.trie = TrieNode("root")
        
        def insertToTrie(word, index):
            curr = self.trie
            for l in word:
                if l not in curr.children:
                    curr.children[l] = TrieNode(l)
                
                curr = curr.children[l]
                curr.index = index
                
                
        def insertPossibilities(word, index):
            for j in range(len(word) - 1, - 1, -1 ):
                temp =  word[j:] + "|" + word  
                insertToTrie(temp, index)
             
            
        for i in range(len(words)):
            insertPossibilities(words[i], i)
        
        
        

    def f(self, pref: str, suff: str) -> int:
        
        def search(word):
            curr = self.trie
            
            for l in word:
                if l not in curr.children:
                    return -1
                
                curr = curr.children[l]
                
            return curr.index 
        
        return search(suff + "|" + pref)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)