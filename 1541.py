m = input().split('-')
s = 0
for i in m[0].split('+'): 
    s+= int(i)

for i in m[1:]:
    for j in i.split('+'):
        s -= int(j)
 
print(s)