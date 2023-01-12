class Solution:
    def isValid(self, st: str) -> bool:
        stack = []
        hashmap = {')':'(', '}':'{', ']':'['}
        for i in st:
            if i not in hashmap:
                stack.append(i)
            else:
                if stack and stack[-1]==hashmap[i]:
                    stack.pop()
                else: return False
        return True if not stack else False
