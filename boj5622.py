t = list(input())
result = 0
for i in t:
    if i in ['A', 'B', 'C']:
        result += 3
    if i in ['D', 'E', 'F']:
        result += 4
    if i in ['G', 'H', 'I']:
        result += 5
    if i in ['J', 'K', 'L']:
        result += 6
    if i in ['M', 'N', 'O']:
        result += 7
    if i in ['P', 'Q', 'R', 'S']:
        result += 8
    if i in ['T', 'U', 'V']:
        result += 9
    if i in ['W', 'X', 'Y', 'Z']:
        result += 10

print(result)
