#User function Template for python3

class Solution:
    def findMaxLen(ob, S):
        # code here 
        st=[]
        index=[]
        index.append(-1)
        area=0
        for i in range (len(S)):
            if S[i]=='(':
                st.append(S[i])
                index.append(i)
            else:
                if len(st)!=0 and st[-1]=='(':
                    st.pop()
                    index.pop()
                    area=max(area,i-index[-1])
                    
                    
                else:
                    index.append(i)
                    
        return area 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        
        ob = Solution()
        print(ob.findMaxLen(S))
# } Driver Code Ends