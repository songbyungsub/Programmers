def solution(price, money, count):
    answer = -1
    total = 0
    i = 1
    while count > 0:
        total += price * i
        count -= 1
        i+= 1
    if money >= total: answer =0
    else: answer = total -money
    return answer