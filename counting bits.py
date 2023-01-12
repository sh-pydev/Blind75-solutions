class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(0,n+1):
            b = bin(i)[2:]
            a = 0
            for j in b:
                if j == '1':
                    a += 1
            ans.append(a)
        return ans
