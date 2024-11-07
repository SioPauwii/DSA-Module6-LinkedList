class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = node('BMW')
        self.head.next = node('Lexus')
        self.head.next.prev = self.head
        self.head.next.next = node('Porsche')
        self.head.next.next.prev = self.head.next
        self.head.next.next.next = node('Honda')
        self.head.next.next.next.prev = self.head.next.next
        self.head.next.next.next.next = node('Audi')
        self.head.next.next.next.next.prev = self.head.next.next.next
        self.head.next.next.next.next.next = node('Hyundai')
        self.head.next.next.next.next.next.prev = self.head.next.next.next.next
        self.head.next.next.next.next.next.next = node('Toyota')
        self.head.next.next.next.next.next.next.prev = self.head.next.next.next.next.next
        self.head.next.next.next.next.next.next.next = node('Mercedes-Benz')
        self.head.next.next.next.next.next.next.next.prev = self.head.next.next.next.next.next.next
        self.head.next.next.next.next.next.next.next.next = node('Subaru')
        self.head.next.next.next.next.next.next.next.next.prev = self.head.next.next.next.next.next.next.next


    def findMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
        return slow_ptr


    def countNodes(self):
        count = 0
        current_node = self.head
        while(current_node):
            count += 1
            current_node = current_node.next
        return count


    def insertAtStart(self, data):
        new_node = node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node


    def insertAtEnd(self, data):
        new_node = node(data)
        current_node = self.head

        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node


    def insertAtPosition(self, data, position):
        new_node = node(data)
        current_node = self.head
        current_position = 0

        while(current_position != position - 2):
            current_node = current_node.next
            current_position += 1

        new_node.next = current_node.next
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node


    def insertAtMiddle(self, data):
        middle_node = self.findMiddle()
        middle_node_index = 1
        current_node = self.head

        while(current_node.data != middle_node.data):
            current_node = current_node.next
            middle_node_index += 1

        self.insertAtPosition(data, middle_node_index)


    def deleteAtPosition(self, position):
        current_node = self.head
        current_position = 0

        while(current_position != position - 2):
            current_node = current_node.next
            current_position += 1

        current_node.next = current_node.next.next
        if current_node.next:
            current_node.next.next.prev = current_node


    def replaceAtPosition(self, data, position):
        current_node = self.head
        current_position = 0

        while(current_position != position - 2):
            current_node = current_node.next
            current_position += 1

        current_node.data = data


    def countAndPrintList(self):
        current_node = self.head
        count = self.countNodes()
        print(f'\n\nThe number of nodes are {count}')
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
        print('NULL')


    def printList(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
        print('NULL')

    def printListReverse(self):
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.prev
        print('NULL')

    def startFromPrint(self, startingData):
        current_node = self.head
        while(current_node.data.lower() != startingData.lower()):
            current_node = current_node.next
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
        print('NULL')

    def printListAlphabetical(self):
        current_node = self.head
        data_list = []
        while(current_node):
            data_list.append(current_node.data)
            current_node = current_node.next
        data_list.sort()
        for data in data_list:
            print(data, end="->")
        print('NULL')

list = linkedList()
list.printList()
list.printListReverse()
list.startFromPrint('hyundai')
list.printListAlphabetical()