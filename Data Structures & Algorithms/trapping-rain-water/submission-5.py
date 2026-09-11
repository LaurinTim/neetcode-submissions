class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        l = 0
        vol = 0

        while l < len(height) - 2:
            while l < len(height) - 2 and (height[l] == 0 or height[l + 1] >= height[l]):
                l += 1

            r = l + 2
            w = min(len(height) - 1, r)
            while r < len(height) and height[r - 1] < height[l]:
                if height[r] > height[w]:
                    w = r
                r += 1

            if height[w] == 0:
                break
            
            h = min(height[l], height[w])
            while l < w:
                vol += max(0, h - height[l])
                l += 1
            
        return vol

