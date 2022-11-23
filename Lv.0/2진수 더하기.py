def solution(bin1, bin2):
    answer = bin(int(bin1,6)+int(bin2,6))
    return answer[2:]