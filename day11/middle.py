alphabet_dict = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
}
'''
문자열 -> s와 skip
자연수 -> index

s의 알파벳을 index 뒤의 알파벳으로 변경
index 넘어갈 경우 다시 a로 돌아감
skip의 알파벳 제외

s = "aukks", skip ="wbqd", index = 5
a는 b,d는 제외 되므로 5번째 뒤는 c,e,f,g,h -> h
나머지도 동일하게 하면
aukks -> happy

풀이과정
dict 만들어서 index를 key value를 알파벳으로 해서 하면 될 듯
skip의 경우 관련 값 찾아서 key 값 자체 제거
index 넘을 경우 환산하게 해서 계산 하면 결과 나올 듯

실패 -> k 값 제거 때문에 제대로 값이 안들어감
'''
s = "aukkwerfrwerswervwrewr"
skip = "wbxcqoqd"
index = 5
word_list = []

value_change = 1
for k in alphabet_dict.keys():
    if k in skip:
        alphabet_dict[k] = value_change
        continue
    alphabet_dict[k] = value_change
    value_change += 1

index_alphabet_dict= {alphabet_dict[k]: k for k, v in alphabet_dict.items()}
    

for word in s:
    index_change = int(alphabet_dict[word]+index) % len(index_alphabet_dict.keys())
    if index_change == 0:
        index_change = 19
    word_list.append(index_alphabet_dict[index_change][-1])


print(''.join(word_list))