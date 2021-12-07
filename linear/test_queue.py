from linear.my_queue import EmptyQueueException, Queue, QueueLimitReachedException


def test_queue():
    print('\n------- TESTES FILA -------')
    queue = Queue(max_size=5)
    try:
        queue.dequeue()
    except EmptyQueueException:
        pass
    else:
        assert False, 'Fila vazia permitindo dequeue'

    queue.enqueue(0)
    print(f'Enqueued 0, head: {queue.head}, tail: {queue.tail}')
    assert queue.tail == 0
    assert queue.head == 0

    for i in range(1, 5):
        queue.enqueue(i)
        print(f'Enqueued {i}, head: {queue.head}, tail: {queue.tail}')
        assert queue.head == 0
        assert queue.tail == i

    try:
        queue.enqueue(5)
    except QueueLimitReachedException:
        pass
    else:
        assert False, 'Limite da fila sendo desrespeitado'

    for i in range(4):
        queue.dequeue()
        print(f'Dequeued, head: {queue.head}, tail: {queue.tail}')
        assert queue.head == i + 1
        assert queue.tail == 4

    assert queue.head == 4
    queue.dequeue()
    assert queue.tail is None
    assert queue.head is None
    print('OK')


if __name__ == '__main__':
    test_queue()
