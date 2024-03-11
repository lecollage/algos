steps = []

def hanoiTower(n, fromPeg, toPeg):
    if n == 1:
        # print(fromPeg, toPeg)
        return steps.append([fromPeg, toPeg])
    
    unusedPeg1 = 6 - fromPeg - toPeg
    unusedPeg2 = 7 - fromPeg - toPeg

    hanoiTower(n-1, fromPeg, unusedPeg1)

    steps.append([unusedPeg1, unusedPeg2])
    hanoiTower(n-1, unusedPeg1, unusedPeg2)

    steps.append([unusedPeg2, toPeg])
    hanoiTower(n-1, unusedPeg2, toPeg)


N = int(input())
hanoiTower(N, 1, 4)

print(len(steps))
for step in steps:
    print(" ".join(map(str, step)))