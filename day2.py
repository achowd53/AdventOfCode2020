o1=0
o2=0
for s in open("day2.txt"):
    s=s.strip()
    ran,c,pas = s.split()
    a,b = map(int,ran.split("-"))
    c = c[0]
    if a<=pas.count(c)<=b:
        o1+=1
    if (pas[a-1]+pas[b-1]).count(c)==1:
        o2+=1
print(o1)
print(o2)
