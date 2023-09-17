import readline
import sys
n = int(input())
b = str(input())
min_time = 0
b = b.split(' ')
b = list(map(int, b))


b.sort()

# for i in range(n):
#     a = b[0]
#     a2 = a+(b[i+1])
#     a3 = a2 + (b[i+2])
#     a4 = a3 + (b[i+3])
#     a5 = a4 + (b[i+4])
# a = b[0]
# a2 = b[0]+(b[1])
# a3 = b[0] + (b[1]) + (b[2])
# a4 = b[0] + (b[1]) + (b[2]) + (b[3])
# a5 = b[0] + (b[1]) + (b[2]) + (b[3]) + (b[4])


c = [0]*n

c[0] = b[0]
for i in range(1,n):
    c[i] = c[i-1] + b[i]

for i in c:
    min_time += i
print(min_time)
    