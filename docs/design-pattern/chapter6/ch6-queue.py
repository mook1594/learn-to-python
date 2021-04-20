from queue import Queue, LifoQueue, PriorityQueue

## FIFO queue
lineup = Queue(maxsize=3)
lineup.put('one')
lineup.put('two')
lineup.put('three', timeout=1)
print(lineup.full())
print(lineup.get())
print(lineup.get())
print(lineup.get())

print('=' * 20)

## stack
stack = LifoQueue(maxsize=3)
stack.put('one')
stack.put('two')
stack.put('three', block=False)
print(stack.get())
print(stack.get())
print(stack.get())

print('=' * 20)

## Priority Queue
heap = PriorityQueue(maxsize=5)
heap.put((3, 'three'))
heap.put((4, 'four'))
heap.put((1, 'one'))
heap.put((2, 'two'))
heap.put((5, 'five'), block=False)
while not heap.empty():
    print(heap.get())

