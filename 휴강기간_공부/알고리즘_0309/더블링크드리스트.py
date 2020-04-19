class Node:
    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class DoubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.nodesize=0

    def append(self,data):  ### 끝에 값을 추가해주는 메서드
        newNode=Node(data)  
        if (self.head):
            newNode.prev=self.tail
            self.tail.next=newNode            
            self.tail=newNode
        else:
            self.head=newNode
            self.tail=newNode
        self.nodesize+=1

    def insert(self,ind,data):  ### 해당 index위치에 data를 넣어준다.
        newNode=Node(data)        
        if self.head:
            if ind==0:            #### 여기가 수정되었다. ind==0일때 추가적인 Node 생성없이 해결해줬다.
                if self.nodesize==1:
                    self.head=newNode
                    self.head.next=self.tail
                    self.tail.prev=self.head
                else:
                    newNode.next=self.head
                    self.head.prev=newNode
                    self.head=newNode
            else:
                if ind<=self.nodesize//2:
                    current=self.head
                    cnt=0
                    while cnt<ind:
                        prev=current
                        current=current.next
                        cnt+=1
                    prev.next=newNode
                    newNode.prev=prev
                    newNode.next=current
                    current.prev=newNode
                elif self.nodesize//2<ind<self.nodesize:
                    prev=self.tail
                    cnt=self.nodesize
                    while cnt>ind:
                        current=prev
                        prev=current.prev
                        cnt-=1
                    prev.next=newNode
                    newNode.prev=prev
                    newNode.next=current
                    current.prev=newNode

                else:
                    newNode.prev=self.tail
                    self.tail.next=newNode                  
                    self.tail=newNode
                
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

    def find(self,ind):  #### 입력된 ind의 값이 무엇인지 알려준다.
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    return self.head.data
                else:
                    if ind<self.nodesize//2:
                        current=self.head
                        cnt=0
                        while cnt<ind:
                            current=current.next
                            cnt+=1
                        return current.data
                    else:
                        prev=self.tail
                        cnt=self.nodesize-1
                        while cnt>ind:
                            current=prev
                            prev=current.prev
                            cnt-=1
                        return prev.data
    def change(self,ind,data):  ### 내가 찾은 ind의 값을 data로 바꿔준다.
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    self.head.data=data
                else:
                    if ind<self.nodesize//2:
                        current=self.head
                        cnt=0
                        while cnt<ind:
                            current=current.next
                            cnt+=1
                        current.data=data
                    else:
                        prev=self.tail
                        cnt=self.nodesize-1
                        while cnt>ind:
                            current=prev
                            prev=current.prev
                            cnt-=1
                        prev.data=data
    def remove(self,ind):   ### 내가 찾는 ind의 data를 삭제해준다. list의 del과 동일
        if self.head:
            if ind<0 or ind>self.nodesize-1:
                return False
            else:
                if ind==0:
                    current=self.head
                    self.head=current.next
                    self.head.prev=None
                else:
                    if ind<self.nodesize//2:
                        current=self.head
                        cnt=0
                        while cnt<ind:
                            prev=current
                            current=current.next
                            cnt+=1
                        prev.next=current.next
                        current.next.prev=prev
                    else:
                        prev=self.tail
                        cnt=self.nodesize-1
                        if cnt>ind:
                            while cnt>ind:
                                current=prev
                                prev=current.prev
                                cnt-=1
                            current.prev=prev.prev
                            prev.prev.next=current
                        else:
                            self.tail=prev.prev
                            self.tail.next=None

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
                prev=self.tail
                self.tail=prev.prev
                self.tail.next=None
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


    def find_lager_index(self,data): ### data보다 큰 값이 있는 최초 index의 위치를 찾아준다.
        ind=0                        ## 없을시 -1을 반환
        current=self.head
        while ind<self.nodesize:
            if current.data>data:
                return ind
            current=current.next
            ind+=1
        return -1



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

    def popleft(self):           #### 추가된 기능 popleft() 가장 왼쪽걸 꺼내준다.
        if self.nodesize>1:
            result=self.head.data
            temp=self.head
            self.head=temp.next
            self.head.prev=None
            self.nodesize-=1
            return result
        else:
            result=self.head.data
            self.head=None
            self.tail=None
            return result

