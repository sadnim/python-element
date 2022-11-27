string=input()
a=int(string[0])
b=int(string[2])
c=int(string[4])

def Election(a, b, c):
    if(a==b==c or a==b or a==c):
        print(a)
    elif(b==c):
        print(b)

Election(a, b, c)