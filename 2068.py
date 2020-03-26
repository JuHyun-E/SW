# 최대수 구하기
import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    L = input()
    line = L.split(" ")
    Max = 0
    for i in range(0, len(line) - 1):
        if Max < int(line[i]):
            Max = int(line[i])
        else:
            continue
    print('#{} {}'.format(test_case, Max))


# 다른 사람이 한 것
'''
case = int(input())
for i in range(case):
    result = 0
    t = input().split(' ')
    k = []
    for j in t:
        k.append(int(j))
    result = max(k)

    print("#{} {}".format(i + 1, result))
'''
