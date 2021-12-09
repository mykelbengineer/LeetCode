class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, stack = 0, [-1]
        for i, c in enumerate(s):
            if c == ")":
                stack.pop()
                if stack:
                    ans = max(ans, i - stack[-1])
                    continue
            stack.append(i)
        return ans