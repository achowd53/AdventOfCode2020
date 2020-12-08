import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import string, numpy, itertools
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)

def run(filename):
    print("Running",filename+"...")

    #lines = open(filename)
    #lines = open(filename).read().split('\n\n')
    lines = open(filename).read().splitlines()
    
    for line in lines:
        pass


run("example.txt")
print()
run("day9.txt")
