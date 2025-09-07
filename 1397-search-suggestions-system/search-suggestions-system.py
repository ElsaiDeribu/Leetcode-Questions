class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggest = []        


class Trie:

    def __init__(self):
        self.trie = TrieNode()


    def insert(self, word):
        node = self.trie

        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()

            node = node.children[w]
            
            if len(node.suggest) < 3:
                node.suggest.append(word)

    def suggest(self, word):
        res = [[] for _ in range(len(word))]
        node = self.trie

        for i in range(len(word)):
            w = word[i]
            if w in node.children:
                node = node.children[w]
                res[i] = (node.suggest[:])

            else:
                break

            
        return res
        


    

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        trie = Trie()
        products.sort()
        for p in products:
            trie.insert(p)

        return trie.suggest(searchWord)
        