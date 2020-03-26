# 더블더블
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력
N = 8
if N <= 30:
    for i in range(N + 1):
        print('{}'.format(2**i), end=' ')
