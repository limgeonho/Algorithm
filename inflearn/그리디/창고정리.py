#창고정리

n = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0]+=1
    a[n-1]-=1
    a.sort()

print(a[n-1] - a[0])