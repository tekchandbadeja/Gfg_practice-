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

	def kLargest(self,arr, n, k):
		# code here
		ans=helper(arr,n,k)
		return sort(ans) 
		
		
		        
		#heapq._heapify_max(heap)
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.kLargest(arr, n, k)
        for x in ans:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends