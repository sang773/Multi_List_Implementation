class SupplierNode:

    def __init__(self, no, name, nxt, supply):
        self.sno = no
        self.sname = name
        self.next = nxt
        self.first_supply = supply
        self.num_supply = 0

    # Write setters and getters and __str__ methods

    # Getters
    def get_sno(self):
        return self.sno

    def get_sname(self):
        return self.sname

    def get_next(self):
        return self.next

    def get_first_supply(self):
        return self.first_supply

    def get_num_supply(self):
        return self.num_supply

    # Setters
    def set_sno(self, sno):
        self.sno = sno

    def set_sname(self, sname):
        self.sname = sname

    def set_next(self, next_node):
        self.next = next_node

    def set_first_supply(self, first_supply):
        self.first_supply = first_supply

    def set_num_supply(self, num_supply):
        self.num_supply = num_supply

    def __str__(self):
        """
        Returns a string representation of the SupplierNode object.
        """
        return f"({self.sno},{self.sname})"
