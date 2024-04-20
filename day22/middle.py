def solution(sequence, k):
    '''
    비내림차순으로 정렬된 수열에서 조건에 만족하는 수열
    기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함
    sequence=정수배열
    k=부분 수열의 합
    
    예시
    sequence=[1,2,3,4,5], k=7
    3+4 -> 7 인덱스로 보면 [2,3]
    
    짧은 인덱스
    sequence=[1,1,1,2,3,4,5], k=5
    1+1+1+2, 2+3, 5 -> 5 제일 짧은 것 [6,6]
    
    앞의 인덱스 값
    sequence=[2,2,2,2,2], k=6
    2+2+2 -> 6 제일 앞 인덱스 0~2
    
    제한 사항
    sequence 길이 -> 5 ~ 백만
    sequence 하나 원소 길이 -> 1 ~ 1000
    k의 범위 -> 5 ~ 백만
    k는 sequence의 부분 수열
    
    풀이과정
    인덱스 가장 작은 값부터 시작해서 점점 늘려가면서 값 확인
    인덱스 1개일 때 2개일 때 방식으로 늘려가기
    여기에서 중요한 건 사이의 값을 모두 더하는 것
    1개일 때 한칸 이동 2개일 때도 2칸 이동 이렇게 이동하면서 파악
    시간 초과 및 실패 에러
    
    시간초과의 경우 두개 세개 이렇게 늘리는 게 효율적으로 보임
    실패는 코드 다시 작성 후 확인 필요로 보임    
    '''
#     answer = []
    
#     range_idx = 0
#     list_count = len(sequence)
#     for first_idx in range(len(sequence)):
#         range_idx = first_idx+1
#         while True:
#             if list_count <= range_idx - first_idx:
#                 break
#             if k == sum(sequence[first_idx:range_idx]):
#                 answer=[sequence.index(sequence[first_idx]), range_idx-1]
#                 list_count = range_idx - first_idx
#                 break
#             elif range_idx >= len(sequence):
#                 break
#             range_idx += 1


    answer = []
    first_idx = 0
    range_idx = 0
    range_count = 1
    range_num = 1
    while True:
        if sequence.count(k) > 0:
            answer = [sequence.index(k), sequence.index(k)]
            break
        range_idx = first_idx+range_num
        if k == sum(sequence[first_idx:range_idx]):
            answer = [first_idx, range_idx-1]
            break
            
        elif range_idx == len(sequence):
            first_idx = 0
            range_num += 1
            continue
        
        first_idx += range_count
        range_idx += range_count
            
    return answer

# sequence=[1, 2, 3, 4, 5]
# k=7

sequence=[1, 1, 1, 2, 3, 4, 5]
k=5

# sequence=[2, 2, 2, 2, 2]
# k=6

solution(sequence, k)