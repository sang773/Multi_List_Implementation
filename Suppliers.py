from SupplierNode import *
from SupplyNode import *

class Suppliers:

    def __init__(self):
        self.head = SupplierNode("","",None,None)
        self.size = 0

    def __iter__(self):
            current_node = self.head.next
            while current_node:
                yield current_node
                current_node = current_node.next

    def find(self, sno):
        """
        Finds a supplier node with the given sno.
        Returns the SupplierNode object if found, None otherwise.
        """
        current_node = self.head.next
        while current_node:
            if current_node.sno == sno:
                return current_node
            current_node = current_node.next
        return None

    def insert(self, sno, sname):
        """
        Inserts a new supplier node with the given sno and sname.
        Returns True if insertion is successful, False otherwise.
        """
        if self.find(sno):
            return False

        new_node = SupplierNode(sno, sname, None, None)
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
        return True

    def delete(self, sno):
        """
        Deletes the supplier node with the given sno.
        Returns True if deletion is successful, False otherwise.
        """
        prev_node = self.head
        current_node = prev_node.next
        while current_node:
            if current_node.sno == sno:
                prev_node.next = current_node.next
                self.size -= 1
                return True
            prev_node = current_node
            current_node = current_node.next
        return False

    def update(self, sno, sname):
        """
        Updates the sname of the supplier node with the given sno.
        Returns True if update is successful, False otherwise.
        """
        node = self.find(sno)
        if node:
            node.sname = sname
            return True
        return False

    def __str__(self):
        """
        Returns a string representation of all supplier nodes.
        """
        output = ""
        for supplier in self:
            supply_str = ""
            current_supply = supplier.first_supply
            while current_supply:
                supply_str += f"({current_supply.powner.pno},{current_supply.price}) "
                current_supply = current_supply.snext
            output += f"{supplier} Supplies: {supply_str}\n"
        return output