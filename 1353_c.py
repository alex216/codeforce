t = int(input())
M = 250003
a = [0] * M
for i in range(1,M-1):
    a[i+1] = a[i] + 8 * i**2

while t:
    print(a[(int(input())+1)//2])
    t -= 1

