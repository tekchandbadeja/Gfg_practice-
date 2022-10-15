# User function Template for Python3

class Solution:
    def maxLength(self, S):
        # code here
        ch=[]
        index=[]
        index.append(-1)
        maxium=0
        for i in range (len(S)):
            if S[i]=='(':
                ch.append(S[i])
                index.append(i)
            else:
                if len(ch)!=0 and ch[-1]=='(':
                    ch.pop()
                    index.pop()
                    maxium=max(maxium,i-index[-1])
                
                else:
                    index.append(i)
        return maxium
                    
                


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends