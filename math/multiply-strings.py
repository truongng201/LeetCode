class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def karatsuba(x, y):
            if x < 10 and y < 10:
                return int(x) * int(y)
            n = max(len(str(x)), len(str(y)))
            m = n // 2
            
            a = x // (10 ** m)
            b = x % (10 ** m)
            c = y // (10 ** m)
            d = y % (10 ** m)
            
            z0 = karatsuba(b, d)
            z1 = karatsuba((a + b), (c + d))
            z2 = karatsuba(a, c)
            return (z2 * (10 ** (2 * m))) + ((z1 - z2 - z0) * (10 ** m)) + z0
        return str(karatsuba(int(num1), int(num2)))