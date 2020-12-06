import string

part1=part2=0
for line in open("day6.txt").read().split('\n\n'):
    for x in string.ascii_lowercase:
        if x in line:part1+=1
        if line.count(x)==line.count('\n')+1:part2+=1

print(part1)
print(part2)
