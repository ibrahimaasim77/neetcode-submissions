class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = -1
        left = 0
        right = len(heights) - 1
        count = len(heights)
        for i in range(count):
            value = min(heights[left], heights[right])
            max1 = value * (right - left)
            if max1 >= max:
                max = max1
            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1

        return max