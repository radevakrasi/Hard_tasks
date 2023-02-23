matrix_size = int(input())
car_number = input()
race_route = []
for i in range(matrix_size):
    race_route.append([x for x in input().split(" ")])

rows, cols = 0, 0

command = input()
distance = 0
success = False

while command != "End":

    if command == "left":
        cols -= 1
    elif command == "right":
        cols += 1
    elif command == "up":
        rows -= 1
    elif command == "down":
        rows += 1

    position = race_route[rows][cols]
    if position == "F":
        distance += 10
        success = True
        break
    elif position == "T":
        race_route[rows][cols] = "."
        for i, e in enumerate(race_route):
            for j, ee in enumerate(e):
                if 'T' in ee:
                    rows, cols = i, j
                    race_route[rows][cols] = '.'

        distance += 30

    else:
        distance += 10

    command = input()

race_route[rows][cols] = "C"

if success:
    print(f"Racing car {car_number} finished the stage!")
else:
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance} km.")
for b in race_route:
    print(''.join(b))

# for i, e in enumerate(race_route):
#     for j, ee in enumerate(e):
#         if 'T' in ee:
#             print(i, j)
