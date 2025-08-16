def fact(num):
    if(num==1):
        return 1
    return num*fact(num-1)

n=fact(6)
print(n)