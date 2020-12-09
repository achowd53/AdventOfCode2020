import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import string, numpy, itertools
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)

def run(filename, preamble):
    print("Running",filename+"...")

    lines = [*map(int,open(filename).read().splitlines())]
    seen=[]
    for i,val in enumerate(lines):
        if i > preamble:
            result=False
            for x,y in itertools.combinations(seen[-preamble:], 2):
                if x+y == val:
                    result=True
                    break
            if not(result):
                print(sum:=val)
                break
        seen.append(val)
    sums = [[0]*len(lines) for i in range(len(lines))]
    for i in range(len(sums)):
        prefix=[]
        for _ in range(i+1): prefix.append(0)
        for j in range(i,len(sums)):
            prefix.append(prefix[-1]+lines[j])
        sums[i]=prefix[1:]
    for i in range(len(lines)):
        for j in range(len(lines)):
            if sums[i][j]==sum:
                print(min(lines[i:j+1])+max(lines[i:j+1]))
                return -1

run("example.txt", 5)
print()
run("day9.txt", 25)
