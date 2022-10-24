#User function Template for python3

'''
# Node class

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''

class Solution:
    def buildtree(self, inorder, preorder, n):
        # code here
        # build tree and return root node
        
        if len(preorder)==0:
            return None
        
        rootdata=preorder[0]
        root=Node(rootdata)
        
        rootdata_index=-1
        for i in range (len(inorder)):
            if inorder[i]==rootdata:
                rootdata_index=i
                break
        
        if rootdata_index==-1:
            return None
            
        left_inorder=inorder[0:rootdata_index]
        right_inorder=inorder[rootdata_index+1:]
        
        l=len(left_inorder)
        
        left_preorder=preorder[1:l+1]
        right_preorder=preorder[l+1:]
        
        left_tree=self.buildtree(left_inorder, left_preorder, n)
        right_tree=self.buildtree(right_inorder, right_preorder, n)
        
        root.left=left_tree
        root.right=right_tree
        
        return root
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

def printPostorder(n):
    if n is None:
        return
    printPostorder(n.left)
    printPostorder(n.right)
    print(n.data, end=' ')

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        inorder = [ int(x) for x in input().split() ]
        preorder = [ int(x) for x in input().split() ]
        
        root = Solution().buildtree(inorder, preorder, n)
        printPostorder(root)
        print()

# } Driver Code Ends