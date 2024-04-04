'''
k = 한 상자에 담으려는 귤의 개수
tangerine = 모든 귤을 가진 리스트

k=6, tangerine=[1,3,2,5,4,5,2,3]
k를 판다고 할 때 서로 다른 종류가 최소일 때 찾기
2,3,5 -> 2개, 1,4 1개 // 결과 3

k=4, tangerine[1,3,2,5,4,5,2,3]
2,3,5 -> 2개, 1,4 1개 // 결과 2


풀이 과정
1. tangerine의 각 개수를 파악
2. 최대부터 더해 가면서 k개수 만큼 파악
3. 결과 도출
'''
k = 6
tangerine = [1,3,2,5,4,5,2,3]

from collections import defaultdict
tangerine_count_dict = defaultdict(int)

for tangerine_number in tangerine:
    tangerine_count_dict[tangerine_number] += 1

tangerine_count_dict = dict(sorted(tangerine_count_dict.items(), 
                                key=lambda item: item[1], reverse=True))

answer = 0
tangerine_count = 0
for value in tangerine_count_dict.values():
    if (k-tangerine_count) > 0:
        answer += 1
        tangerine_count += value
        if tangerine_count >= k:
            break
    elif tangerine_count > k:
        answer += 1
        break
