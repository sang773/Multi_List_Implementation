class SupplyNode:

    def __init__(self, snxt, pnxt, sown, pown, p):
        self.snext = snxt
        self.pnext = pnxt
        self.sowner = sown
        self.powner = pown
        self.price = p

    # Write getters and setters and __str__ method

    # Getters
    def get_snext(self):
        return self.snext

    def get_pnext(self):
        return self.pnext

    def get_sowner(self):
        return self.sowner

    def get_powner(self):
        return self.powner

    def get_price(self):
        return self.price

    # Setters
    def set_snext(self, snext):
        self.snext = snext

    def set_pnext(self, pnext):
        self.pnext = pnext

    def set_sowner(self, sowner):
        self.sowner = sowner

    def set_powner(self, powner):
        self.powner = powner

    def set_price(self, price):
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the SupplyNode object.
        """
        return f"({self.sowner.sno},{self.powner.pno},{self.price})"

