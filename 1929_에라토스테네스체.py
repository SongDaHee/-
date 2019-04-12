m, n = map(int, input().split())
check = [False] * (n+1) # 0은 False 1은 True
check[0] = check[1] = True

for i in range(2, n+1):
    if not check[i]:
      j = i+i
      while j <= n:
          check[j] = True
          j += i

for i in range(m, n+1):
    if check[i] == False:
        print(i)

# import java.util.*;
#
# public class Main {
# public static void main(String args[]) {
# Scanner sc = new Scanner(System.in);
# int n = sc.nextInt();
# int m = sc.nextInt();
# boolean[] check = new boolean[m+1];
# check[0] = check[1] = true;
# for (int i=2; i*i <= m; i++) {
# if (check[i] == true) {
# continue;
# }
# for (int j=i+i; j<=m; j+=i) {
#     check[j] = true;
# }
# }
# for (int i=n; i<=m; i++) {
# if (check[i] == false) {
# System.out.println(i);
# }
# }
# }
# }

# MAX = 1000000
# check = [0]*(MAX+1)
# check[0] = check[1] = True
#
# for i in range(2, MAX+1):
#     if not check[i]:
#         j = i+i
#         while j <= MAX:
#             check[j] = True
#             j += i
# m, n = map(int,input().split())
# for i in range(m, n+1):
#     if check[i] == False:
#         print(i)