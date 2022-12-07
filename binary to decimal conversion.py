a="1001101"
len1=len(a)
x = print(range(len1))
print(len1)
count=0
ans=0
for i in range (len1):
    x = print(range(len1))
    if a[len1-1-i]=='1':
        ans+=2**count
    count+=1
print(ans)