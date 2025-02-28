class Solution:
    def getMinimumCost(self, n, left, right, weight):
        self.left = left
        self.right = right
        self.n = n
        self.dp = [[[-2 for _ in range(right + 1)] for _ in range(n)] for _ in range(n)]
        self.sum = [0] * n
        for i in range(n):
            self.sum[i] = (self.sum[i - 1] if i > 0 else 0) + weight[i]

        # Start DFS to compute the result
        self.dfs(0, n - 1, 1)

        if self.dp[0][n - 1][1] <= -1:
            return 0
        return self.dp[0][n - 1][1]

    def dfs(self, s, e, k):
        if self.dp[s][e][k] >= -1:
            return self.dp[s][e][k]

        if e - s + 1 < k:
            self.dp[s][e][k] = -1
        elif s == e:
            self.dp[s][e][k] = 0
        else:
            self.dp[s][e][k] = float('inf')

            if k == 1:
                m = min(self.right, e - s + 1)
                for i in range(self.left, m + 1):
                    v = self.dfs(s, e, i)
                    if v != -1:
                        self.dp[s][e][k] = min(self.dp[s][e][k], v)
                if self.dp[s][e][k] != float('inf'):
                    self.dp[s][e][k] += self.sum[e] - (self.sum[s - 1] if s > 0 else 0)
                else:
                    self.dp[s][e][k] = -1
            else:
                for i in range(s + 1, e + 1):
                    v1 = self.dfs(s, i - 1, k - 1)
                    v2 = self.dfs(i, e, 1)
                    if v1 != -1 and v2 != -1:
                        self.dp[s][e][k] = min(self.dp[s][e][k], v1 + v2)

        return self.dp[s][e][k]

sol = Solution()
arr = [1,2,3,4,5,6]
left = 3
right = 4
n = 6
print(sol.getMinimumCost(n,left,right,arr))
