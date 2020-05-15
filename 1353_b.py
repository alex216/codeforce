t = int(input())
while t:
    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = sorted(list(map(int,input().split())),reverse = True)

    for i in range(k):
        if a[i] >= b[i]:break
        a[i] = b[i]
    print(sum(a))
    t -= 1
