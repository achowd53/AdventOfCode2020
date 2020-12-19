r,l = open("day19.txt").read().split('\n\n')
lines, rules = l.splitlines(), __import__("collections").defaultdict(list)
for rule in r.splitlines():
    name, lowers = rule.split(": ")
    for lower in lowers.split(' | '): rules[int(name)].append(list(eval(part)for part in lower.split()))
rules[39],rules[110]='a','b'
def check(line, rule):
    if not rule: return len(line)==0
    lower_rules = rules[rule.pop(0)]
    if lower_rules in ['a','b']: return line.startswith(lower_rules)and check(line[1:],rule)
    else: return any(check(line,lower_rule+rule) for lower_rule in lower_rules)
print("Part 1:",sum(check(line,[0]) for line in lines))
rules[8],rules[11]=[[42],[42,8]],[[42,31],[42,11,31]]
print("Part 2:",sum(check(line,[0]) for line in lines))
