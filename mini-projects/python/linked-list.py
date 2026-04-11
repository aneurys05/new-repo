


class Nodes:
      
      def __init__(self, value, next=None):
          self.value = value
          self.next = next

      def __str__(self):
          return self.value
      
      @classmethod
      def display_nodes(cls):
          node = node1
          while node:
                print(node.value)
                node = node.next

      @classmethod
      def contains_node(cls, element):
          node = node1
          while node:
                if node.value == element.upper():
                   return f"Linked list contains {element}"
                else:
                     node = node.next
          
          return f"Linked list does not contain {element}"
        

        
node1 = Nodes("A")
node2 = Nodes("B")
node3 = Nodes("C")
node4 = Nodes("D")
node5 = Nodes("E")
node6 = Nodes("F")

node1.next = node2
node2.next = node3 
node3.next = node4
node4.next = node5
node5.next = node6

