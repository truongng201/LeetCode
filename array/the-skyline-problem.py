class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def div_and_con(arr):
            if len(arr) == 1:
                return [[arr[0][0], arr[0][2]], [arr[0][1], 0]]
            
            mid = len(arr) // 2
            left = div_and_con(arr[:mid])
            right = div_and_con(arr[mid:])
            
            # merging
            i, j = 0, 0
            h1, h2 = 0, 0
            ans = []
            while i < len(left) or j < len(right):
                x = 0
                if i >= len(left):
                    ans+= right[j:]
                    break
                if j >= len(right):
                    ans+= left[i:]
                    break
                if left[i][0] < right[j][0]:
                    x, h1 = left[i]
                    i += 1
                elif left[i][0] > right[j][0]:
                    x, h2 = right[j]
                    j += 1
                else:
                    h1 = left[i][1]
                    h2 = right[j][1]
                    x = left[i][0]
                    i += 1
                    j += 1
                h = max(h1, h2)
                if ans and ans[-1][1] == h:
                    continue
                ans.append([x, h])
            
            return ans
        return div_and_con(buildings)