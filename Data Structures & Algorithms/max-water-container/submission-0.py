class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            currArea = min(heights[l], heights[r]) * width
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l+=1
                r-=1
        return maxArea