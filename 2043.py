# 서랍의 비밀번호
import sys
sys.stdin = open('input8.txt', 'r')

T = input().split(' ')
P = T[0]
K = T[1]
if 000 <= int(P) <= 999:
    print(int(P) - int(K) + 1)
