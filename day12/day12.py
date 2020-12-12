lines=[(d,int(''.join(n)))for d,*n in open("day12.txt")]
p1,p2,dir,wp,dirs=0+0j,0+0j,1+0j,10+1j,{"N":1j,"S":-1j,"E":1,"W":-1}
for d,n in lines:
    if d in dirs:p1,wp=p1+dirs[d]*n,wp+dirs[d]*n
    elif d in["L","R"]:dir,wp=[x*(1j if d=="L"else -1j)**(n//90)for x in(dir,wp)]
    else:p1,p2=p1+n*dir,p2+n*wp
print("Part 1:",int(abs(p1.real)+abs(p1.imag)),"\nPart 2:",int(abs(p2.real)+abs(p2.imag)))
