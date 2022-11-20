a=int(input())
b=int(input())
c=int(input())
first=min(a, min(b, c))
third=max(a, max(b, c))
second=a+b+c-first-third
print(first, second, third)