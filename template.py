import re #re.split(), re.match, re.findall, Regex Guide at https://www.debuggex.com/cheatsheet/regex/python
import collections #defaultdicts, maybe counters
import functools #use @functools.lru_cache(None) above a function to keep track of all inputs and speed it up
import string, numpy, itertools
#Sets are POG {}, A|B finds union of sets, A&B finds intersection, A-B finds difference, A^B is (A|B)-(A&B)

def run(filename):
    print("Running",filename+"...")

    #lines = open(filename)
    #lines = open(filename).read().split('\n\n')
    lines = open(filename).readlines()

    for line in lines:
        pass


run("example.txt")
print()
run("day11.txt")
