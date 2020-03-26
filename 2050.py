# 알파벳을 숫자로 변환
import sys
sys.stdin = open('input6.txt', 'r')

T = input()
if len(T) <= 200:
    for c in T:
        print('{}'.format(ord(c) - 64), end=' ')
