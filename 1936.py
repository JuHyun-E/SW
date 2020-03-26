# 1대1 가위바위보
# 가위는 1, 바위는 2, 보는 3
# A가 이기면 A, B가 이기면 B를 출력
import sys
sys.stdin = open('input11.txt', 'r')
A, B = map(int, input().split(' '))
if (A == 1 and B == 3) or (A == 2 and B == 1) or (A == 3 and B == 2):
    print('A')
else:
    print('B')
