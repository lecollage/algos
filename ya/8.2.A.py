M = int(input())

max=1000000
dp=[max]*M
dp[0]=1
dp[2]=1
dp[3]=1

for i in range(1, M):
    dp[i] = min(dp[i], min(dp[i-1], dp[i-3] if i > 2 else max, dp[i-4] if i > 3 else max) + 1)

print(dp[len(dp)-1])