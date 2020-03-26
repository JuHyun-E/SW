# 연월일 달력
import sys
sys.stdin = open('input5.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    line = input()
    month = line[4:6]
    day = line[6:]
    _list = [2, 4, 6, 9, 11]  # 28일 and 30일
    if int(month) > 12 or int(month) == 0 or int(day) > 31 or int(day) == 0:
        print('#{} {}'.format(test_case, -1))
    elif int(month) in _list and int(day) > 30:
        print('#{} {}'.format(test_case, -1))
    elif int(month) == 2 and int(day) > 28:
        print('#{} {}'.format(test_case, -1))
    else:
        print('#{} {}/{}/{}'.format(test_case, line[:4], month, day))
