#점수 계산

n = int(input())
a = list(map(int, input().split()))
cnt = 0
res = 0

for i in range(n):
    if a[i] == 1 and cnt == 0:
        cnt = 1
        res += cnt
        continue
    elif a[i] ==1 and cnt != 0:
        cnt += 1
        res += cnt
        continue
    else:
        cnt = 0

print(res)

'''
cnt=0
sum=0
for i in range(n):
    if a[i]==1:
        cnt=cnt+1
        sum=sum+cnt
    else:
        cnt=0

print(sum)
'''
