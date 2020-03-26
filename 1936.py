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

# 다른 사람이 한 것??? 이해못함
'''
s = input().split(" ")
A=int(s[0])
B=int(s[1])
if (A+1)%3 == (B%3):  # 2, 3, 4 -> 2, 0, 1 == 1, 2, 0
    print("B")
elif (B+1)%3 == A%3:
    print("A")
else:
    print("무승부")
'''