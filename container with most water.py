class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxArea = 0
        while l<r:
            h = min(height[l], height[r])
            w = r-l
            maxArea = max(maxArea,h*w)
            if height[l]>height[r]:
                r -= 1
            elif height[l]<height[r]:
                l += 1
            else:
                l+=1
        return maxArea
