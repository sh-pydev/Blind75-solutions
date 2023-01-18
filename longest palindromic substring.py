class Solution:
    def longestPalindrome(self, s: str) -> str:
        x = len(s)
        res = 0
        ans = ''
        for i in range(0,x):
            l,r = i,i
            while l >= 0 and r < x and s[l] == s[r]:
                temp = r - l + 1
                if temp > res:
                    ans = s[l:r+1]
                    res = temp
                l -= 1
                r += 1

        for i in range(0,x):
            l,r = i,i+1
            while l >= 0 and r < x and s[l] == s[r]:
                temp = r - l + 1
                if temp > res:
                    ans = s[l:r+1]
                    res = temp
                l -= 1
                r += 1
        return ans
