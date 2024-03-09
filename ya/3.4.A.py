steps = []

def hanoiTower(n, fromPeg, toPeg):
    if n == 1: 
        # print(fromPeg, toPeg)
        return steps.append([fromPeg, toPeg])
    unusedPeg = 6 - fromPeg - toPeg

    hanoiTower(n-1, fromPeg, unusedPeg)
    # print(fromPeg, toPeg)
    steps.append([fromPeg, toPeg])
    hanoiTower(n-1, unusedPeg, toPeg)


N = int(input())
hanoiTower(N, 1, 3)

print(len(steps))
for step in steps:
    print(" ".join(map(str, step)))