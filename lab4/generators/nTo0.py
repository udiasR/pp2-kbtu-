n = int(input())

def nums(n):
    for i in range(n, 0, -1):     #  -1 means decreasing
        yield i

print(*nums(n))    #*nums(n) unpacks the generator, converting it to a space-separated output.
