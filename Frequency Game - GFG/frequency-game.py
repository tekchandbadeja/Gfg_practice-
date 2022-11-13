#User function Template for python3


def LargButMinFreq(arr,n):
    #code here
    d={}
    ans=[]
    output=[]
    for i in arr:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
            
    for i in d:
        ans.append(d[i])
        
    m=min(ans)
    
    for i in d:
        if d[i]==m:
            output.append(i)
            
    return max(output)
            
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
#Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends