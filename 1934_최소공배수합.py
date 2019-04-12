def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a%b)

c = int(input())

for i in range(c):
    a, b = map(int, input().split())
    g = gcd(a, b)
    l = (a*b)//g
    print(l)