#230929(FRI) / 큐 / Lv.2
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리를 표현하는 큐, 0으로 초기화
    current_weight = 0
    
    while truck_weights:
        time += 1
        
        # 다리에서 트럭을 빼고 현재 무게에서 빼기
        current_weight -= bridge.popleft()
        
        # 대기 중인 트럭이 다리에 올라갈 수 있는지 확인
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)  # 트럭을 대기시키기 위해 0을 추가
            
    # 마지막 트럭이 다리를 건널 때의 시간을 더해줌
    time += bridge_length
    
    return time
