def divisible_by3_and4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i    
            # Only keeps one number in memory
            #Instead of storing all values in memory, it yields one at a time, making it memory-efficient.
            # we use this instead of RETURN


print(*divisible_by3_and4(30), sep=", ")
