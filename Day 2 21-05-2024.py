class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    
# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
# t = a
# while t:
#     print(t.data)
#     t = t.next
#Ps2
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.count = 0

    def addbeg(self,val):
        n_n = Node(val)
        n_n.next = self.head
        self.head = n_n

    def addend(self,val):
        n_n = Node(val)
        if not self.head:
            self.head = n_n
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = n_n

    def delbeg(self):
        if self.head:
            self.head = self.head.next
        else:
            print("Head is empty")

    def delend(self):
        if self.head:
            curr = self.head
            while curr.next.next:
                curr  = curr.next
            curr.next = None
        else:
            print("Head is empty")

    def lenofll(self):
            if not self.head:
                print("Empty list")
            else:
                
                curr = self.head
                while curr:
                        self.count += 1
                        curr = curr.next
                return self.count
    def addmid(self,data):
        new = Node(data)
        # self.count = self.lenofll()
        if self.count==1:
            self.head.next = new
        else:
            h = self.count//2
            i = 1
            curr = self.head
            while i!=h:
                curr = curr.next
                i+=1
            new.next = curr.next
            curr.next = new
                
    def printll(self):
        if not self.head:
            print("Empty list")
        else:
            curr = self.head
            while curr:
                print(curr.data,end="")
                curr = curr.next
            print()
    def printmid(self):
        s = self.head
        h = self.head
        while h.next and h.next.next:
            h = h.next.next
            s = s.next
        
        print(s.data)
    def delmid(self):
        s = self.head
        h = self.head
        while h.next and h.next.next:
            h = h.next.next
            s = s.next
        
           
ll = LinkedList()
ll.addbeg(1)
ll.addbeg(2)
ll.addbeg(3)
ll.addend(4)
ll.printll()
ll.delend()
ll.printll()
print(ll.lenofll())
ll.addmid(6)
ll.printll()
ll.printmid()

#ps -> Leetcode 160
#ps -> Leetcode 141
#ps -> Leetcode 121