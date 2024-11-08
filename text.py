class Node:
    def __init__(self, char, next = None, prev = None):
        self.char = char
        self.next = next
        self.prev = prev
    
    def __next__(self):
        return self.next
    
class Text:
    def __init__(self, text = ""):
        if (not (isinstance(text, str) or isinstance(text, Text))):
            raise TypeError()
        self.text = text
    
