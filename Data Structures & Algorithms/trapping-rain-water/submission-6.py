class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        lm = height[l]
        rm = height[r]
        vol = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                vol += lm - height[l]
            elif rm < lm:
                r -= 1
                rm = max(rm, height[r])
                vol += rm - height[r]
            else:
                l += 1
                r -= 1
                lm = max(lm, height[l])
                rm = max(rm, height[r])
                if l < r:
                    vol += lm - height[l] + rm - height[r]
                elif l == r:
                    vol += rm - height[r]

        return vol        