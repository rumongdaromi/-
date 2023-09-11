import sys
n = str(sys.stdin.readline())
n = n.split()
n = list(map(int,n))


m = str(sys.stdin.readline())
m = m.split()
m = list(map(int,m))



list_n = []
list_m = []

for i in m:
    for j in m[m.index(i) + 1 :]:
        for k in m[m.index(j) + 1:]:
            list_n.append(i + j + k)


for i in list_n:
    if i <= n[1]:
        list_m.append(i)
print(max(list_m))
