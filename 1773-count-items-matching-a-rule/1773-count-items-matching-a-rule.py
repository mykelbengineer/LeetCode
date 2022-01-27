class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule_map = {"type":0, "color":1, "name":2}
        
        output = 0
        
        searchIndex = rule_map[ruleKey]
        
        for item in items:
            if item[searchIndex] == ruleValue:
                output += 1
                
                
        return output
            
        
        