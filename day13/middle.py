ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_sorted(idx, n, string, strings):
    if idx < 0:
        return 0
    if ALPHABET.index(string[n]) > ALPHABET.index(strings[idx+1][n]):
        strings[idx] = strings[idx+1]
        strings[idx+1] = string
        alphabet_sorted(idx-1, n, string, strings)
    elif ALPHABET.index(string[n]) == ALPHABET.index(strings[idx+1][n]):
        strings[idx], strings[idx+1] = sorted(strings[idx:idx+2])
        alphabet_sorted(idx-1, n, string, strings)
    return strings

def solution(strings, n):
    for idx, string in enumerate(strings):
        if len(strings)-1 == idx:
            break
        strings = alphabet_sorted(idx, n, string, strings)
    return strings

strings = ["sun", "bed", "car"]
n = 1
solution(strings, n)