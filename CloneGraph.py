"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from queue import Queue
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return node
        q=Queue()
        map1={}
        copyNode=Node(node.val)
        q.put(node)
        #jo node copy kiya hain start se usko map me dal denge
        #{1:Node1}
        map1[node.val]=copyNode
        while not(q.empty()):
            curr=q.get()
            for n in curr.neighbors:
                #2 neightbour hain to wo map me nahi hain key=2, val=Node2 aise daldo
                if n.val not in map1:
                    copy=Node(n.val)
                    map1[n.val]=copy
                    q.put(n)
                #get copy of original node
                #add to its neighbours, copy of my original node neighbor
                map1[curr.val].neighbors.append(map1[n.val])
        return copyNode
        
#Time complexity is O(V+E)
#Space complexity is O(n)
        
