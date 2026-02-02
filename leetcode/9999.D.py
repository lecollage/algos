from typing import Optional, List

# @lc code=start
class DSU:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
        self.experience = [0] * size

    def get_find(self, x: int):
        if x == self.parents[x]:
            return (x, self.experience[x])

        root, exp = self.get_find(self.parents[x])

        self.parents[x] = root
        self.experience[x] += exp - self.experience[root]

        return (root, self.experience[x]+self.experience[root])

    def union(self, x, y):
        rootX = self.get_find(x)[0]
        rootY = self.get_find(y)[0]

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parents[rootY] = rootX
                self.experience[rootY] -= self.experience[rootX]
            elif self.rank[rootX] < self.rank[rootY]:
                self.parents[rootX] = rootY
                self.experience[rootX] -= self.experience[rootY]
            else:
                self.parents[rootY] = rootX
                self.rank[rootX] += 1
                self.experience[rootY] -= self.experience[rootX]

    def add(self, player: int, exp: int):
        parent = self.get_find(player)[0]
        self.experience[parent] += exp
# @lc code=end

'''
clane exp
personal exp



exp
            node1: 100
             /       \
        node2: 30     node3: 50
        / 
    node5: 0



    node1: 100
    node2: 30

        node1: 100+20
        /
    node2: (30-100)=-70


        node3: 50+1-120
        /
    node4: (0-50)=-50


    join 2 3 -> join 1 3


    get 2: -70+120=50
    get 1: 120

'''
n, m = map(int, input().split())
dsu = DSU(n)

for _ in range(m):
    op, *param = input().split()

    if op == 'add':
        dsu.add(int(param[0])-1, int(param[1]))
    if op == 'join':
        dsu.union(int(param[0])-1, int(param[1])-1)
    if op == 'get':
        print(dsu.get_find(int(param[0])-1)[1])
    


'''
3 6
add 1 100
join 1 3
add 1 50
get 1
get 2
get 3

4 12
add 1 100
add 2 30
join 1 2
add 1 20
add 3 50
join 3 4
add 4 0
join 2 4
get 1
get 2
get 3
get 4


'''

