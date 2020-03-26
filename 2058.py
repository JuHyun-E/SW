# 자릿수 더하기
import sys
sys.stdin = open('input4.txt', 'r')

N = int(input())
if 1 <= N <= 9999:
    strN = str(N)
    Sum = 0
    for i in range(len(strN)):
        Sum += int(strN[i])
    print(Sum)
