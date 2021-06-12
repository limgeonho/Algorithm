#뒤집은 소수

#숫자 거꾸로 출력하기(마지막 자릿수부터 거꾸로 누적)
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res*10 + t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())

a = list(map(int, input().split()))

for i in a:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')