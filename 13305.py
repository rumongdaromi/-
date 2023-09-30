a = int(input())
r = list(map(int,input().split())) #거리
c = list(map(int,input().split())) #기름값

# 현재 도착한 도시 기준 앞으로 남은 도시 중 더 싼값이 있다면 거기까지만 기름을 구매 

ans = 0
val = c[0]
for i in range(a-1):
    if val > c[i]: # 현재 도시보다 코스트가 낮은 곳이 있을 때 까지 비교
        val = c[i] # 낮은곳에 도착하면 작은 코스트로 바꿔줌
    ans += val * r[i] #현재 도시보다 작은 코스트가 나올 때 까지 더함 
print(ans)




    

    


             
        
    
            



