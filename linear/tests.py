from linear.pile import Pile, EmptyPileException, PileLimitReachedException
from linear.queue import Queue, EmptyQueueException, QueueLimitReachedException


def test_pile():
    print('\n\n------- TESTES PILHA -------')
    pile = Pile(max_size=5)
    try:
        pile.pop()
    except EmptyPileException:
        pass
    else:
        assert False, 'Pilha vazia permitindo pop'
    
    for i in range(5):
        pile.push(i)
        print(f'Pushed {i}, novo topo: {pile.top.content}')
        assert pile.top.content == i
        
    try:
        pile.push(5)
    except PileLimitReachedException:
        pass
    else:
        assert False, 'Limite da pilha sendo desrespeitado'
    
    for i in reversed(range(4)):
        pile.pop()
        print(f'Pop, novo topo: {pile.top.content}')
        assert pile.top.content == i
        
    pile.pop()
    assert pile.top is None
    print('OK')
    
    
def test_queue():
    print('\n\n------- TESTES FILA -------')
    queue = Queue(max_size=5)
    try:
        queue.dequeue()
    except EmptyQueueException:
        pass
    else:
        assert False, 'Fila vazia permitindo dequeue'
    
    queue.enqueue(0)
    print(f'Enqueued 0, head: {queue.head.content}, tail: {queue.tail.content}')
    assert queue.tail.content == 0
    assert queue.head.content == 0

    for i in range(1, 5):
        queue.enqueue(i)
        print(f'Enqueued {i}, head: {queue.head.content}, tail: {queue.tail.content}')
        assert queue.head.content == 0
        assert queue.tail.content == i

    try:
        queue.enqueue(5)
    except QueueLimitReachedException:
        pass
    else:
        assert False, 'Limite da fila sendo desrespeitado'

    for i in range(4):
        queue.dequeue()
        print(f'Dequeued, head: {queue.head.content}, tail: {queue.tail.content}')
        assert queue.head.content == i + 1
        assert queue.tail.content == 4

    assert queue.head.content == 4
    queue.dequeue()
    assert queue.tail is None
    assert queue.head is None
    print('OK')


if __name__ == '__main__':
    test_pile()
    test_queue()
