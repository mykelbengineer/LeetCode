class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_dict = defaultdict(int)
        lowered_p = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = lowered_p.split()
        banned_words = set(banned)
        
        for word in words:
            if word not in banned:
                words_dict[word] += 1
                
        max_word = max(words_dict.values())
        
        print(words_dict)
        
        for k, v in words_dict.items():
            if v == max_word:
                return k