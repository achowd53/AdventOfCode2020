class M(int):
    def __sub__(self, y):return M(int(self)*y)
    def __add__(self, y):return M(int(self)+y)
    def __mul__(self, y):return M(int(self)+y)
l = open("day18.txt").read().splitlines()
print("Part 1:",sum(eval(__import__("re").sub(r'(\d+)',r'M(\1)',e).replace('*','-'))for e in l))
print("Part 2:",sum(eval(__import__("re").sub(r'(\d+)',r'M(\1)',e).replace('*','-').replace('+','*'))for e in l))
