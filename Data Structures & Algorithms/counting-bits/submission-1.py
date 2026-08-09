class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(n + 1):
            curr = i
            count = 0
            while curr:
                if curr & 1 == 1:
                    count += 1
                curr = curr >> 1
            res[i] = count
        return res
        