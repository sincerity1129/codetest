def solution(N,A,B):
    '''
    토너먼트 형식
    N명의 참가자 -> 1 ~ N 순서대로 배정
    1<->2 , 3<->4, N-1<->N
    N -> 게임 참가자 수
    A -> 참가자 번호
    B -> 경쟁자 번호
    
    제한사항
    N -> 2의1승 ~ 2의20승
    A,B <= N
    
    예시
    N=8, A=4,B=7
    1,2 // 3,4 // 5,6 // 7,8
    1,4 // 5,7
    4,7
    3번 만에 만남
    
    풀이과정
    2의 n의 절반 넘어갈 경우 마지막에 만남
    2의 n의 절반의 절반 넘어가면 n-1에서 만남 이를 활용하면 값 나올 듯
    예시에서 A는 N의 절반에 포함 B는 포함되지 않아 3번째 만에 만남
    이 같은 방법 활용해서 N에서 2를 나눈 값 중 하나는 안에 포함 하나는 미포함 할 때
    그 승을 값으로 넣으면 됨
    '''
#     def number2log(num1, num2):
#         if math.log(num1, 2) == int(math.log(num1, 2)):
#             location1 = math.log(num1, 2)
#         else:
#             location1 = int(math.log(num1, 2))+1
            
#         if math.log(num2, 2) == int(math.log(num2, 2)):
#             location2 = math.log(num2, 2)
#         else:
#             location2 = int(math.log(num2, 2))+1

            
#         if location1 > location2:
#             return location1
#         elif location1 < location2:
#             return location2
#         elif location1 == location2:
#             return number2log(math.pow(2, location1)-num1, math.pow(2, location2)-num2)
# 위의 값 4개 정도 런타임 에러 뜨는데 이유는 모르겠음
    def number2log(num1, num2, count):
        global result_count 
        
        if num1 == num2:
            result_count = count
            return result_count
        return number2log((num1+1)//2, (num2+1)//2, count+1)
    
    return number2log(A//2,B//2, 1)
    
N, A, B = 256, 4, 7
result = solution(N,A,B)
print(result)