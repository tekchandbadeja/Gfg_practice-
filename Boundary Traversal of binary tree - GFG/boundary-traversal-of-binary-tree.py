#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def left_traversal(root,ans):
    if root==None or (root.left==None and root.right==None):
        return 
    #phle append karte jao 
    ans.append(root.data)
    ### ab left jao aur right jao aur dono ke left vaale part pick kar lo
    if root.left:
        left_traversal(root.left,ans)
    else:
        left_traversal(root.right,ans)
        
def leaf_traversal(root,ans):
    if root==None:
        return 
    if root.left==None and root.right==None:
        ans.append(root.data)
        return 
    
        
    leaf_traversal(root.left,ans)
    leaf_traversal(root.right,ans)
    
def right_traversal(root,ans):
    if root==None or (root.left==None and root.right==None):
        return
    ### phle traverse kar lo 
    if root.right:
        right_traversal(root.right,ans)
    else:
        right_traversal(root.left,ans)
        
    ### wapas aa gye  ab add karte jao
    ans.append(root.data)
    
    
    
class Solution:
    def printBoundaryView(self, root):
        # Code here
        if root==None:
            return 
        ans=[]
        ans.append(root.data)
        
        ### left part 
        left_traversal(root.left,ans)
        
        ### now come to leaf part  leaft leaf and right koi se bhee ho skte hai
        
        leaf_traversal(root.left,ans)
        
        leaf_traversal(root.right,ans)
        
        
        ### now right part
        right_traversal(root.right,ans)
        
        return ans 
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends