class Solution:
    def trap(self, height):
        n = len(height)
        maxLeft = [0]*n
        maxRight = [0]*n
        minLR = [0]*n
        result = [0]*n
        for i in range(n):
            maxLeft[i] = max(height[:i+1])
            maxRight[i] = max(height[i:])
            minLR[i] = min(maxLeft[i], maxRight[i])
            result[i] = minLR[i] - height[i]
        return sum(result)



        
            

s = Solution()
print(s.trap([0,2,0,3,1,0,1,3,2,1]))