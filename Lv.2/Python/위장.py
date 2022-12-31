def solution(clothes):
    answer = 1
    dic = {}

    for item, category in clothes:
        if category not in dic:
            dic[category] = []
        dic[category].append(item)
    
    com = []
    for i in dic.values():
        com.append(len(i))
    for i in com:
        i +=1
        answer *= i
    return answer - 1



solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"],['white_sunglasses','eyewear'],['blue_pants','pants']])