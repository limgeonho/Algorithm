#대표값

n = int(input())
a = list(map(int, input().split()))
min = 2147000000

#나누기(/)연산을 한 번 하게 되면 소수점이 붙는다
avg = sum(a) / n
#무조건 0.5를 더해서 반올림할 수 있는 수를 만든다
avg = avg + 0.5
#강제로 소수점을 없애버린다
avg = int(avg)

#enumerate()를 사용하면 idx와 해당 값으로 return 한다
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif min == tmp:
        if x > score:
            score = x
            res = idx + 1
            
print(avg, res)