from collections import Counter

def firstUniqChar(s: str) -> int:
    count = Counter(s)
    print(count)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i 
    return -1


print(firstUniqChar("loveleetcode"))

