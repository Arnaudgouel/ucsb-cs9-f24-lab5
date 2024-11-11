class Node:
    def __init__(self, char, next = None, prev = None):
        self.char = char
        self.next = next
        self.prev = prev
        self.index = 0
    
    def __next__(self):
        return self.next
    
class Text:
    def __init__(self, text = ""):
        self.checkType(text, haveToBeText=True, haveToBeString=True)
        self.headPrt = None
        self.tailPrt = None
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
        if (len(text) != maxLength):
            raise ValueError()
        
    def parseIndex(self, index , toInsert = False):
        if (index < 0):
            newIndex = len(self) + index
        else:
            newIndex = index
        if (not toInsert and (newIndex < 0 or (newIndex >= len(self) and len(self) != 0))):
            raise IndexError(newIndex, len(self))
        elif (toInsert and newIndex < 0 or newIndex > len(self)):
            raise IndexError(newIndex, len(self), "test")
        return newIndex

    def append(self, text):
        self.checkType(text, haveToBeString=True)
        self.checkLength(text)
        newNode = Node(text)
        if (self.headPrt is None):
            self.headPrt = newNode
            self.tailPrt = newNode
        else:
            self.tailPrt.next = newNode
            newNode.prev = self.tailPrt
            self.tailPrt = newNode

    def clear(self):
        self.headPrt = None
        self.tailPrt = None

    def copy(self):
        newText = Text()
        for char in self:
            newText.append(char)
        return newText
    
    def extend(self, text):
        self.checkType(text, haveToBeString=True, haveToBeText=True)
        for char in text:
            self.append(char)

    def insert(self, index, text):
        self.checkType(text, haveToBeString=True)
        self.checkType(index, haveToBeInt=True)
        self.checkLength(text)
        index = self.parseIndex(index, True)

        if (index == 0):
            if (self.headPrt is None):
                self.headPrt = Node(text)
                self.tailPrt = self.headPrt
            else:
                newHead = Node(text, self.headPrt, None)
                self.headPrt = newHead
                self.headPrt.next.prev = self.headPrt
        else:
            current = self.headPrt
            for _ in range(index - 1):
                current = current.next
            current.next = Node(text, current.next, current)
            if (current.next.next == None):
                self.tailPrt = current.next
            else:
                current.next.next.prev = current.next


    def pop(self, index = -1):
        self.checkType(index, haveToBeInt=True)
        index = self.parseIndex(index)
        if len(self) == 0:
            raise IndexError("Cannot pop from empty text")
            
        
        if index == 0:
            char = self.headPrt.char
            self.headPrt = self.headPrt.next
            if self.headPrt:
                self.headPrt.prev = None
            else:
                self.tailPrt = None
        elif index == len(self) - 1:
            char = self.tailPrt.char
            self.tailPrt = self.tailPrt.prev
            if self.tailPrt:
                self.tailPrt.next = None
            else:
                self.headPrt = None
        else:
            node = self._get_node_at_index(index)
            char = node.char
            node.prev.next = node.next
            node.next.prev = node.prev
        
        return char
    
    def head(self):
        return self.headPrt
    
    def tail(self):
        return self.tailPrt
    
    def __len__(self):
        current = self.headPrt
        length = 0
        while (current != None):
            length += 1
            current = current.next
        return length
    
    def __str__(self):
        current = self.headPrt
        result = ""
        while (current != None):
            result += current.char
            current = current.next
        return result
    
    def _get_node_at_index(self, index):
        index = self.parseIndex(index)
        
        if index <= len(self) // 2:
            current = self.headPrt
            for _ in range(index):
                current = current.next
        else:
            current = self.tailPrt
            for _ in range(len(self) - 1 - index):
                current = current.prev
                
        return current
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(len(self))
            result = Text()
            indices = range(start, stop, step)
            for i in indices:
                result.append(self._get_node_at_index(i).char)
            return result
        else:
            return self._get_node_at_index(index).char
    
    def __setitem__(self, index, value):
        self.checkType(index, haveToBeInt=True)
        self.checkType(value, haveToBeString=True)
        self.checkLength(value)
        index = self.parseIndex(index)
        current = self.headPrt
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
        current = self.headPrt
        if isinstance(item, str) or isinstance(item, Text):
            item_length = len(item)
            while current is not None:
                runner = current
                match = True
                for char in item:
                    if runner is None or runner.char != char:
                        match = False
                        break
                    runner = runner.next
                if match:
                    return True
                current = current.next
            return False
        else:
            raise TypeError("Invalid argument type.")
    
    def __iter__(self):
        self.current = self.headPrt
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        char = self.current.char
        self.current = self.current.next
        return char

    

                