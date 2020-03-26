# N줄 덧셈
# 1부터 주어진 숫자만큼 모두 더하기
T = 10
s = 0
if T < 10000:
    for i in range(T + 1):
        s += i
    print(s)
