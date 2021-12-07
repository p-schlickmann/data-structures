"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False
        opening = set('([{')
        matches = set([('(', ')'), ('[', ']'), ('{', '}')])  # faster then set literal (wtf?)
        stack = []

        for paren in s:
            if paren in opening:
                stack.append(paren)
            else:
                if not stack:
                    return False
                last_open = stack.pop()
                if (last_open, paren) not in matches:
                    return False
        return not stack


sol = Solution()
print(sol.isValid('()'))
print(sol.isValid("(){}}{"))
print(sol.isValid('()[]{}'))
print(sol.isValid('('))
print(sol.isValid('([])'))
print(sol.isValid('([})'))
print(sol.isValid('([)]'))
