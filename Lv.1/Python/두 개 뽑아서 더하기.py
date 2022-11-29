from itertools import combinations
def solution(numbers):
    answer = list(combinations(numbers,2))
    result = []
    for i in answer:
        result.append(sum(i))
    result2= list(set(result))
    result2.sort()
    return result2