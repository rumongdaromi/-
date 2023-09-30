# N = list(map(int,input().split())) #거리
# K = []
# for i in range(N[0]):
#     K.append(int(input()))
    
# # 일단 크기비교를해서 가장 근접한 값을 빼준다면 되지않을까 ?
# #4200
# # 가장 가까운 (가장 큰 수 and N[1]보다는 작은 수)
# a = 0
# count = 0
# while N[1] != 0:
#     for i in range(len(K)):
#         if K[i] <= N[1]:
#             if a < K[i]:
#                 a = K[i]
        
            
            
#     if N[1] >= 0:
#         N[1] -= a
#         a = 0
#         count += 1
        
    
# print(count)
    
#     #리스트 중에서 N[1]보다 작은 것들중 가장 큰값을 빼줌 그리고 count를 증가시킴
    


import sys

N = list(map(int, input().split()))  # 거리
K = []
for i in range(N[0]):
    K.append(int(sys.stdin.readline()))

K.sort(reverse=True)

count = 0

for i in K:
    count += N[1] // i
    N[1] = N[1] % i
print(count)