class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodesize=0
    def append(self,data):  ### 끝에 값을 추가해주는 메서드
        newNode=Node(data)  
        if (self.head):
            current=self.head
            while current.next:
                current=current.next
            self.tail=newNode
            current.next=self.tail
        else:
            self.head=newNode
            self.tail=newNode
        self.nodesize+=1
    def insert(self,ind,data):  ### 해당 index위치에 data를 넣어준다.
        newNode=Node(data)        
        if self.head:
            if ind==0:
                temp=Node(self.head.data,self.head.next)
                self.head=newNode
                self.tail=temp
                self.head.next=self.tail
            else:
                if ind<self.nodesize:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        prev=current
                        current=current.next
                        cnt+=1
                    prev.next=newNode
                    newNode.next=current
                else:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        prev=current
                        current=current.next
                        cnt+=1
                    self.tail=newNode
                    prev.next=self.tail
                
        else:
            self.head=newNode
            self.tail=newNode
        self.nodesize+=1
    
    def empty(self):
        if not self.nodesize:
            return True
        else:
            return False
    
    def sizeofList(self):  ## 현재 사이즈를 알려준다.
        return self.nodesize
    
    def clear(self):  ### 다 비워준다.
        self.head=None
        self.tail=None
        self.nodesize=0
    
    def slicing(self,start,end):  ### start에서 end 직전까지 잘라준다. 추가된 기능
        if not(start>self.nodesize-1 or end>self.nodesize+1):
            if end-start>1:
                if start==0:              ### list로 반환해준다.
                    result=[]
                    current=self.head
                    result.append(current.data)
                    start+=1
                    while start<end:
                        current=current.next
                        result.append(current.data)
                        start+=1
                    return result
                else:
                    result=[]
                    current=self.head
                    cnt=0
                    while cnt<start:
                        current=current.next
                        cnt+=1
                    result.append(current.data)
                    start+=1
                    while start<end:
                        current=current.next
                        start+=1
                        result.append(current.data)
                    return result
            else:
                return False
        else:
            return False

    
    def find(self,ind):  #### 입력된 ind의 값이 무엇인지 알려준다.
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    return self.head.data
                else:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        current=current.next
                        cnt+=1
                    return current.data
    
    def change(self,ind,data):  ### 내가 찾은 ind의 값을 data로 바꿔준다.
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    self.head.data=data
                else:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        current=current.next
                        cnt+=1
                    current.data=data
    def remove(self,ind):   ### 내가 찾는 ind의 data를 삭제해준다. list의 del과 동일
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    current=self.head
                    self.head=current.next
                else:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        prev=current
                        current=current.next
                        cnt+=1
                    prev.next=current.next
            self.nodesize-=1
    def print_all(self):   ### 내가 지금까지 저장한 링크드리스트를 리스트형태로 반환해준다.
        result=[]
        if self.head:
            current=self.head
            result.append(current.data)
            while current.next:
                current=current.next
                result.append(current.data)
            return result
        else:
            return result
    
    def pop(self):                #### 추가된 기능 pop() 가장 마지막걸 꺼내준다.
        if self.nodesize:
            if self.nodesize >1:
                result=self.tail.data
                current=self.head
                while current.next.next:
                    prev=current
                    current=current.next
                self.tail=current
                prev.next=self.tail
                current.next=None
                self.nodesize-=1
                return result
            else:
                result=self.head.data
                self.head=None
                self.tail=None
                self.nodesize-=1
                return result
        else:
            return False
    def popleft(self):           #### 추가된 기능 popleft() 가장 왼쪽걸 꺼내준다.
        if self.nodesize>1:
            result=self.head.data
            temp=self.head
            self.head=temp.next
            self.nodesize-=1
            return result
        else:
            result=self.head.data
            self.head=None
            self.tail=None
            return result
    def find_lager_index(self,data): ### data보다 큰 값이 있는 최초 index의 위치를 찾아준다.
        ind=0                        ## 없을시 -1을 반환
        current=self.head
        while ind<self.nodesize:
            if current.data>data:
                return ind
            current=current.next
            ind+=1
        return -1


T=int(input())


for tc in range(1,T+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(M)]
    result=LinkedList()
    for i in range(N):
        result.append(arr[0][i])
    row=1
    while row<M:
        larger_index=result.find_lager_index(arr[row][0])
        if larger_index==-1:
            for i in range(N):
                result.append(arr[row][i])
        else:
            for i in range(N-1,-1,-1):
                result.insert(larger_index,arr[row][i])
        row+=1
    print('#{} '.format(tc),end='')
    total_len=result.sizeofList()
    result=reversed(result.slicing(total_len-10,total_len))
    print(*result)
    
    