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
    prefix=[0]
    for i in range(len(lines)): prefix.append(prefix[-1]+lines[i])
    for i in range(1, len(prefix)):
        for j in range(i+1, len(prefix)):
            if prefix[j]-prefix[i]==sum:
                print(min(lines[i:j])+max(lines[i:j]))
                return -1

run("example.txt", 5)
print()
run("day9.txt", 25)
