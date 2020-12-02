o1=0
o2=0
for s in open("day2.txt"):
    s=s.strip()
    ran,c,passw = s.split(" ")
    a,b = map(int,ran.split("-"))
    c = c[0]
    if a<=passw.count(c)<=b:
        o1+=1
    if (passw[a-1]+passw[b-1]).count(c)==1:
        o2+=1
print(o1)
print(o2)
