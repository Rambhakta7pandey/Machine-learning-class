# ----------------------------------------
# QUEUE IMPLEMENTATION USING CLASS
# ----------------------------------------

class Queue:
    def __init__(self, size):
        self.size = size
        self.items = []
        self.front = 0
        self.rear = -1

    # Check if queue is empty
    def is_empty(self):
        return self.front > self.rear

    # Check if queue is full
    def is_full(self):
        return self.rear == self.size - 1

    # Insert (enqueue)
    def enqueue(self, value):
        if self.is_full():
            print("Queue Overflow ❌")
        else:
            self.items.append(value)
            self.rear += 1
            print(f"{value} added to queue ✔")

    # Delete (dequeue)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow ❌")
        else:
            value = self.items[self.front]
            self.front += 1
            print(f"{value} removed from queue ✔")
            return value

    # Peek / front element
    def peek(self):
        if self.is_empty():
            print("Queue is empty ❌")
        else:
            print(f"Front element → {self.items[self.front]}")

    # Display queue contents
    def display(self):
        if self.is_empty():
            print("Queue is empty ❌")
        else:
            print("Queue:", self.items[self.front:self.rear + 1])


# ------------------------------
# RUNNING THE QUEUE OPERATIONS
# ------------------------------

def main():
    size = int(input("Enter queue size: "))
    q = Queue(size)

    while True:
        print("\n=== QUEUE MENU ===")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            val = int(input("Enter value to add: "))
            q.enqueue(val)

        elif choice == 2:
            q.dequeue()

        elif choice == 3:
            q.peek()

        elif choice == 4:
            q.display()

        elif choice == 5:
            print("Exiting… 👋")
            break

        else:
            print("Bruh… invalid choice 😭")


main()
