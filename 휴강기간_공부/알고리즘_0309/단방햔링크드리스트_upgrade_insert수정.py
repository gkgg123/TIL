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
                if self.nodesize==1:
                    temp=Node(self.head.data,self.head.next)
                    self.head=newNode
                    self.tail=temp
                    self.head.next=self.tail
                else:
                    temp=Node(self.head.data,self.head.next)
                    self.head=newNode
                    self.head.next=temp
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
        
            
            
a=LinkedList()  ### a라는 링크드 리스트를 생성
print(a.empty())  ### a가 비어있는지 True False를 알려준다.
a.append(1)     ### append 제일 뒤에 값을 추가해준다.
a.insert(0,3)   ### insert는 해당 인덱스에 값을 넣어주고 원래 해당인덱스와 그 뒤로 있던 값들이 하나씩 뒤로 밀어진다.
a.clear()       ### clear는 전부 초기화시켜서 값을 다 비워준다.
for i in range(30):
    a.append(i)
print(a.find(19)) ### 19 index에 위치한 값을 반환해준다.
a.change(19,55)    ### change는  해당 index의 값을 변환시켜준다. 여기서는 19번째 index의 값을 55로 바꿔준다.
print(a.find(19))
a.remove(19)      ### 해당 index의 위치의 값을 삭제한다.
print(a.print_all())  ### 저장된 모든 값을 list로 반환해준다.
print(a.pop())    ### 가장 끝의 값을 반환해주고, 삭제한다.
print(a.popleft())   ### 가장 왼쪽의 값을 반환해주고, 삭제한다. 
print(a.find_lager_index(23))   ### 들어가 값보다 큰 값이 있는 index의 위치를 반환해준다. 수열합치기를 쉽게풀기위해만든 메서드이다.
length=a.sizeofList()  ### a의 size를 알려준다.
print(a.slicing(length-10,length))   ### slicing은 start 위치에서 end-1 위치까지 값을 list로 반환해준다.