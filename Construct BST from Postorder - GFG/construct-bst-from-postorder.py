# #User function Template for python3
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
        
# def in_post(post,inorder):
#     if post==None:
#         return 
#     rootdata=post[-1]
#     root=Node(rootdata)
    
#     rootIndex=-1
#     for i in range (len(inorder)):
#         if inorder[i]==rootdata:
#             rootIndex=i
#             break
#     if rootIndex==-1:
#         return None
#     left_In=inorder[0:rootIndex]
#     right_In=inorder[rootIndex+1:]
    
#     y=len(left_In)
    
#     left_Post=post[0:y]
#     right_Post=post[y:len(post)-1]
    
#     left_tree=in_post(left_Post,left_In)
#     right_tree=in_post=(right_Post,right_In)
    
#     root.left=left_tree
#     root.right=right_tree
    
#     return root 
    
# class Solution:
#     def constructTree(self,post,n):
#         # code here
#         inorder=sorted(post)
#         return in_post(post,inorder)
        
        
class Solution:
   def constructTree(self,post,n):
       post.sort()
       return(self.arr_to_bst(post))
       

   def arr_to_bst(self,arr):
       if not arr:
           return None
       mid = len(arr) // 2
       root = Node(arr[mid]) #typecast in node type
       root.left = self.arr_to_bst(arr[:mid])
       root.right = self.arr_to_bst(arr[mid + 1:])
       return root
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
   def __init__(self,val):
       self.val=val
       self.left=None
       self.right=None
class BST:
   size=0
   def inorder(self,tmp,size=0):
       if tmp:
           self.inorder(tmp.left,self.size)
           print(tmp.val,end=" ")
           self.inorder(tmp.right,self.size)
     
if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        obj=Solution()
        b=BST()
        pt=obj.constructTree(arr,n)
        b.inorder(pt)
        print()

# } Driver Code Ends