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
# 다른 사람이 한 것
'''
for i in range (1, int(input())+1):
    d=input()
    a=d[4:6]
    b=d[6:]
    m=int(a)
    o=int(b)
    if m>12 or m*o<1 or o>int("303232332323"[m-1])+28:
        print(f'#{i} -1')
    else:
        print(f'#{i} {d[:4]}/{a}/{b}')
'''
'''
def calendar_validation(text):
  year = text[:4]
  month = text[4:6]
  day = text[6:]
  m_30 = [2, 4, 6, 9, 11]
  if int(month) > 12 or int(month) == 0 or int(day) > 31:
    return -1
  elif int(month) in m_30 and int(day) > 30:
    return -1
  elif int(month) == 2 and int(day) > 28:
    return -1
  else:
    return year+"/"+month+"/"+day
 
T = int(input())
 
for case in range(1, T+1):
  text = input()
  res = calendar_validation(text)
  print("#%d"%(case), res)
'''
