#User function Template for python3
def knows(a,b,M):
    if M[a][b]==1:
        return True
    return False 
        
class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        st=[]
        for i in range (n):
            st.append(i)
        while len(st)!=1:
            a=st[-1]
            st.pop()
            b=st[-1]
            st.pop()
            if knows(a,b,M):
                st.append(b)
            else:
                st.append(a)
            
        ans=st[-1]
        
        ###verification
        
        row_check=False
        row_count=0
        for i in range (n):
            if M[ans][i]==0:
                row_count+=1
        if row_count==n:
            row_check= True
        # else:
        #     False
        col_check=False
        col_count=0
        for i in range(n):
            if M[i][ans]==1:
                col_count+=1
        if col_count==n-1:
            col_check= True
        # else:
        #     return False 
        
        if row_check==True and col_check==True:
            return ans 
        else:
            return -1
                
            
            
            
        # code here 
        # st=[]
        # i=0
        # j=0
        # count=0
        # while i<n:
        #     while j<n:
        #         if M[i][j]==0:
        #             st.append(M[i][j])
        #     while len(st)!=0:
        #         st.pop()
        #         count+=1
        #     if count==n:
        #         return i
        #     else:
        #         j+=1
        #     i+=1
        # return -1
                
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends