import sys

input = sys.stdin.readline

n = int(input())
사람, 다른사람 = map(int, input().split())
m = int(input())
result = 0

촌수 = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(1, m + 1):
    a, b = map(int, input().split())
    촌수[a].append(b)
    촌수[b].append(a)  
    
print(촌수)
print(visited)
count = 0
def DFS(v,count,촌수,visited):
    global result
    count += 1
    visited[v] = True
    
    if v == 다른사람:
        result = count
    for i in 촌수[v]:
        if not visited[i]:
            DFS(i,count,촌수,visited)
    


DFS(사람,count,촌수,visited)

if result == 0:
  print(-1)
else:
  print(result -1)
  
#print(result)
