class StackNode:
    
    def __init__(self, data):
        self.data = data
        self.next = None
class MyStack:
    def __init__(self):
        self.head=None
        self.count=0


    
        
    #Function to push an integer into the stack.
    def push(self, data):

        # Add code here
        new_node=StackNode(data)
        new_node.next=self.head
        self.head=new_node
        self.count+=1
    def size(self):
        return self.count
    def isempty(self):
        return self.size()==0
        


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.isempty():
            return -1
        ele=self.head.data
        self.head=self.head.next
        self.count-=1
        return ele

        # Add code here



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends