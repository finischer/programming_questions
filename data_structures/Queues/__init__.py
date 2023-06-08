from Queue import Queue

if __name__ == "__main__":
    q = Queue(10)

    print("Head: ", q.peek())

    q.enqueue(9)

    print("Head: ", q.peek())

    q.dequeue()

    print("Head: ", q.peek())
