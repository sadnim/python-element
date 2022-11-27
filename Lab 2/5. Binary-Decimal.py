n=input()
i=0
num=0
l=len(n)#length of input string
for i in range(l):
    a=int(n[l-i-1])#index of element is reversed. if i=1, index=length-i
    num+=a*2**i
    i+=1
print(num)