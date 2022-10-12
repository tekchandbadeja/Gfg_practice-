#!/usr/bin/env python
# coding: utf-8

# In[11]:


###
1.taking input in linked list

2. print linked list

3. find the length of linked list or (find the nodes in linked list)


# In[12]:


class Node:                    ### basic structure of linked list
    def __init__(self,data):
        self.data=data
        self.next=None
        
        
###basic apporach to take input

def takeinput():
    head=None
    curr_input=[int(ele) for ele in input().split()]
    for curr_ele in curr_input:
        if curr_ele ==-1:
            break
        new_node=Node(curr_ele)
        if head is None:                      ### here time complexiblity of taking input is order of (n**2) because everytime curr have to traversal upto (n-1) node 
                                      ## for example 1,2,3 is a linked list and 4 comes than curr traverse 3 time and same if i add 5 again than curr traverse upto 4 means 4 time 
                                      ### 0+1+2+3+.......+ (n-1)==O(n**2)   so taking input needed to be optimization
            head=new_node
        else:
            curr=head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node
    return head


#### print linked list

def print_ll(head):
    
    while head is not None:
        print(str(head.data)+'->',end=(' '))
        head=head.next
    print('None')
    return 

obj=takeinput()
print_ll(obj)
        

                


# In[ ]:


###OPTIMIZED TAKING INPUT O(N)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeinput():
    head=None            ### here i maded two thing head and tail if I add any new node in my previous linked list than I need to traverse tail only one step
    tail=None            #### 1+1+1+1+.....+1==O(n)
    input_list=[int(ele) for ele in input().split()]

    for curr_ele in input_list:
        if curr_ele ==-1:
            break
        new_node=Node(curr_ele)
        if head is None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
    return head

def printll(head):
    while head is not None:
        print(str(head.data)+"->",end=(''))
        head=head.next
    print("None")
    return 


obj1=takeinput()
printll(obj1)


# In[26]:


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeinput():
    head=None
    tail=None
    input_list=[int(ele) for ele in input().split()]
    for curr_ele in input_list:
        if curr_ele==-1:
            break
        new_node=Node(curr_ele)
        if head is None:
            head=new_node
            tail=new_node
        else:
            tail.next=new_node
            tail=new_node
    return head

def printll(head):
    while head is not None:
        print(str(head.data)+'->',end=(' '))
        head=head.next
    print('None')
    return 

def lengthll(head):
    count=0
    while head is not None:
        count+=1
        head=head.next
    return count
###
def insertion(head,i,value):
    if i<0 or i>lengthll(head):
        return head
    prev=None
    curr=head
    count=0
    while count<i:
        prev=curr
        curr=curr.next
        count+=1
    new_node=Node(value)
    if prev is   None:
        head=new_node
    else:
        prev.next=new_node
    new_node.next=curr
    return head
obj=takeinput()
printll(obj)
print(lengthll(obj))
ans=insertion(obj,6,9)
printll(ans)
print(lengthll(ans))
    
    
    


# In[ ]:





# In[ ]:




