# from collections import Counter, defaultdict

# def firstUniqChar(s: str) -> int:
#     count = Counter(s)
#     for i, ch in enumerate(s):
#         if count[ch] == 1:
#             return i 
#     return -1

# Runtime: 120 ms, faster than 63.38%

# def firstUniqChar(s: str):
#     count = Counter(s)
    
#     index = 0
#     for ch in s:
#         if count[ch] == 1:
#             return index
#         else:
#             index += 1       
#     return -1

# Runtime: 140 ms, faster than 42.15% 

# def firstUniqChar(s: str):
#     dic = defaultdict(lambda: 0)

#     for i in s:
#         dic[i] += 1

#     for i, ch in enumerate(s):
#         if dic[ch] == 1:
#             return i 
#     return -1

# Runtime: 136 ms, faster than 46.28%


# def firstUniqChar(s: str):
#     for pos, char in enumerate(s):
#         if char not in s.replace(char, '', 1):
#             return pos
#     return -1

# Runtime: 284 ms, faster than 8.75%

def firstUniqChar(s):
    letters='abcdefghijklmnopqrstuvwxyz'
    index = []

    for l in letters:
        if s.count(l) == 1:
            index.append(s.index(l))

    if len(index) > 0:
        return min(index) 
    else:
        return -1

# Runtime: 52 ms, faster than 98.66%

print(firstUniqChar('loveleetcode'))