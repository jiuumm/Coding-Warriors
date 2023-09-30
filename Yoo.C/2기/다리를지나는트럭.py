from collections import deque
def solution(bridge_length, weight, truck_weight):
    truck_weight= deque(truck_weight)
    #다리를 건너는 트럭
    bridge = deque([0 for _ in range(bridge_length)])
    time = 0
    
    bridge_weight = 0
    #bridge = [0,0]
    #bridge = [7]
    #bridge = [0]
    while len(bridge) != 0:
        out =  bridge.popleft()
        bridge_weight -= out
        time+=1
        if truck_weight:
            if bridge_weight+ truck_weight[0] <= weight:
                left=truck_weight.popleft()
                bridge_weight+= left
                bridge.append(left)
        else:
            bridge.append(0)
    return time