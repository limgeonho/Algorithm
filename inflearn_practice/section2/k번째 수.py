#k번째 수

t = int(input())

for _ in range(t):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print(a[k-1])