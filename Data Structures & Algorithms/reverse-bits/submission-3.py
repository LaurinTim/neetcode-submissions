class Solution:
    def reverseBits(self, n: int) -> int:
        bin_list = []
        while n != 0:
            bin_list.append(n % 2)
            n = n >> 1
        res = 0
        for i, val in enumerate(bin_list):
            if val == 1:
                res += 2**(31 - i)
        return res
            