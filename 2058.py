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

# 다른 사람이 한 것
'''
T = input()
sum = 0
for i in T:
    sum += int(i)
print(sum)
'''
