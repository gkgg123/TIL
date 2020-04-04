class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
        self.nodesize=0
    def append(self,data):
        newNode=Node(data)  ### head는 제일 처음 next가 있으면 연결해준다.
        if (self.head):
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
        else:
            self.head=newNode
        self.nodesize+=1
    def insert(self,ind,data):
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

    def find(self,ind):
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
    def change(self,ind,data):
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
    def remove(self,ind):
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
    def print_all(self):
        result=[]
        if self:
            cnt=0
            current=self.head
            result.append(current.data)
            while current.next:
                current=current.next
                result.append(current.data)
            return result


T=int(input())

for tc in range(1,T+1):
    N,M,L=map(int,input().split())
    arr=list(map(int,input().split()))
    result=LinkedList()
    for i in arr:
        result.append(i)
    for i in range(M):
        doit=list(input().split())

        if doit[0]=='I':
            result.insert(int(doit[1]),int(doit[2]))
        elif doit[0]=='D':
            result.remove(int(doit[1]))
        else:
            result.change(int(doit[1]),int(doit[2]))


    result=result.print_all()

    if L<len(result):
        print('#{} {}'.format(tc,result[L]))
    else:
        print('#{} -1'.format(tc))