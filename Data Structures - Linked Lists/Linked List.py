# 15 --> 6 --> 8

class Node():

  def __init__(self,data):
    self.data = data
    self.next = None
    
class LinkedList():

  def __init__(self):
    self.head = None
    self.tail = None
  
  def append(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
      self.tail = self.head
      self.length = 1
    else:
      self.tail.next = new_node
      self.tail = new_node 
      self.length += 1

  def prepend(self,data):
    new_node = Node(data)
    new_node.next = self.head 
    self.head = new_node
    

    self.length += 1

  def insert(self,index,data):
    new_node = Node(data)
    i = 0
    temp = self.head
    if index>=self.length:
      self.append(data)
      return 
    if index ==0:
      self.prepend(data)
      return
    while i<self.length:
      if i == index-1:
        temp.next , new_node.next = new_node , temp.next
        self.length+=1
        break
      temp = temp.next
      i+=1
    

  def remove(self,index):
    i =0
        currentNode = self.head
        if index ==0:
            self.head = currentNode.next 
            self.length -=1
        elif index<0:
            print("index cant be negative")
        else:
            if index < (self.length):
                while i<(index):
                    prevNode = currentNode
                    currentNode = currentNode.next
                    nextNode = currentNode.next
                    i+=1
                if index != (self.length-1):
                    prevNode.next = nextNode
                    self.length -=1
                else:
                    prevNode.next = None
                    self.tail = prevNode
                    self.length -=1
            else:
                print("no element at index")
    
  def printl(self):
    temp = self.head
    while temp != None:
      print(temp.data , end = ' ')
      temp = temp.next
    print()
    print('Length = '+str(self.length))

  def reverse(self):
    prev = None
    self.tail = self.head 
    while self.head != None:
      temp = self.head
      self.head = self.head.next
      temp.next = prev
      prev = temp  
    self.head = temp
    

l = LinkedList()
l.append(10)
l.append(5)
l.append(6)
l.prepend(1)
l.insert(2,99)
l.insert(34,23)
l.remove(5)
l.reverse()
l.printl()
print(l.head.data, l.tail.data)
