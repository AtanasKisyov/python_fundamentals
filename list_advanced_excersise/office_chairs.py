rooms = int(input())
room_number = 0
free_chairs = 0
is_free = True
for i in range(rooms):
    room_number += 1
    office = input().split()
    chairs_on_hand, people = int(len(office[0])), int(office[1])
    if chairs_on_hand < people:
        is_free = False
        print(f'{people - chairs_on_hand} more chairs needed in room {room_number}')
    else:
        free_chairs += chairs_on_hand - people
if is_free:
    print(f'Game On, {free_chairs} free chairs left')
