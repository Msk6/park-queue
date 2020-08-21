class Node:
    def __init__(self, group_size, next=None):
        self.group_size = group_size
        self.next = next
    
    def get_group_size(self):
        return self.group_size

    def get_next(self):
        return self.next
    
    def set_year(self, group_size):
        self.group_size = group_size
    
    def set_next(self, node):
        self.next = node

class Queue:

    def __init__(self, limit=50, front=None):
        self.front = front
        self.back = front
        self.limit = limit
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length == self.limit

    def enqueue(self, group_size):
        if self.is_full():
            print("Can't accept more")
            return
        elif self.is_empty():
            node = Node(group_size)
            self.front = node
            self.back = node
        else:
            node = Node(group_size)
            self.back.set_next(node)
            self.back = node

        self.length += 1

    
    def dequeue(self):
        # condition is_empty
        if self.is_empty():
            print("There is no groups")
        else:
            de_node = self.front
            self.front = de_node.get_next()
            self.length -= 1
            return de_node.get_group_size()
        return

# Calculate waiting time using Queue length
def waiting_time():
    waiting_time_seconds = ((waitiing_queue.length * 30) % 60)
    waiting_time_minutes = ((waitiing_queue.length * 30) / 60)
    waiting_time_hours = ((waitiing_queue.length * 30) / 3600)

    print ("%d H %d m %d s" % (waiting_time_hours, waiting_time_minutes, waiting_time_seconds))

# Queue Initialization
waitiing_queue = Queue()
waitiing_queue.enqueue(7)
waitiing_queue.enqueue(9)
waitiing_queue.enqueue(10)
waitiing_queue.enqueue(1)
waitiing_queue.enqueue(5)
waitiing_queue.enqueue(11)
waitiing_queue.enqueue(1)
waitiing_queue.enqueue(12)


waiting_time()

controler = True

# Add new groups
while controler:

    try:
        group_size = int(input("Number of persons (Enter 0 if you want to exit): "))
        if group_size == 0:
            break
        elif group_size <= 12:
            waitiing_queue.enqueue(group_size)
        else:
            print ("For your enjoy, the max capacity is 12 persons")
    except: 
        print ("Enter your group size")

waiting_time()

# Next in line go to the ride
print (f'Next in line group has {waitiing_queue.dequeue()} persons')

waiting_time()




    


