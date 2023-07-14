def objects(x, y):
    if x is type(int) and y is type(int):
        sum = x + y
        print(sum)
    else:
        print('Not valid')
print(objects('3', 'yes'))
print(objects(4, 5))