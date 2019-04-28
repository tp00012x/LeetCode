from collections import Counter

# def firstUniqChar(s: str) -> int:
#     count = Counter(s)
#     for i, ch in enumerate(s):
#         if count[ch] == 1:
#             return i 
#     return -1

# Runtime: 120 ms, faster than 63.38%

def firstUniqChar(s: str):
    count = Counter(s)
    
    index = 0
    for ch in s:
        if count[ch] == 1:
            return index
        else:
            index += 1       
    return -1

print(firstUniqChar('loveleetcode'))

# Runtime: 140 ms, faster than 42.15% 