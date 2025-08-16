def summ_all(*args):
    print(*args)
    return sum(args)

print(summ_all(1,2))
print(summ_all(1,2,3,4,5))
print(summ_all(3,6,5,4,3,8,7))