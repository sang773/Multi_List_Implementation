from PartNode import *
from SupplyNode import *

class Parts:

    def __init__(self):
        self.head = PartNode("","",None,None)
        self.size = 0
    
    def __iter__(self):
        current_node = self.head.next
        while current_node:
            yield current_node
            current_node = current_node.next

    def find(self,pno):
        """
        Finds a part node with the given pno.
        Returns the PartNode object if found, None otherwise.
        """
        current_node = self.head.next
        while current_node:
            if current_node.pno == pno:
                return current_node
            current_node = current_node.next
        return None

    def insert(self,pno,pname):
        """
        Inserts a new part node with the given pno and pname.
        Returns True if insertion is successful, False otherwise.
        """
        if self.find(pno):
            return False

        new_node = PartNode(pno, pname, None, None)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
        return True

    def delete(self,pno):
        """
        Deletes the part node with the given pno.
        Returns True if deletion is successful, False otherwise.
        """
        prev_node = self.head
        current_node = prev_node.next
        while current_node:
            if current_node.pno == pno:
                prev_node.next = current_node.next
                self.size -= 1
                return True
            prev_node = current_node
            current_node = current_node.next
        return False

    def update(self,pno,pname):
        """
        Updates the pname of the part node with the given pno.
        Returns True if update is successful, False otherwise.
        """
        node = self.find(pno)
        if node:
            node.pname = pname
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of all part nodes.
        """
        output = ""
        for part in self:
            supply_str = ""
            current_supply = part.first_supply
            while current_supply:
                supply_str += f"({current_supply.sowner.sno},{current_supply.price}) "
                current_supply = current_supply.pnext
            output += f"({part.pno},{part.pname}) Supplied by: {supply_str}\n"
        return output