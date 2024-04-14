def solution(cards1, cards2, goal):
    '''
    카드 뭉치 두 개
    카드에 적힌 단어들을 사용하여 순서의 단어 배열
    
    조건
    원하는 카드 뭉치에서 카드 순서대로 한 장씩 사용
    한 번 사용한 카드 사용 불가
    카드를 사용하지 않고 다음 카드 넘어갈 수 없음
    기존에 주어진 카드 뭉치의 단어 순서 변경 불가
    
    카드 뭉치 길이 -> 1 ~ 10
    카드 내 단어 길이 -> 1 ~ 10
    조합 리스트 길이 -> 2 ~ 카드 뭉치 2개 합
    
    예시
    cards1 = ["i", "drink", "water"], cards2 = ["want", "to"]
    goal = ["i", "want", "to", "drink", "water"]
    
    풀이 과정
    goal가 cards1,2에 순차적으로 적용되었는지 확인 필요
    goal에서 값을 2개씩 뽑아내서 일치하는 지 여부만 판단하면 될 듯
    '''
    
    for word in goal:
        if len(cards1) > 0 and word in cards1[0]:
            cards1.remove(cards1[0])
        elif len(cards2) > 0 and word in cards2[0]:
            cards2.remove(cards2[0])
        else:
            return 'No'
    return 'Yes'

# cards1 = ["i", "drink", "water"]
# cards2 =["want", "to"]	
# goal = ["i", "want", "to", "drink", "water"]

cards1 = ["i", "water", "drink"]	
cards2 = ["want", "to"]	
goal = ["i", "want", "to", "drink", "water"]

answer = solution(cards1, cards2, goal)
print(answer)