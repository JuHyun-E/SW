# 큰 놈, 작은 놈, 같은 놈
# 2개의 수를 입력 받아 크기를 비교하여 등호 또는 부등호를 출력하는 프로그램
import sys
sys.stdin = open('input2.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    L = input()
    line = L.split(" ")
    if int(line[0]) > int(line[1]):
        compare = '>'
        print('#{} {}'.format(test_case, compare))
    if int(line[0]) < int(line[1]):
        compare = '<'
        print('#{} {}'.format(test_case, compare))
    if int(line[0]) == int(line[1]):
        compare = '='
        print('#{} {}'.format(test_case, compare))
