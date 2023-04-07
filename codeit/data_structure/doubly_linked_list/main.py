from DoublyLinkedList import DoublyLinkedList


def createList(data_list):
    dll = DoublyLinkedList()

    for data in data_list:
        dll.append(data)

    return dll


def main():
    print("< Doubly Linked List >")

    print("\n----- 삽입 연산 -----")

    dll = createList([2, 3, 5, 7, 11])

    print("INITIAL LIST : {}".format(dll))

    # tail 노드 뒤에 노드 삽입
    tail_node = dll.tail  # 4 번째(마지막)노드를 찾는다
    dll.insert_after(tail_node, 5)  # 4 번째(마지막)노드 뒤에 노드 추가
    print("Insert new node({}) after tail => {}".format(dll.tail.data, dll))  # 새로운 tail 노드 데이터 출력

    # 링크드 리스트 중간에 데이터 삽입
    insert_idx = 3
    node_at_index_3 = dll.find_node_at(insert_idx)  # 노드 접근
    dll.insert_after(node_at_index_3, 3)
    print("Insert new node after node of index {}  => {}".format(insert_idx, dll))

    # 링크드 리스트 중간에 데이터 삽입
    insert_idx = 2
    node_at_index_2 = dll.find_node_at(insert_idx)  # 노드 접근
    dll.insert_after(node_at_index_2, 2)
    print("Insert new node after node of index {}  => {}".format(insert_idx, dll))

    print("\n----- 삭제 연산 -----")

    dll = createList([2, 3, 5, 7])
    print("INITIAL LIST : {}".format(dll))

    # 두 노드 사이에 있는 노드 삭제
    node_at_index_2 = dll.find_node_at(2)
    dll.delete(node_at_index_2)
    print(dll)

    # 가장 앞 노드 삭제
    head_node = dll.head
    print(dll.delete(head_node))
    print(dll)

    # 가장 뒤 노드 삭제
    tail_node = dll.tail
    dll.delete(tail_node)
    print(dll)

    # 마지막 노드 삭제
    last_node = dll.head
    dll.delete(last_node)
    print(dll)



if __name__ == "__main__":
    main()
