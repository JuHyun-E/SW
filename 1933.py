# 간단한 N의 약수
N = 10
if 1 <= N <= 1000:
    for i in range(1, N + 1):
        measure = N % i
        if measure == 0:
            print(i, end=' ')
