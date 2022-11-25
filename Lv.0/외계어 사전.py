def solution(spell, dic):
    answer = 2
    spell.sort()
    for i in dic:
        if len(spell) == len(i):
            result = sorted(list(i))
            if spell == result: answer = 1
            
    return answer