import itertools
def run(filename, preamble):
    lines = [*map(int,open(filename).readlines())]
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
run("day9.txt", 25)
