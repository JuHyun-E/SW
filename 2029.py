# 몫과 나머지 출력하기
import sys
sys.stdin = open('input9.txt', 'r')
T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if 1 <= a and b <= 10000:
        quotient = a//b
        remain = a % b
        print('#{} {} {}'.format(test_case, quotient, remain))
