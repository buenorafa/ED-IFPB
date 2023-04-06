class QueueException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)


class Queue:
    def __init__(self, capacity=10) -> None:
        self.__capacity = capacity
        self.__storage = [None]*capacity
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def isFull(self):
        return self.__capacity == self.__size

    def isEmpty(self):
        return self.__size == 0

    def enqueue(self, data: any):
        if self.isFull():
            raise QueueException('Queue is already full!')
        self.__storage[self.__tail] = data
        self.__tail = (self.__tail + 1) % self.__capacity
        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise QueueException('Queue is empty!')
        data = self.__storage[self.__head]
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return data

    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        if self.isEmpty():
            return 'Queue is empty!'
        result = 'queue: ['
        index = self.__head
        for i in range(self.__size):
            result += f'{self.__storage[index]}'
            index = (index + 1) % self.__capacity
            if index != self.__tail:
                result += ', '
        result += ']'
        return result


# TESTS

# q1 = Queue()
# for i in range(10):
#     q1.enqueue(i)
# # str method
# print(q1)
# # Full queue
# try:
#     q1.enqueue(10)
# except QueueException as qe:
#     print(qe)

# # Empty queue
# for i in range(10):
#     print(q1.dequeue())
# try:
#     q1.dequeue()
# except QueueException as qe:
#     print(qe)
