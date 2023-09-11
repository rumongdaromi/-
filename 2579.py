n = int(input())
f = [0]*301
dp =[0]*301
for i in range(1,n+1):
    f[i] = int(input())
    

dp[1] = f[1]
dp[2] = f[1] + f[2]
dp[3] = max(f[1] + f[3],f[2]+f[3])
for i in range(4,n+1):
    dp[i] = max(dp[i-2] + f[i],dp[i-3] + f[i-1] + f[i])
    
print(dp[n])
