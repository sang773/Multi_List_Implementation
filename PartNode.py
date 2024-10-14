class PartNode:

    def __init__(self, no, name, nxt, supply):
        self.pno = no
        self.pname = name
        self.next = nxt
        self.first_supply = supply
        self.num_supply = 0

    # Write getters and setters and __str__ method

    # Getters
    def get_pno(self):
        return self.pno

    def get_pname(self):
        return self.pname

    def get_next(self):
        return self.next

    def get_first_supply(self):
        return self.first_supply

    def get_num_supply(self):
        return self.num_supply

    # Setters
    def set_pno(self, pno):
        self.pno = pno

    def set_pname(self, pname):
        self.pname = pname

    def set_next(self, next_node):
        self.next = next_node

    def set_first_supply(self, first_supply):
        self.first_supply = first_supply

    def set_num_supply(self, num_supply):
        self.num_supply = num_supply

    def __str__(self):
        """
        Returns a string representation of the PartNode object.
        """
        return f"({self.pno},{self.pname})"