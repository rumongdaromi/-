#바닥장식
# 같은 행 -가 2개  -- 일 때 1개로  ㅣ
# 같은 열 ㅣ 가 위아래 2개 일 때    ㅣ 일 떄 1개로 

# 1. 같은게 나오면 계속 해서 옆으로 간다
# 2. 다른게 나오면 함수를 호출해서 y+1 열에서 1번에서 멈춘 곳과 같은 곳과 같으면 또 호출하고 있으면 또 호출 없을 때까지 반복 그리고 도착한 곳은 다른 걸로 표기? 하면 되지않을까
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
count = 0
x,y = 0,0
graph = []
for i in range(N):
    graph.append(list(input().strip()))  # 개행 문자 제거


def 수직탐색(x,y):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] != '-':
        return 
    
    if graph[x][y] == '-':
        graph[x][y] = True
        수직탐색(x,y+1)
        return True

    return False


def 수평탐색(x,y):
    if x < 0 or x >= N or y < 0 or y >= M or graph[x][y] != '|':
        return
    if graph[x][y] == '|':
        graph[x][y] = True
        수평탐색(x+1,y)
        return True
    
    return False


# N,M = 6,9
# x =9 y = 6
for i in range(N):
    for j in range(M):
        
        if 수직탐색(i,j) == True:
                # 6,9
            count += 1
            

for i in range(M):
    for j in range(N):
        #6,9
        if 수평탐색(j,i) == True:
            count += 1
    
print(count)  
  

