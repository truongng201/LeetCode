class Solution:
    def myPow(self, x: float, n: int) -> float:
        def new_pow(x, n):
            if n == 0:
                return 1
            if n == 1 or n == -1:
                return x ** n
            mid = n // 2
            remain = n % 2
            a = new_pow(x, mid)
            a *= a
            a *= x ** remain
            return a
        return round(new_pow(x, n), 5)