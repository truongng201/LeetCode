class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = ""
        while i >= 0 or j >= 0:
            if j < 0:
                ans = str(int(num1[:i+1]) + add) + ans
                add = 0
                break
            if i < 0:
                ans = str(int(num2[:j+1]) + add) + ans
                add = 0
                break
            x = int(num1[i]) + int(num2[j]) + add
            if x >= 10:
                add = 1
                ans = str(x - 10) + ans
            else:
                ans = str(x) + ans
            i -= 1
            j -= 1
        if add == 1:
            ans = "1" + ans
        return ans