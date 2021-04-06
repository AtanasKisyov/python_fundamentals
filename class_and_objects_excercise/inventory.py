class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.items = []
        self.used_capacity = 0

    def add_item(self, item):

        if self.used_capacity < self.__capacity:
            self.used_capacity += 1
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.__capacity - self.used_capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
