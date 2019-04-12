from math import sqrt

def prime(a):
    if a < 2:
        return False
    for i in range(2, int(sqrt(a))+1):
        if a%i == 0:
            return False
    return True

n = int(input())
cnt = 0

a = list(map(int, input().split()))
for i in a:
    if prime(i) == True:
        cnt += 1

print(cnt)

# def is_prime(x):
#     if x < 2:
#         return False
#     i = 2
#     while i*i <= x:
#         if x % i == 0:
#             return False
#         i += 1
#     return True
#
# n = int(input())
# a = list(map(int,input().split()))
# ans = 0
# for x in a:
#     if is_prime(x):
#         ans += 1
# print(ans)