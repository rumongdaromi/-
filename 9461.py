dp = [0] *101
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6,101):
    dp[i] = dp[i-1] + dp[i-5]
    
for i in b:
    print(dp[i])
    