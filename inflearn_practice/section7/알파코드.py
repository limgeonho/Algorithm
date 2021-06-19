#알파코드

#이 문제는 두 자리 숫자를 따로 분류해서 L+2를 해주는 것이 핵심... 한 자리 수와 두 자리수를 선택(O, X)문제
def DFS(L, P):
    global cnt
    if L == n:
        cnt+=1
        for j in range(P):
            print(chr(res[j] + 64), end='')
        print()

    else:
        for i in range(1, 27):
            if code[L] == i:
                res[P] = i
                DFS(L+1, P+1)
            elif i>=10 and code[L]==i//10 and code[L+1]==i%10:
                res[P] = i
                DFS(L+2, P+1)


code = list(map(int, input()))
n = len(code)
code.insert(n, -1)
res = [0] * (n+3)
cnt = 0
DFS(0, 0)
print(cnt)