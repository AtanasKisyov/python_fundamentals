HIGH_RANGE = range(81, 126)
MEDIUM_RANGE = range(51, 81)
LOW_RANGE = range(1, 51)
effort = 0
total_fire = 0
fire_list = input().split("#")
water_amount = int(input())
print("Cells:")
for fire in range(len(fire_list)):
    cell, fire_level = fire_list[fire].split(" = ")
    fire_level = int(fire_level)
    if cell == "High" and fire_level not in HIGH_RANGE:
        continue
    elif cell == "Medium" and fire_level not in MEDIUM_RANGE:
        continue
    elif cell == "Low" and fire_level not in LOW_RANGE:
        continue
    if fire_level <= water_amount:
        water_amount -= fire_level
        total_fire += fire_level
        effort += fire_level * 0.25
        print(f" - {fire_level}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
