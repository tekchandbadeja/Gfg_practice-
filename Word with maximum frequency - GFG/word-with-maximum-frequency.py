#User function Template for python3

def maximumFrequency (S) : 
    #Complete the function
    d={}
    words=S.split(' ')
    for i in words:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    ans=''
    count=0
    
    
    for i in words:
        if d[i]>count:
            ans=i
            count=d[i]
    if count==1:
        return words[0]+ ' '+'1'
    
    return ans+' '+str(count)
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    S = input()
    
    print(maximumFrequency(S))




# } Driver Code Ends