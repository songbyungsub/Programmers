def solution(bridge_length, weight, truck_weights):
    answer = 0
    being_truck = [0]*bridge_length
    sum_being=0
    while being_truck:
        answer+=1
        c=being_truck.pop(0)
        sum_being-=c
        if truck_weights:
            if sum_being+truck_weights[0]<=weight:
                a=truck_weights.pop(0)
                being_truck.append(a)
                sum_being+=a
            else:
                being_truck.append(0)
    
    return answer