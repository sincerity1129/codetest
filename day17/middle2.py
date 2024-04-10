def solution(food):
    '''
    매달 주어진 음식 빨리 먹는 푸드 파이트 대회
    한 선수는 왼쪽에서 오른쪽
    다른 선수는 오른쪽에서 왼쪽
    물을 먼저 먹는 선수가 승리
    
    food = [물, 칼로리 순서로 개수]
    
    풀이과정
    무조건 짝수로 개수 카운팅
    개수의 몫을 구해서 양 옆에 개수 카운팅
    '''
    food_list = ['0']
    for idx, food_count in enumerate(reversed(food)):
        calorie = len(food) - idx - 1
        if calorie == 0:
            continue
        distribution = int(food_count) // 2
        food_list = [str(calorie)*distribution] + food_list
        food_list.append(str(calorie)*distribution)
    
    answer = ''.join(food_list)
    return answer


food = [1, 3, 4, 6]
solution(food)