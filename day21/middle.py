def solution(keymap, targets):
    '''
    keymap -> 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열
    targets -> 문자열들이 담긴 배열
    targets 문자열 누르려면 최소 몇 번 눌러야 하는지
    
    제약 사항
    keymap, targets의 길이 -> 1 ~ 100
    keymap, targets의 원소 길이 -> 1 ~ 100
    keymap, targets의 무조건 대문자

    예시
    keymap=["ABACD", "BCEFD"], targets=["ABCD","AABB"]
    A -> 1번키 1, B -> 2번키 1, C -> 2번키 2, D -> 1번키 5(1+1+2+5)
    A -> 1번키 1, A -> 1번키 1, B -> 2번키 1, B -> 2번키 1(1+1+1+1)
    
    풀이 과정
    keymap에서 가장 최소 값을 지닌 key 값을 찾아서 이를 target에 적용
    알파벳 순으로 index 조회해서 
    '''
    
    key_dict = {}
    for key in keymap:
        for idx, alphabet in enumerate(key):
            try:
                if key_dict[alphabet] > idx+1:
                    key_dict[alphabet]=idx+1
            except:
                key_dict[alphabet]=idx+1
    
    answer = []
    for target in targets:
        cnt = 0
        try:
            for alphabet in target:
                cnt += key_dict[alphabet]
        except:
            cnt = -1
        answer.append(cnt)
        
    return answer

keymap=["ABACD", "BCEFD"]
targets=["ABCD","AABBKNA"]

solution(keymap, targets)