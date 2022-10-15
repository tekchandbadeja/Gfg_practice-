#User function Template for python3
def findall(string,open,close,ans,n):
    if len(string)==2*n:
        ans.append(string)
        return 
    
    if open<n:
        findall(string+'(',open+1,close,ans,n)
    if close<open:
        findall(string+')',open,close+1,ans,n)
        
class Solution:
    def AllParenthesis(self,n):
        #code here
        ans=[]
        findall('(',1,0,ans,n)
        return ans 



#{ 
 # Driver Code Starts
#Initial Template for Python 3


        
if __name__=="__main__":
    t=int(input())
    for i in range(0,t):
        n=int(input())
        ob=Solution()
        result=ob.AllParenthesis(n)
        result.sort()
        for i in range(0,len(result)):
            print(result[i])
        

# } Driver Code Ends