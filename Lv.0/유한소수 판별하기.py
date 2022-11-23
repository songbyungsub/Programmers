import math
def solution(a, b):
    answer = 0
    b = b // math.gcd(a,b)
    while True:
        flag = 0
        if b == 1:
            return 1
        if b % 2 == 0:
            b = b // 2
            flag = 1
        if b % 5 == 0:
            b = b // 5
            flag = 1
        if flag == 0 and b != 1:
            return 2


    return answer