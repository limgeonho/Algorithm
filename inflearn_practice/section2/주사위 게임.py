#주사위 게임

n = int(input())

p = [0] * (n+1)

max = -2147000000

for i in range(1, n+1):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        p[i] = 10000 + a * 1000
    elif a == b:
        p[i] = 1000 + a * 100
    elif b == c:
        p[i] = 1000 + b * 100
    elif a == c:
        p[i] = 1000 + a * 100
    else:
        tmp = []
        for _ in range(n):
            tmp.append(a)
            tmp.append(b)
            tmp.append(c)

        tmp.sort()     
        p[i] = tmp[2] * 100    

    if p[i] > max:
        max = p[i] 

print(max)  
'''
max=0
res=0
n=int(input())
for i in range(n):
    tmp=input().split() 
    tmp.sort() 
    a, b, c=map(int, tmp)
    if a==b and b==c:
        money=10000+(a*1000)
    elif a==b or a==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100
    if money > res:
        res=money

print(res)
'''