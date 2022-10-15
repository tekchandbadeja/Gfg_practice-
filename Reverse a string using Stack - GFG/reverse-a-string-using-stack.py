#{ 
 # Driver Code Starts

# } Driver Code Ends
def reverse(S):
    st=[]
    for i in S:
        st.append(i)
    ans=''
    while len(st)!=0:
        ans+=st.pop()
    return ans 
    
    #Add code here

#{ 
 # Driver Code Starts.
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        print(reverse(str1))
# } Driver Code Ends