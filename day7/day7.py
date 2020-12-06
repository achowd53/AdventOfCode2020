import re #Flashback to regex, re.fullmatch(r'#[0-9a-f]{6}',hcl) and re.fullmatch(r'[0-9]{9}',pid)
import string
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)
#Flexing sets with a day6 code reminder:
    #day=open("day6.txt").read().split('\n\n')
    #print("Part 1:",sum(len(set(line)-{'\n'}) for line in day))
    #print("Part 2:",sum(len(set.intersection(*map(set,line.split("\n")))) for line in day))

part1=part2=0

c=0
l=[]
#for s in open("day7.txt"):
#    s=s.strip()
    
for line in open("day7.txt").read().split('\n\n'):
    pass

print(part1)
print(part2)

