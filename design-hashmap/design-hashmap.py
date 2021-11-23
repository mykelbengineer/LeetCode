class Node:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value=value
        self.next=None

class MyHashMap:

    def __init__(self):
        self.data = [Node() for _ in range(2069)]
        self.size = len(self.data)
        
    def _getHashCode(self, key):
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        hashcode = self._getHashCode(key)
        head = self.data[hashcode]
        
        while head.next:
            if head.next.key == key:
                head.next.value = value
                return
            head = head.next
            
        head.next = Node(key,value)

    def get(self, key: int) -> int:
        hashcode = self._getHashCode(key)
        head = self.data[hashcode]
        
        while head.next:
            if head.next.key == key:
                return head.next.value
            
            head = head.next
            
        return -1

    def remove(self, key: int) -> None:
        hashcode = self._getHashCode(key)
        head = self.data[hashcode]
        
        while head.next:
            if head.next.key == key:
                toRemove = head.next
                head.next = toRemove.next
                toRemove.next = None
                return
            head = head.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)