def solution(order):
    order = str(order)
    answer=0
    answer +=order.count('3')
    answer +=order.count('6')
    answer +=order.count('9')
    return answer