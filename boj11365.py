while True:
    array = list(map(str, input()))
    if ''.join(array) == 'END':
        break
    array.reverse()
    print(''.join(array))
