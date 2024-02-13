    
def solve(n):    
    steps = []

    def hanoiTower(n, fromPeg, toPeg):
        if n == 1: 
            # print(fromPeg, toPeg)
            return steps.append([fromPeg, toPeg])
        unusedPeg = 6 - fromPeg - toPeg

        hanoiTower(n-1, fromPeg, unusedPeg)
        # print(fromPeg, toPeg)
        steps.append([fromPeg, toPeg])


N = int(input())
solve(N, 1, 3)
steps = []

print(len(steps))
for step in steps:
    print(" ".join(map(str, step)))