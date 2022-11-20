def coincide(a, b): #bool function
    if(a==b):
        return True
    else:
        return False

a=input()
b=input()
c=input()
d=input()
if(coincide(a,c) or coincide(a,d) or coincide(b,c) or coincide(b,d)):
    print("YES")
else:
    print("NO")