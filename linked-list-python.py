class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

  def printNode(self):
    print(self.value, end=" -> None")

class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

  def insertValue(self, value):
    while self.next:
      self = self.next
    self.next = Node(value)

  def printList(self):
    while self:
      print(self.value, end=" -> ")
      self = self.next
    print("None")

myList = LinkedList(5)
myList.insertValue(7)
myList.insertValue(9)
myList.insertValue(11)
myList.printList()
