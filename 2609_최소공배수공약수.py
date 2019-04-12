def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

a, b = map(int, input().split())

g = gcd(a, b)
l = a*b//g
# //은 소수점 버리고 정수만

print(g)
print(l)
