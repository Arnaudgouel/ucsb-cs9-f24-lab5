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
        self.text = text

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

    def append(self, text):
        self.checkType(text, haveToBeString=True)
        self.checkLength(text)
        self.text += text

    def clear(self):
        self.text = ""

    def copy(self):
        return Text(self.text)
    
    def extend(self, text):
        self.checkType(text, haveToBeString=True, haveToBeText=True)
        self.text += text

    def insert(self, index, text):
        self.checkType(text, haveToBeString=True)
        self.checkType(index, haveToBeInt=True)
        self.checkLength(text)
        self.text = self.text[:index] + text + self.text[index:]

    def pop(self, index = -1):
        self.checkType(index, haveToBeInt=True)
        if (index < 0):
            index = len(self.text) + index
        if (index < 0 or index >= len(self.text)):
            raise IndexError()
        result = self.text[index]
        self.text = self.text[:index] + self.text[index + 1:]
        return result