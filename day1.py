l=[] 
for s in open("day1.txt"):
    s=int(s.strip())
    l.append(s)
part1 = 0
part2 = 0
for a in l:
    for b in l:
        if a+b==2020:
            part1=a*b
        for c in l:
            if a+b+c==2020:
                part2=a*b*c
print(part1)
print(part2)
    
