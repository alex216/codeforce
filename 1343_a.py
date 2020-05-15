a = []
for k in range(2,31):
    a.append(2**k-1)

t = int(input())
for _ in range(t):
    m = int(input())
    for d in a:
        if m%d == 0:
            print(m//d)
            break
