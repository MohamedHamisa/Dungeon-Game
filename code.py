class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m-1][n] = dp[m][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j], 1)
        return dp[0][0]

'''
This solution uses dynamic programming to solve the problem. The main idea is to build a 2D array dp to store the minimum initial health required at each position to reach the bottom-right corner. We start from the bottom-right corner and work our way backwards to the top-left corner.

At each position, we take the minimum of the minimum initial health required at the position below and the position to the right, and subtract the dungeon value at the current position. If the result is less than or equal to 0, we set it to 1 (since the knight needs to have at least 1 health point to be alive). Finally, we return the value at the top-left corner of the dp array.

To handle the boundary cases, we add an extra row and an extra column to the dp array, and set them all to infinity except for dp[m-1][n] and dp[m][n-1], which are set to 1.

This solution has a time complexity of O(mn) and a space complexity of O(mn).
'''
