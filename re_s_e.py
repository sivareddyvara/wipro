x='hai siva reddy helo buddy'

s=x.split()
a=[]
for i in s:
    if i==s[0] or i==s[-1]:
        a.append(i)
    else:
        a.append(i[::-1])


z=' '.join(a)
print(z)
