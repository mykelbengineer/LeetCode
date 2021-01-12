class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = right = max_count =  0
        len_of_s = len(s)
        check_dict = set()
        
        
        while  left < len_of_s and right < len_of_s:
            if s[right] not in check_dict:
                check_dict.add(s[right])
                right += 1
                max_count = max(max_count, right - left)
                
            else:
                check_dict.remove(s[left])
                left += 1
​
                
        
        return max_count
                
                
                
            
            
        
        
