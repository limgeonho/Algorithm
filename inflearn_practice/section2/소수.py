#소수(에라토스테네스의 체)

n = int(input())

a = [0] * (n+1)

cnt = 0

for i in range(2, n+1):
    if a[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            a[j] = 1

print(cnt)