class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.nodesize=0
    def append(self,data):  ### 끝에 값을 추가해주는 메서드
        newNode=Node(data)  
        if (self.head):
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
        self.nodesize+=1
    def insert(self,ind,data):  ### 해당 index위치에 data를 넣어준다.
        newNode=Node(data)
        self.nodesize+=1
        if self.head:
            if ind==0:
                temp=Node(self.head.data,self.head.next)
                self.head=newNode
                self.head.next=temp
            else:
                current=self.head
                cnt=0
                while cnt<ind:
                    prev=current
                    current=current.next
                    cnt+=1
                prev.next=newNode
                newNode.next=current
                
        else:
            self.head=newNode

    def find(self,ind):  #### 입력된 ind의 값이 무엇인지 알려준다.
        if self.head:
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
        if self:
            current=self.head
            result.append(current.data)
            while current.next:
                current=current.next
                result.append(current.data)
            return result


### 사용법 ####
r=LinkedList()  ### 먼저 인스턴스를 만들어준다.

r.append(1)   ### 이렇게 값을 추가시켜준다.

r.append(2)
r.append(3)
print(r.print_all()) ### print_all()을 하면 지금까지 저장된 값을 리스트로 반환해서 보여준다.

r.insert(1,99)  ### 1번째 index에 99을 넣고 뒤를 밀어준다.
print(r.print_all())
r.remove(1)     ### 1번째 index의 값을 삭제해준다.
print(r.print_all())
print(r.find(2))      #### 2번째 index 값을 찾고싶을때 쓴다.
r.change(2,999)      ### 2번째 index의 값을 999으로 바꿔준다.
print(r.print_all())