# 평균값 구하기
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    L = input()
    line = L.split(" ")
    Sum = 0
    for i in range(len(line)):
        if 0 <= int(line[i]) <= 10000:
            Sum += int(line[i])
    avg = round(Sum/len(line))
    print('#{} {}'.format(test_case, avg))
