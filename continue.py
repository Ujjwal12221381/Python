#continue
x=int(input())
y=x + (x-1)-1
mid=int(y/2)
index=mid
for i in range(x):
    if i %2!=0 :
        continue
    else:
        print(" "*index, end="")
        for j in range (index,mid+1):
            if j%2==0:
                print("x", end="")
            else:
                print(" ", end="")
        index -=2
        mid +=2
        print()

