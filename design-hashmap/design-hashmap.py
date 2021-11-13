class Node:
    
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [Node() for _ in range(2069)]
        self.size = len(self.data)
        
    def get_hash_code(self, key):
        """
        Returns hash value
        """
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashcode = self.get_hash_code(key)
        head = self.data[hashcode]
        
        while head.next:
            if key == head.next.key:
                head.next.value = value
                return
            
            head = head.next
            
        head.next = Node(key, value)
            
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashcode = self.get_hash_code(key)
        head = self.data[hashcode]
        
        while head.next:
            if key == head.next.key:
                return head.next.value
            head = head.next
            
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashcode = self.get_hash_code(key)
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