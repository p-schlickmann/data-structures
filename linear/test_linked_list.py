from linear.linked_list import LinkedList


def test_linked_list():
    lst = LinkedList()

    # []
    lst.insert_at_the_start(10)
    # [10]
    assert lst.head == lst.get_current()
    assert lst.head.val == 10
    assert lst.head.next is None
    assert lst.head.prev is None

    # [10]
    lst.insert_at_the_start(20)
    # [20, 10]
    cursor = lst.get_current()
    assert lst.head.val == 20
    assert lst.head == cursor
    assert lst.head.next.prev == lst.head
    assert lst.head.prev is None

    # [20, 10]
    lst.insert_at_the_end(30)
    # [20, 10, 30]
    last = lst.get_current()
    assert last.val == 30
    assert last.next is None
    assert last.prev.val == 10

    # [20, 10, 30]
    lst.insert_after_current(5)
    # [20, 10, 30, 5]
    current = lst.get_current()
    assert current.val == 5
    assert current.next is None
    assert current.prev.val == 30

    # [20, 10, 30, 5]
    lst.insert_before_current(60)
    # [20, 10, 30, 60, 5]
    current = lst.get_current()
    assert current.val == 60
    assert current.next.val == 5
    assert current.prev.val == 30

    # [20, 10, 30, 60, 5]
    lst.insert_at(1, 50)
    # [20, 50, 10, 30, 60, 5]
    current = lst.get_current()
    assert current.val == 50
    assert current.prev.val == 20
    assert current.next.val == 10

    # [20, 50, 10, 30, 60, 5]
    result = lst.search(100)
    assert result is None
    result = lst.search(50)
    assert result.val == 50
    assert result.next.val == 10
    assert result.prev.val == 20

    # [20, 50, 10, 30, 60, 5] current: 50
    lst.delete_current()
    # [20, 10, 30, 60, 5]
    current = lst.get_current()
    assert current.val == 20
    assert current.next.val == 10
    assert current.prev is None

    # [20, 10, 30, 60, 5]
    lst.delete_first()
    # [10, 30, 60, 5]
    current = lst.get_current()
    assert current.val == 10
    assert current.prev is None
    assert current.next

    # delete last
    # [10, 30, 60, 5]
    lst.delete_last()
    # [10, 30, 60]
    current = lst.get_current()
    assert current.val == 60
    assert current.prev.val == 30
    assert current.next is None

    # [10, 30, 60]
    lst.delete(30)
    # [10, 60]
    current = lst.get_current()
    assert current.val == 10
    assert lst.head.val == 10
    assert current.prev is None
    assert current.next.val == 60
    assert current.next.prev.val == 10

    # [10, 60]
    lst.delete_at(1)
    # [10]
    current = lst.get_current()
    assert current.val == 10
    assert lst.head.val == 10
    assert current.prev is None
    assert current.next is None


test_linked_list()
