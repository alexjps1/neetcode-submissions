
class Node:

    def __init__(self, val, minim=None, next=None):
        self.val = val
        self.minim = minim
        self.next = next

class MinStack:


    def __init__(self):
        self.topnode = None
        

    def push(self, val: int) -> None:
        if self.topnode is None:
            self.topnode = Node(val, minim=val)
            return
        oldtopnode = self.topnode
        self.topnode = Node(val, minim=min(oldtopnode.minim, val), next=oldtopnode)
        

    def pop(self) -> None:
        if self.topnode is None:
            return
        delete = self.topnode
        result = self.topnode.val
        self.topnode = self.topnode.next
        del delete
        return result
        

    def top(self) -> int:
        if self.topnode is None:
            return None
        return self.topnode.val
        

    def getMin(self) -> int:
        if self.topnode is None:
            return None
        return self.topnode.minim 
