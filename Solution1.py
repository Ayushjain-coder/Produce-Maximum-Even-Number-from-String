l = list(input())
p = set()
i = 0
flag = 0
for i in l:
    if i >= '0' and i <= '9':
        p.add(i)

l = sorted(list(p))
for i in l:
    if int(i)%2 == 0:
        l.remove(i)
        flag = 1
        break
    
if flag == 0:
    print(-1)
else:    
    l.reverse()
    l.append(i)

    print("".join(l))
