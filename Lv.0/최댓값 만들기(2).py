from itertools import combinations
def solution(numbers):
    answer = []
    arr = list(combinations(numbers,2))
    for i in range(len(arr)):
        answer.append(arr[i][0]*arr[i][1])
    
    return max(answer)
# def solution(numbers):
#     numbers = sorted(numbers)
#     return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2])

solution([1, 2, -3, 4, -5])