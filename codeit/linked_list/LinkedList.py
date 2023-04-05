from Node import Node


class LinkedList:
    """ 링크드리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """ 링크드리스트 노드 추가 메서드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_node_at(self, index):
        """ 링크드리스트에서 특정 index에 있는 node를 찾는 메서드"""

        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def find_node_with_data(self, data):
        """ 링크드리스트에서 특정 data를 가지고 있는 node를 찾는 메서드"""

        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next

        return iterator

    def insert_after(self, prev_node: Node, data):
        """ 링크드리스트에서 prev_node 뒤에 data를 가진 새로운 노드를 삽입하는 메서드"""

        new_node = Node(data)

        # 맨 뒤에 삽입하는 경우
        if self.tail == prev_node:
            self.tail.next = new_node
            self.tail = new_node
        # 중간에 삽입하는 경우
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node

    def prepend(self, data):
        """ 링크드리스트의 맨 앞에 노드를 삽입하는 메서드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_after(self, prev_node):
        """링크드리스트에서 prev_node 뒤에 있는 노드를 삭제하는 메서드. 삭제된 데이터를 반환한다."""
        data = prev_node.next.data

        if prev_node.next is self.tail:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = prev_node.next.next

        return data

    def popleft(self):
        """ 링크드리스트에서 맨 앞에 있는 노드를 삭제하는 메서드"""
        data = self.head.data

        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        return data

    def __str__(self):
        """ 링크드리스트 출력 메서드"""
        iterator = self.head
        res_str = "|"

        while iterator is not None:
            res_str += f" {iterator.data} |"
            iterator = iterator.next

        return res_str


# --- 노드 추가
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
print(linked_list)

# --- 특정 인덱스에 있는 노드 탐색
idx = 3
print("data at index of {} : {}".format(idx, linked_list.find_node_at(idx).data))
linked_list.find_node_at(2).data = 13
print(linked_list)

# --- 특정 데이터를 갖는 노드 탐색
node_with_6 = linked_list.find_node_with_data(6)
if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6을 갖는 노드는 없습니다.")

# --- 특정 노드 뒤에 새 노드 삽입
node_2 = linked_list.find_node_at(2)
linked_list.insert_after(node_2, 33)
print(linked_list)
linked_list.insert_after(linked_list.head, 88)
print(linked_list)

# --- 맨 앞에 노드 삽입
linked_list.prepend(-1)
linked_list.prepend(-2)
print(linked_list)
print("Head node: {} \nTail node: {}".format(linked_list.head.data, linked_list.tail.data))  # head, tail 노드가 제대로 설정됐는지 확인

# --- 특정 노드 뒤에 있는 노드 삭제
idx = 3
node_3 = linked_list.find_node_at(idx)
deleted_data = linked_list.delete_after(node_3)
print("Delete next node of a node with index {}, deleted data is {}".format(idx, deleted_data))
print(linked_list)

# --- 맨 앞에 있는 노드 삭제
deleted_data = linked_list.popleft()
print("deleted data is {}".format(deleted_data))
print(linked_list)