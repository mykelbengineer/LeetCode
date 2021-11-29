class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            
            curr = curr.children[ch]
            curr.suggestions.append(word)
            curr.suggestions.sort()
            
            while len(curr.suggestions) > 3:
                curr.suggestions.pop()

    def search(self, word):
        curr = self.root
        res = []
        
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
                res.append(curr.suggestions[:])
                
            else:
                break
        
        remaining = len(word) - len(res)
        
        for _ in range(remaining):
            res.append([])
            
        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        
        for product in products:
            trie.insert(product)
            
        return trie.search(searchWord)
        