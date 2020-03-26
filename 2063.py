# 중간값 찾기
# 입력으로 N개가 주어졌을 때 중간값 찾기
import sys
sys.stdin = open('input3.txt', 'r')

N = int(input())
L = input()
num = L.split(' ')
s = []
if (N % 2 == 1) and (9 <= N <= 199):
    for i in range(N):
        s.append(int(num[i]))
    s.sort()
    mid = int(len(s)/2)
    print(s[mid])

# 다른 사람이 한 것
'''
a = input()
x = list(map(int, input().split()))
x.sort()
print(x[int(a)//2])
'''
