import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

x,y = map(int,input().split())
nums = [x]

sum = 0
for i in str(nums[-1]):
    sum += int(i)**y

graph = []
graph.append(x)

def D(x,y):
    sum = 0
    nums = [x]
    for i in str(nums[-1]):
        sum += int(i)**y
        
    if sum in graph:
        graph.append(sum)
        print(graph.index(sum))
        return 1
        
    graph.append(sum)
    if D(sum,y) == 1:
        return 1
        
    return 0 
D(x,y)
