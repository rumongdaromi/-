#바닥장식
# 같은 행 -가 2개  -- 일 때 1개로  ㅣ
# 같은 열 ㅣ 가 위아래 2개 일 때    ㅣ 일 떄 1개로 

# 1. 같은게 나오면 계속 해서 옆으로 간다
# 2. 다른게 나오면 함수를 호출해서 y+1 열에서 1번에서 멈춘 곳과 같은 곳과 같으면 또 호출하고 있으면 또 호출 없을 때까지 반복 그리고 도착한 곳은 다른 걸로 표기? 하면 되지않을까
import sys
input = sys.stdin.readline

N,M = map(int,input().split())


#visited = [[False] * M  for i in range(N)]    
count = 0
x,y = 0,0
graph = []
for i in range(N):
    graph[i] = list(input().replace('\n',''))  # 개행 문자 제거

#graph[0].remove()
count = 0 
dx = [1,0,0,0]
dy = [0,0,1,0]


print(graph)
def DFS(x,y):
    global count
    
    if x >= 0 and x < M and y >= 0 and y < N: #밖으로 나가지 않게하기 위함
        if graph[x][y] == '-' and graph[x+1][y] == '-':
            count += 1
            DFS(x+1,y)
            
        elif graph[x][y] == '|' and graph[x][y+1] == '|':
            count += 1
            DFS(x,y+1)
