def value(values, n):
    for value in values:
        if n == value:
            print("Value found")
    else:
            print("Value not found")
print(value([5,8,5,0,1], 5))
print(value([18,15,2,0], 3))
print(value([0,5,2,1], 8))
print(value([23,0,1,5,7,8,4,9], 0))
