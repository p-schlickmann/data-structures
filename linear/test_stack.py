from linear.stack import EmptyStackException, Stack, StackLimitReachedException


def test_stack():
    print('\n\n------- TESTES PILHA -------')
    stack = Stack(max_size=5)
    try:
        stack.pop()
    except EmptyStackException:
        pass
    else:
        assert False, 'Pilha vazia permitindo pop'

    for i in range(5):
        stack.push(i)
        print(f'Pushed {i}, novo topo: {stack.top}')
        assert stack.top == i

    try:
        stack.push(5)
    except StackLimitReachedException:
        pass
    else:
        assert False, 'Limite da pilha sendo desrespeitado'

    for i in reversed(range(4)):
        stack.pop()
        print(f'Pop, novo topo: {stack.top}')
        assert stack.top == i

    stack.pop()
    assert stack.top is None
    print('OK')


if __name__ == '__main__':
    test_stack()
