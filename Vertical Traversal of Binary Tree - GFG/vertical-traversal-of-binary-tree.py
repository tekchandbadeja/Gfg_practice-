#User function Template for python3

# import queue
# class Solution:
    
#     #Function to find the vertical order traversal of Binary Tree.
#     def verticalOrder(self, root): 
#         #Your code here
#         q=queue.Queue()
#         a=[root,(0,0)]
#         q.put(a)
#         map={}

#         while (not(q.empty())):

#             current=q.get()

#             #root data
#             rd=current[0]
#             ### horizontal_distance
#             hd=current[1][0]

#             ####level 
#             le=current[1][1]


#             if hd in map:
#                 map[hd].append(rd.data)
#             else:
#                 map[hd]=rd.data
#             if rd.left:
#                 left=[rd.left,(hd-1,le+1)]
#                 q.put(left)

#             if rd.right:
#                 right=[rd.right,(hd+1,le+1)]
#                 q.put(right)

#             ar=sorted(map)
#             ans=[]
#             for i in ar:
#                 ans=ans+map[i]

#         return ans
import queue
from collections import deque
class Solution:
    def verticalOrder(self, root):
        q=deque([])
        #q=queue.Queue([])
        a=[root,[0,0]]
        #a=[root,(0,0)]
        q.append(a)
        #q.put(a)
        d={}
        #n=q.qsize()
        
        while(len(q)!=0):
            b=q.popleft()
            #b=q.get()
            ro=b[0]
            hd=b[1][0] # horizontal distance
            lev=b[1][1] # at level
            if(hd in d):
                d[hd].append(ro.data) # checking if horizontal distance in dict
            else:
                d[hd]=[ro.data] # making a dict like{1:[1,5,6]} array as key
            if(ro.left):
                b=[ro.left,[hd-1,lev+1]] #if left is present than hd=hd-1 and lev=lev+1
                q.append(b)
                #q.put(b)
            if(ro.right):
                b=[ro.right,[hd+1,lev+1]] # if right is present than hd=hd+1 and lev=lev+1
                q.append(b)
                #q.put(b)
        ar=sorted(d)
        ans=[]
        for i in ar:
            ans=ans+d[i]
        return ans
       
       



#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
    import sys
    sys.setrecursionlimit(10000)
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        res = Solution().verticalOrder(root)
        for i in res:
            print (i, end=" ")
        print()



# } Driver Code Ends