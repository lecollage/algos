M = int(input())

"""
+1
*2
*3
"""


max=1000000
dp=[max]*M
dp[0]=0
dp[1]=1
dp[2]=2
dp[3]=2

for i in range(1, M):
    one = dp[i-1]
    two = max
    three = max

    if i > 2 and i%2 == 0:
        two = dp[int(i/2)]

    if i > 3 and i%3 == 0:
        three = dp[int(i/3)]

    dp[i]=min(dp[i], min(one, two, three)+1)

print(dp)
print(dp[len(dp)-1])