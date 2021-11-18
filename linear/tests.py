from linear.stack import Stack, EmptyStackException, StackLimitReachedException
from linear.queue import Queue, EmptyQueueException, QueueLimitReachedException


def test_pile():
    print('\n\n------- TESTES PILHA -------')
    pile = Stack(max_size=5)
    try:
        pile.pop()
    except EmptyStackException:
        pass
    else:
        assert False, 'Pilha vazia permitindo pop'
    
    for i in range(5):
        pile.push(i)
        print(f'Pushed {i}, novo topo: {pile.top}')
        assert pile.top == i
        
    try:
        pile.push(5)
    except StackLimitReachedException:
        pass
    else:
        assert False, 'Limite da pilha sendo desrespeitado'
    
    for i in reversed(range(4)):
        pile.pop()
        print(f'Pop, novo topo: {pile.top}')
        assert pile.top == i
        
    pile.pop()
    assert pile.top is None
    print('OK')
    
    
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
    test_pile()
    test_queue()
