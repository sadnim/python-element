def power(a, b):
    i=0
    num=1
    for i in range(1, b):
        num*=a
        i+=1
    return num

a, b=float(input()), int(input())
print(power(a, b))