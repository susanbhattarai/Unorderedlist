
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def setData(self, newdata):
        self.data = newdata

    def getNext(self):
        return self.next

    def setNext(self, newnext):
        self.next = newnext


class LinkedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def addItem(self, items):
        temp = Node(items)
        temp.setNext(self.head)
        self.head = temp

    def count(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while not found and current!= None:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


    def append(self, item):
        current = self.head
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
            
        temp = Node(item)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)


    def insert(self, item, index):
        count = 0
        current = self.head
        previous = None
        while count != index:
            count = count + 1
            previous = current
            current = current.getNext()
        temp = Node(item)
        if previous == None:
            temp.setNext(current)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    def index(self, item):
        index = 0
        found = False
        current = self.head
        while not found and current != None:
            if current.getData() == item:
                found = True
            else:
                index += 1
                current = current.getNext()
        if found:
            return index
        else:
            return -1

    def pop(self, index):
        currentindex = 0
        current = self.head
        previous = None
        while currentindex != index:
            previous = None
            current = current.getNext()
            currentindex += 1
        if previous == None:
            self.head = current.getNext()
            return current.getData()
        else:
            previous.setNext(current.getNext())
            return current.getData()
        
    
        
        
            
