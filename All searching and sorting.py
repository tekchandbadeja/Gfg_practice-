#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Binary search code    (only apply when our array in a specific order may be in asecnding and decending )

def binary_search(arr,n,key):
    start_index=0
    end_index=n-1
    while start_index<=end_index:
        mid=(start_index+end_index)//2
        if arr[mid]==key:
            return mid                     #### TIME COMPLEXITY===O(log(n))
        elif arr[mid]<key:                 ####(because n,n/2,n/4,n/8,n/16....), at the end n/2*x=1 so log(n) base 2
            start_index=mid+1
        elif arr[mid]>key:
            end_index=mid-1
    return -1


# In[ ]:


# FAMOUS PROBLEM OF BINARY SEARCH

# 1.first and last occurence of a given number

# 2.find total number of occurence of a key   {formula== last_occurence-first_occurence+1}

# 3. find peak in mountain array

# 4. find pivot in array

# 5. search element in rotated and sorted array

# 6. square root of a number


# In[4]:


def first_occur(arr,n,key):
    si=0
    li=n-1
    ans=-1
    while si<=li:
        mid=(si+li)//2
        if arr[mid]==key:
            ans=mid
            li=mid-1
        elif arr[mid]>key:
            li=mid-1
        else:
            si=mid+1
    return ans


def last_occur(arr,n,key):
    si=0
    li=n-1
    ans=-1
    while si<=li:
        mid=(si+li)//2
        if arr[mid]==key:
            ans=mid
            si=mid+1
        elif arr[mid]>key:
            li=mid-1
        else:
            si=mid+1
    return ans

def first_last(arr,n,key):
    ans1=first_occur(arr,n,key)
    ans2=last_occur(arr,n,key)
    return ans1,ans2

print(first_last([1,2,5,7,7,7,7,9],8,0))
        
        
    
    


# In[7]:


def total_occur(arr,n,key):
    f1=first_occur(arr,n,key)
    l1=last_occur(arr,n,key)
    return l1-f1+1
print(total_occur([1,2,5,7,7,7,7,9],8,0))


# In[15]:


### Mountain element
def mountain_peak(arr,n):
    si=0
    ei=n-1
    while si<ei:
        mid=(si+ei)//2
        if arr[mid]<arr[mid+1]:
            si=mid+1
        else:
            ei=mid
    return si
print(mountain_peak([5,7,9,11,19,2,1,0],8))


# In[2]:


### SORTING
def selection_sort(arr):
    for i in range (len(arr)):
        min_index=i
        for j in range (i+1,len(arr)):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

print(selection_sort([10,9,4,6,2]))
        


# In[3]:


### BUBBLE SORT
def bubble_sort(arr,n):
    for i in range (1,n):
        for j in range (0,n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([10,9,4,6,2],5))
            


# In[9]:


####OPTIMISED BUBBLE SORT
def bubble_sort_opti(arr,n):
    temp=False
    for i in range (1,n):
        for j in range (0,n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                temp=True
        if temp==False:
            break
    return arr
print(bubble_sort_opti([13,14,15,16,17],5))


# In[ ]:


def insertion_sort(arr,n):
    for i in range (1,n):
        temp=arr[i]
        j=i-1
        while (j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr
print(insertion_sort([10,9,4,6,2],5))


# In[18]:


def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while (i<len(a1) and j<len(a2)):
        if a1[i]<a2[j]:
            arr[k]=a1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=a2[j]
            j=j+1
            k=k+1
    while i<len(a1):
        arr[k]=a1[i]
        i=i+1
        k=k+1
    while j<len(a2):
        arr[k]=a2[j]
        j=j+1
        k=k+1

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid=(len(arr)//2)
    a1=arr[0:mid]
    a2=arr[mid:]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1,a2,arr)

arr=[10,9,4,6,2]
merge_sort(arr)
print(*arr)
    


# In[12]:


def binary_search_recursion(arr,n,key,si,ei):
    if si>ei:
        return -1
    mid=(si+ei)//2
    if arr[mid]==key:
        return mid
    elif arr[mid]>key:
        return binary_search_recursion(arr,n,key,si,mid-1)
    else:
        return binary_search_recursion(arr,n,key,mid+1,ei)
print(binary_search_recursion([1,2,5,7,9,11],6,11,0,5))
    


# In[4]:


def partation(arr,si,ei):
    pivot=arr[si]
    count=0
    for i in range(si+1,ei+1):
        if arr[i]<pivot:
            count+=1
    pivot_index=si+count
    arr[si],arr[pivot_index]=arr[pivot_index],arr[si]
    i=si
    j=ei
    while i<j:
        if arr[i]<pivot:
            i=i+1
        elif arr[j]>=pivot:
            j=j-1
        else:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
            j=j-1
    return pivot_index

def quick_sort(arr,si,ei):
    if si>=ei:
        return
    pivot_index=partation(arr,si,ei)
    quick_sort(arr,si,pivot_index-1)
    quick_sort(arr,pivot_index+1,ei)

a=[10,9,6,4,2]
quick_sort(a,0,4)
print(*a)

