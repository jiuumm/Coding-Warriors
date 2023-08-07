'''
기준 데이터를 설정하고
그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.
'''
array=[5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    #원소가 하나인 경우 종료
    if start>= end:
        return
    pivot = start
    left= start+1
    right= end
    while(left<=right):
        #피벗보다 큰 데이터를 찾을 때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right -=1
        #엇갈렸다면 right(오른쪽에서 오는 놈->작은 놈)과 피벗 값을 바꾼다.
        if(left>right):
            array[right], array[pivot]= array[pivot], array[right]
        else:
            array[left],array[right] = array[right], array[left]
    #분할 이후, 왼쪽 부분과 오른쪽 부분에서 다시 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

#더 간단한 코드!    
def quick_sort2(array):
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]
    
    #분할의 왼쪽 부분
    left_side = [x for x in tail if x<= pivot]
    #분할의 오른쪽 부분
    right_side = [x for x in tail if x> pivot]    
    
    return quick_sort2(left_side)+ [pivot]+ quick_sort2(right_side)

    
quick_sort(array,0, len(array)-1)
quick_sort2(array)
print(array) 
