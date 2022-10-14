#User function Template for python3

class Queue:
    def __init__(self):
        self.stack=[]
        self.front=0
        self.count=0
    def enqueue(self,X):
        self.stack.append(X)
        self.count+=1
    def size(self):
        return self.count
    def isempty(self):
        return self.size()==0
        # code here
    def dequeue(self):
        # code here
        if self.isempty():
            return -1
        ele=self.stack[self.front]
        self.front+=1
        self.count-=1
        return ele


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        ob=Queue()
        n = int(input())
        a = list(map(int,input().strip().split()))
        i = 0
        while i<len(a):
            if a[i] == 1:
                ob.enqueue(a[i+1])
                i+=1
            else:
                print(ob.dequeue(),end=" ")
            i+=1

        print()
# } Driver Code Ends