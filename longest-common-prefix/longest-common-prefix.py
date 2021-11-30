class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            
        curr.endOfWord = True
            

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        res = ''
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
            
        root = trie.root
        while root:
            if len(root.children) > 1 or root.endOfWord:
                return res
            
            key = list(root.children)[0]
            res += key
            
            root = root.children[key]
        return res
            
        
        