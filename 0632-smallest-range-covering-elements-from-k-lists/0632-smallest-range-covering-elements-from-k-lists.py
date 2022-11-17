import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        range_start,range_end=float('-inf'),float('inf')
        
        max_value=float('-inf')
        
        heap=[]
        
        #fill the heap initially with first indexing value 
        
        for i in range (len(nums)):
                max_value=max(max_value,nums[i][0])
                
                heapq.heappush(heap,(nums[i][0],i,0))
                
        
                
        while len(heap)==len(nums):
                
                value,arr_pos,col_pos=heapq.heappop(heap)
                
                if (max_value-value)<(range_end-range_start):
                        range_start=value
                        range_end=max_value
                        
                if col_pos+1>=len(nums[arr_pos]):
                        break 
                        
                num=nums[arr_pos][col_pos+1]
                max_value=max(max_value,num)
                
                heapq.heappush(heap,(num,arr_pos,col_pos+1))
        return [range_start,range_end]
                
        
        