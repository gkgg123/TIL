import sys
sys.stdin=open('5110.txt','r')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class CircleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = None
        self.list_size = 1

    def __str__(self):
        print_list = '[ '
        node = self.head
        while True:
            print_list += str(node)
            if node == self.tail:
            # 단순 연결 리스트와 달리
            # 노드가 테일 노드면 끝난다
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = self.head
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        self.tail.next = new_node
        self.list_size += 1

    def insertMiddle(self, num, data):
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    def insertLast(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head.next = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head
        self.list_size += 1

    def selectNode(self, num):
        if self.list_size < num:
            print("Overflow")
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node

    def deleteNode(self, num):
        if self.list_size < 1:
            return # Underflow
        elif self.list_size < num:
            return # Overflow

        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num - 1)
        node.next = node.next.next
        del_node = node.next
        del del_node

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)


T=int(input())

for tc in range(1,T+1):
    N,M=map(int,input().split())
    for i in range(M):
        if i==0:
            temp=list(map(int,input().split()))
            result=CircleLinkedList(temp[0])
            for i in temp[1:]:
                result.insertLast(i)
        else:
            temp=list(map(int,input().split()))
            for k in range(int(result.size())):
                tem=int(str(result.selectNode(k)))
                if tem>temp[0]:
                    if k==0:
                        for j in range(N-1,-1,-1):
                            result.insertFirst(temp[j])
                    else:
                        for j in range(N-1,-1,-1):
                            result.insertMiddle(k-1,temp[j])
                    break
            else:
                for j in temp:
                    result.insertLast(j)
    print('#{} '.format(tc),end='')
    for i in range(10):
        print(result.selectNode(N*M-1-i),end=' ')
    print('')
