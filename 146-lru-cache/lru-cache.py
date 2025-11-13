class ListNode:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.start = ListNode()
        self.end = self.start
        self.map = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]

        if node == self.end:
            return node.val

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.end.next = node
        node.prev = self.end
        node.next = None
        self.end = node


        return node.val


    def put(self, key: int, value: int) -> None:

        if key not in self.map:
            new_node = ListNode(value, key)
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node 
            self.map[key] = new_node
            
            if len(self.map) > self.capacity:
                self.map.pop(self.start.next.key)
                self.start.next = self.start.next.next
                if self.start.next:
                    self.start.next.prev = self.start


                
            return
 
        node = self.map[key]
        node.val = value

        if node == self.end:
            return

        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        self.end.next = node
        node.prev = self.end
        node.next = None
        self.end= node
 
        return

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)