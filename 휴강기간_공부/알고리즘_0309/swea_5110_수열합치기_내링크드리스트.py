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
    N,M=map(int,input().split())

    arr=[list(map(int,input().split())) for _ in range(M)]
    result=LinkedList()
    for i in range(N):
        result.append(arr[0][i])
    row=1
    while row<M:
        ind=-1
        for i in range(row*N):
            a=result.find(i)
            if a>arr[row][0]:
                ind=i
                break
        if ind!=-1:
            for i in range(N-1,-1,-1):
                result.insert(ind,arr[row][i])
        else:
            for i in range(N):
                result.append(arr[row][i])

        row+=1

    print('#{} '.format(tc),end='')
    for i in range(10):
        print(result.find(N*M-1-i),end=' ')
    print('')

    