n=int(input())
t=n
temo=0
while t!=0:
    temo=temo*10+t%10
    t=t//10
   
if n==temo:
    print("yes")
else:
    print("not")
    
