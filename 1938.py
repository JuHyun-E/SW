# 아주 간단한 계산기
# 사칙연산 + , - , * , / 순서로 연산한 결과를 출력한다.
import sys
sys.stdin = open('input10.txt', 'r')
a, b = map(int, input().split(' '))
if 1 <= a and b <= 9:
    print('{}\n{}\n{}\n{}'.format(a + b, a - b, a * b, a // b))
