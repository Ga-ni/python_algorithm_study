class Node:
    """ Node 클래스 """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """ LinkedList class """

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        iterator = self.head
        result = "| "

        while iterator is not None:
            result += f"{iterator.data} | "
            iterator = iterator.next
        return result

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # if self.head is self.tail is node_to_delete:
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node_to_delete:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail is node_to_delete:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        return node_to_delete.data

    def insert_after(self, previous_node, data):
        """링크드 리스트 추가 연산 메소드"""

        if previous_node is self.tail:
            self.append(data)
        else:
            new_node = Node(data)
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next = new_node
            previous_node.next.prev = new_node

    def append(self, data):
        """ 맨 뒤에 새로운 노드 추가 """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        """ 특정 index에 있는 node를 찾는 메서드"""

        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """ 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""

        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return None
