## (1) 연결 리스트
○ 링크드 리스트(linked list)
○ 노드(데이터, 포인터)가 한 줄로 연결되어 있는 방식의 자료구조
○ 포인터는 다음 또는 이전의 노드와의 연결(주소값)을 담당
○ 개념이 복잡하고, 구현이 어려움
○ 메모리 사용 효율성이 높음
○ 데이터 접근이 느림
○ 단일 연결 리스트/이중 연결 리스트/원형 연결 리스트

## (2) 연결 리스트 실습 코드 1
<pre>
    <code>
class SList:
    class Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        print("난 SList의 생성자")  
        self.head = None  
        self.size = 0
    def isEmpty(self):
        return self.size == 0    
    def insert_front(self, item):
        if self.isEmpty():
            self.head = self.Node(item , None)
        else:
            self.head = self.Node(item, self.head)
        self.size += 1

    def printList(self):
        p = self.head
        while p:
            if p.next is not None:
                print(p.item , "=>", end="")
            else:
                print(p.item)
            p = p.next

def globalFunc():
    pass

if __name__=="__main__":
    s = SList()
    s.insert_front("apple")
    s.insert_front("orange")
    s.printList()
        
</code>
</pre>

## (3) 연결 리스트 실습코드 2
 <pre>
    <code>   
class SList:
    class Node:
        def __init__(self, item, link):
           self.item = item
           self.next = link

    def __init__(self):
        print("난 SList의 생성자")
        self.head = None
        self.size = 0
    def isEmpty(self):
        return self.size == 0

    def insert_front(self, item):
        if self.isEmpty():
            self.head = self.Node(item , None)
        else:
            self.head= self.Node(item, 
                                self.head)
        self.size += 1

    def insert_after(self, item, p):
        p.next = self.Node(item , p.next)
        self.size += 1

    def search(self, target):
        p = self.head
        for k in range(self.size):
            if target == p.item:
                return k 
            p = p.next

    #p가 참조하는 노드의 다음 노드를 삭제
    def delete_after(self, p):
        if self.isEmpty():
            print("리스트가 텅 비어있어서 삭제불가")
            return None
        else:
            t = p.next
            p.next = t.next
            del t
            self.size -= 1

    def delete_front(self):
        if self.isEmpty():
            print("리스트가 텅비어서 삭제 불가")
            return None
        else:
            t = self.head
            self.head = self.head.next
            del t 
            self.size -= 1 

    #사용자가 원하는 인덱스에 새로운 노드 삽입하는 함수
    def insert_index(self, index, item):
        pass
     
    #사용자가 원하는 인덱스에 새로운 노드 삭제제하는 함수
    def delete_index(self, index):
        pass
      
    #연결리스트의 맨 마지막 노드를 삭제하는 함수
    def delete_final(self):
        pass
       
    def printList(self):
        p = self.head
        while p:
            if p.next  is not None:
                print(p.item , "=>", end="")
            else:
                print(p.item)
            p = p.next

def globalFunc():
    pass

if __name__ == "__main__":
    s = SList()
    s.insert_front("apple")
    s.insert_front("orange")
    s.printList()
    s.insert_after("cherry" ,s.head.next)
    s.printList()
    s.insert_front('pear')
    s.insert_front('melon')
    s.insert_front('grape')
    s.insert_front('peach')
    s.insert_front('banana')
    s.insert_front('watermelon')

    s.printList()
    print("cherry는 %d번째 노드에 있다" % 
            (s.search("cherry") + 1))
    s.delete_after(s.head)
    s.printList()
    print("첫번째 노드 삭제후 \t\t")
    s.delete_front()
    s.printList()

    s.insert_index(2, "melon")
    s.delete_index(3)
    s.delete_final
    s.printList()


    </code>
 </pre>
