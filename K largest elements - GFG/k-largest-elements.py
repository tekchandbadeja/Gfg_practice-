#User function Template for python3
import heapq

def helper(arr,n,k):
    heap=arr[0:k]
	heapq.heapify(heap)
		
	for i in range (k,n):
	    if heap[0]<arr[i]:
	        heapq.heapreplace(heap,arr[i])
	return heap
	
def sort(arr):
    arr.sort(reverse=True)
    return arr
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        # code here
        ans=helper(li,n,k)
		return sort(ans) 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends