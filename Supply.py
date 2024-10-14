from SupplyNode import *
# Note: This is not a Class but just a set of functions related to Supply nodes

def find_supply(suppliers, parts, sno, pno):
    """
    Finds the supply node with the given sno and pno.
    Returns the SupplyNode object if found, None otherwise.
    """
    supplier_node = suppliers.find(sno)
    if supplier_node:
        current_supply = supplier_node.first_supply
        while current_supply:
            if current_supply.powner.pno == pno:
                return current_supply
            current_supply = current_supply.snext

    part_node = parts.find(pno)
    if part_node:
        current_supply = part_node.first_supply
        while current_supply:
            if current_supply.sowner.sno == sno:
                return current_supply
            current_supply = current_supply.pnext

    return None

def insert_supply(suppliers, parts, sno, pno, price):
    """
    Inserts a new supply node with the given sno, pno, and price.
    Returns True if insertion is successful, False otherwise.
    """
    if find_supply(suppliers, parts, sno, pno):
        return False

    supplier_node = suppliers.find(sno)
    part_node = parts.find(pno)

    if supplier_node and part_node:
        new_supply = SupplyNode(None, None, supplier_node, part_node, price)

        # Insert into supplier's supply list
        if supplier_node.first_supply is None:
            supplier_node.first_supply = new_supply
        else:
            current_supply = supplier_node.first_supply
            while current_supply.snext:
                current_supply = current_supply.snext
            current_supply.snext = new_supply

        # Insert into part's supply list
        if part_node.first_supply is None:
            part_node.first_supply = new_supply
        else:
            current_supply = part_node.first_supply
            while current_supply.pnext:
                current_supply = current_supply.pnext
            current_supply.pnext = new_supply

        supplier_node.num_supply += 1
        part_node.num_supply += 1
        return True

    return False

def delete_supply(suppliers, parts, sno, pno):
    """
    Deletes the supply node with the given sno and pno.
    Returns True if deletion is successful, False otherwise.
    """
    supply_node = find_supply(suppliers, parts, sno, pno)
    if not supply_node:
        return False

    supplier_node = supply_node.sowner
    part_node = supply_node.powner

    # Remove from supplier's supply list
    if supplier_node.first_supply == supply_node:
        supplier_node.first_supply = supply_node.snext
    else:
        current_supply = supplier_node.first_supply
        while current_supply.snext != supply_node:
            current_supply = current_supply.snext
        current_supply.snext = supply_node.snext

    # Remove from part's supply list
    if part_node.first_supply == supply_node:
        part_node.first_supply = supply_node.pnext
    else:
        current_supply = part_node.first_supply
        while current_supply.pnext != supply_node:
            current_supply = current_supply.pnext
        current_supply.pnext = supply_node.pnext

    supplier_node.num_supply -= 1
    part_node.num_supply -= 1
    return True

def update_supply(suppliers, parts, sno, pno, price):
    """
    Updates the price of the supply node with the given sno and pno.
    Returns True if update is successful, False otherwise.
    """
    supply_node = find_supply(suppliers, parts, sno, pno)
    if supply_node:
        supply_node.price = price
        return True
    return False

def print_suppliers_given_part(parts, pno):
    """
    Prints all suppliers for the given part number.
    """
    part_node = parts.find(pno)
    if part_node:
        current_supply = part_node.first_supply
        while current_supply:
            print(f"({current_supply.sowner.sno},{current_supply.sowner.sname},{current_supply.price})")
            current_supply = current_supply.pnext

def print_parts_given_supplier(suppliers, sno):
    """
    Prints all parts for the given supplier number.
    """
    supplier_node = suppliers.find(sno)
    if supplier_node:
        current_supply = supplier_node.first_supply
        while current_supply:
            print(f"({current_supply.powner.pno},{current_supply.powner.pname},{current_supply.price})")
            current_supply = current_supply.snext

def print_cheapest_suppliers_given_part(parts, pno):
    """
    Prints the cheapest suppliers for the given part number.
    """
    part_node = parts.find(pno)
    if part_node:
        cheapest_price = float('inf')
        cheapest_suppliers = []
        current_supply = part_node.first_supply
        while current_supply:
            if current_supply.price < cheapest_price:
                cheapest_price = current_supply.price
                cheapest_suppliers = [(current_supply.sowner.sno, current_supply.sowner.sname, current_supply.price)]
            elif current_supply.price == cheapest_price:
                cheapest_suppliers.append((current_supply.sowner.sno, current_supply.sowner.sname, current_supply.price))
            current_supply = current_supply.pnext

        print("\nCheapest suppliers:")
        for supplier in cheapest_suppliers:
            print(supplier)