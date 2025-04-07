class Solution:
    def reverseBits(self, n: int) -> int:
        x = bin(n)[::-1][:-2]
        x = x + "0"*(32 - len(x))
        return int(x, 2)