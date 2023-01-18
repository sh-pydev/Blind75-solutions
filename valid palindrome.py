class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = list()
        for i in s:
            i = i.lower()
            if (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('0') and ord(i) <= ord('9')):
                final.append(i)
        if final == final[::-1]:
            return True
        else: return False
