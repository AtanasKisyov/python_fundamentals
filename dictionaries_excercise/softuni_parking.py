class Parking:

    def __init__(self, command, name, licence_plate=""):
        self.command = command
        self.name = name
        self.licence_plate = licence_plate

    def register(self, name, licence_plate):
        if self.name not in parking_lot:
            parking_lot[name] = licence_plate
            return print(f"{name} registered {licence_plate} successfully")
        else:
            return print(f"ERROR: already registered with plate number {licence_plate}")

    def unregister(self, name):
        if self.name not in parking_lot:
            return print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking_lot[name]


n = int(input())
parking_lot = {}
for i in range(n):
    data = input().split()
    if "register" in data:
        result = Parking(data[0], data[1], data[2])
        result.register(data[1], data[2])
    else:
        result = Parking(data[0], data[1])
        result.unregister(data[1])

for y in parking_lot:
    print(f"{y} => {parking_lot[y]}")
