class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:
    def __init__(self):
        self.s = [Node(0) for i in range(0, 10**4)]

    def add(self, key: int) -> None:
        curr = self.s[key % 10**4]
        
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next

        curr.next = Node(key)

    def remove(self, key: int) -> None:
        curr = self.s[key % 10**4]
        
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return

            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.s[key % 10**4]
        
        while curr.next:
            if curr.next.key == key:
                return True

            curr = curr.next

        return False
        


# Your MyHashSet object will be instantiated and called as such:

inputs = [
    1
]

for key in inputs:
    obj = MyHashSet()
    obj.add(key)
    print(obj.contains(key))
    obj.add(key)
    print(obj.contains(key))
    obj.remove(key)
    print(obj.contains(key))