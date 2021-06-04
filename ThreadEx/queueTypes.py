import queue

q = queue.Queue()
q.put(400)
q.put(500)
q.put(100)
q.put(900)

while not q.empty():
    print(q.get(), end =' ')

print("\n Lifo Queue")
ql = queue.LifoQueue()
ql.put(400)
ql.put(500)
ql.put(100)
ql.put(900)

while not ql.empty():
    print(ql.get(), end =' ')

print("\n priority Queue")
qp = queue.PriorityQueue()
qp.put(400)
qp.put(500)
qp.put(100)
qp.put(900)

while not qp.empty():
    print(qp.get(), end =' ')

print("\n Passing tuple in the priority Queue")
qpl = queue.PriorityQueue()
qpl.put((400,"John"))
qpl.put((500, "Harry"))
qpl.put((100,"Kim"))
qpl.put((900,"Den"))

while not qpl.empty():
    print(qpl.get(), end =' ')