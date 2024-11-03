class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node('Lexus')
        self.head.next = node('Porsche')
        self.head.next.next = node('Lincoln')
        self.head.next.next.next = node('Toyota')
        self.head.next.next.next.next = node('Mercedes-Benz')

    def findMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
        return slow_ptr.data
    
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
        self.head = new_node

    def insertAtEnd(self, data):
        new_node = node(data)
        current_node = self.head

        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node

    def insertAtPosition(self, data, position):
        new_node = node(data)
        current_node = self.head
        current_position = 0

        while(current_position != position - 2):
            current_node =  current_node.next
            current_position += 1

        new_node.next = current_node.next
        current_node.next = new_node

    def insertAtMiddle(self, data):
        middle_node = self.findMiddle()
        middle_node_index = 1
        current_node = self.head

        while(current_node.data != middle_node):
            current_node = current_node.next
            middle_node_index += 1

        self.insertAtPosition(data, middle_node_index)

    def deleteAtPosition(self, position):
        current_node = self.head
        current_position = 0

        while(current_position != position - 2):
            current_node =  current_node.next
            current_position += 1

        current_node.next = current_node.next.next

    def replaceAtPosition(self, data, position):
        current_node = self.head
        current_position = 0

        while(current_position != position - 1):
            current_node =  current_node.next
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

car_list = linkedList()

def main():
    print("Linked List Operations\n\n")
    
    print(f'\n\nCurrent List:')
    print(f'{car_list.printList()}\n')

    print("1. Add  at start")
    print("2. Add at end")
    print("3. Add at position")
    print("4. Insert in the middle")
    print("5. Delete at position")
    print("6. Replace at position")
    print("7. Count Nodes and Print")
    print("8. Print List")
    print("9. Exit the progam")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): \n\n")

    if choice == "1":
        data = input("Enter the data: \n")
        car_list.insertAtStart(data)
    elif choice == "2":
        data = input("Enter the data: \n")
        car_list.insertAtEnd(data)
    elif choice == "3":
        data = input("Enter the data: \n")
        position = int(input("Enter the position: \n"))
        car_list.insertAtPosition(data, position)
    elif choice == "4":
        data = input("Enter the data: \n")
        car_list.insertAtMiddle(data)
    elif choice == "5":
        position = int(input("Enter the position: \n"))
        car_list.deleteAtPosition(position)
    elif choice == "6":
        data = input("Enter the new data: \n")
        position = int(input("Enter the position: \n"))
        car_list.replaceAtPosition(data, position)
    elif choice == "7":
        car_list.countAndPrintList()
    elif choice == "8":
        car_list.printList()
    elif choice == "9":
        exit()
    else:
        print("Invalid choice")

    main()

main()