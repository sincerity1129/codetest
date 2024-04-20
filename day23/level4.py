def solution(players, callings):
    '''
    선수가 추월했을 때 이름을 부름
    players -> 등수대로 담긴 문자열 배열
    callings -> 해설진이 부른 이름을 담은 문자열 배열
    이를 바탕으로 등수 배열에 담기
    
    제한 사항
    players 길이 -> 5 ~ 5만, 알파벳 소문자, 중복된 값X, 
    callings의 길이 -> 2 ~ 백만
    경주 진행중 1등인 선수 이름은 불리지 않음
    
    예시
    players=["mumu", "soe", "poe", "kai", "mine"]
    callings=["kai", "kai", "mine", "mine"]
    kai -> ["mumu", "soe", "kai", "poe", "mine"]
    kai -> ["mumu", "kai", "soe", "poe", "mine"]
    mine -> ["mumu", "kai", "soe", "mine", "poe"]
    mine -> ["mumu", "kai", "mine", "soe", "poe"]
    최종 등수 -> ["mumu", "kai", "mine", "soe", "poe"]
    
    풀이 과정
    중복 값이 없기 때문에 index 값 찾기
    그 전 값과 그 뒤 값 변경하면서 순차적으로 진행하면 될 듯
    
    리스트 값 찾아가면 시간이 오래 걸리는 문제가 발생
    index 찾아가는 방법을 빠르게 dict로 변환
    '''
    
    players_dict = {name:idx for idx, name in enumerate(players)}
    for name in callings:
        overtake = players_dict[name]
        players_dict[name] -= 1
        players_dict[players[overtake-1]] += 1
        players[overtake-1], players[overtake] = name, players[overtake-1] 
    
    return players


players=["mumu", "soe", "poe", "kai", "mine"]
callings=["kai", "kai", "mine", "mine"]
	
solution(players, callings)