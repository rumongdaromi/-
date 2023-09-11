import sys
arr = []
a = int(sys.stdin.readline())
# for i in range(a):
#     arr.append(int(sys.stdin.readline()))

b = str(sys.stdin.readline())
b = b.split()

b = list(map(int,b))
count = 0
score = 0
for (j) in b:
    count = 0
    for i in range(1,j+1):
        if j % i == 0:
            count += 1
    if count == 2:
        score += 1
        
print(score)
    
    
