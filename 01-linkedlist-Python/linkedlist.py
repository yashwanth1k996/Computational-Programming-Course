"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        if(self.head is None):
            self.head = new_element
        else:
            new_element.next = self.head
            self.head = new_element
        pass
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        current_position = self.head
        count = 1
        while(current_position.next != None):
            if(position == count):
                return current_position
            count += 1
            current_position = current_position.next
        return None

    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        current_position = self.head
        count = 1
        while(current_position.next != None):
            if(position == count+1):
                new_element.next = current_position.next
                current_position.next = new_element
                break
            count += 1
            current_position = current_position.next
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        
        if(value == 1):
            self.head = self.head.next
        current_position = self.head
        while(current_position.next != None):
            if(current_position.next.value == value):
                current_position.next = current_position.next.next
                break
            current_position = current_position.next


e1 = Element(1)
e2 = Element(2)
e3 = Element(3)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)