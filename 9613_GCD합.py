def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    n = a[0]
    a = a[1:]
    ans = 0
    for j in range(0,n-1):
        for k in range(j+1, n):
            ans += gcd(a[j], a[k])
    print(ans)

