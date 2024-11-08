class Node:
    def __init__(self, char, next = None, prev = None):
        self.char = char
        self.next = next
        self.prev = prev
    
    def __next__(self):
        return self.next
    
class Text:
    def __init__(self, text = ""):
        self.checkType(text, haveToBeText=True, haveToBeString=True)
        self.head = None
        self.tail = None
        for char in text:
            self.append(char)

    def checkType(self, text, haveToBeString = False, haveToBeText = False, haveToBeInt = False):
        if (haveToBeString and haveToBeText):
            if (not (isinstance(text, str) or isinstance(text, Text))):
                raise TypeError()
        elif (haveToBeString):
            if (not isinstance(text, str)):
                raise TypeError()
        elif (haveToBeText):
            if (not isinstance(text, Text)):
                raise TypeError()
        elif (haveToBeInt):
            if (not isinstance(text, int)):
                raise TypeError()
    
    def checkLength(self, text, maxLength = 1):
        if (len(text) > maxLength):
            raise ValueError()
        
    def parseIndex(self, index):
        if (index < 0):
            index = len(self.text) + index
        if (index < 0 or index >= len(self.text)):
            raise IndexError()
        return index

    def append(self, text):
        self.checkType(text, haveToBeString=True)
        self.checkLength(text)
        if (self.head == None):
            self.head = Node(text)
            self.tail = self.head
        else:
            self.tail.next = Node(text, None, self.tail)
            self.tail = self.tail.next

    def clear(self):
        self.head = None
        self.tail = None

    def copy(self):
        return Text(self.text)
    
    def extend(self, text):
        self.checkType(text, haveToBeString=True, haveToBeText=True)
        for char in text:
            self.append(char)

    def insert(self, index, text):
        self.checkType(text, haveToBeString=True)
        self.checkType(index, haveToBeInt=True)
        self.checkLength(text)
        self.parseIndex(index)

        # // check of self is empty

        if (index == 0):
            if (self.head == None):
                self.head = Node(text)
                self.tail = self.head
            newHead = Node(text, self.head, None)
            self.head = newHead
            self.head.next.prev = self.head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = Node(text, current.next, current)
            current.next.next.prev = current.next
            if (current.next.next == None):
                self.tail = current.next

    def pop(self, index = -1):
        self.checkType(index, haveToBeInt=True)
        self.parseIndex(index)
        if (index == 0):
            result = self.head.char
            self.head = self.head.next
            self.head.prev = None
            if (self.head == None):
                self.tail = None
            return result
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            result = current.next.char
            current.next = current.next.next
            current.next.next.prev = current.next
            if (current.next == None):
                self.tail = current
            return result
    
    def head(self):
        return self.head
    
    def tail(self):
        return self.tail
    
    def __len__(self):
        current = self.head
        length = 0
        while (current != None):
            length += 1
            current = current.next
        return length
    
    def __str__(self):
        current = self.head
        result = ""
        while (current != None):
            result += current.char
            current = current.next
        return result
    
    def __getitem__(self, index):
        self.checkType(index, haveToBeInt=True)
        index = self.parseIndex(index)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.char
    
    def __setitem__(self, index, value):
        self.checkType(index, haveToBeInt=True)
        self.checkType(value, haveToBeString=True)
        self.checkLength(value)
        index = self.parseIndex(index)
        current = self.head
        for _ in range(index):
            current = current.next
        current.char = value

    def __add__(self, other):
        self.checkType(other, haveToBeText=True, haveToBeString=True)
        return Text(str(self) + str(other))
    
    def __iadd__(self, other):
        self.checkType(other, haveToBeText=True, haveToBeString=True)
        self.extend(str(other))
        return self
    
    def __contains__(self, item):
        self.checkType(item, haveToBeString=True, haveToBeText=True)
        current = self.head
        while (current != None):
            if (current.char == item):
                return True
            current = current.next
        return False