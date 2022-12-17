from itertools import combinations
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer =0
    lst = list(combinations(nums,3))
    sum_ = []
    for i in lst:
        sum_.append(sum(i))
    for i in sum_:
        if prime(i):
            answer+=1
    return answer