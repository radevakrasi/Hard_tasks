# n, m = [int(x) for x in input().split()]
# playground = []
# my_row, my_col = 0, 0
#
# for line in range(n):
#     playground.append([x for x in input().split()])
#
# # for i, e in enumerate(playground):
# #     for j, ee in enumerate(e):
# #         if 'B' in ee:
# #             my_row, my_col = i, j
#
# for i in range(n):
#     for j in range(m):
#         if playground[i][j] == 'B':
#             my_row, my_col = i, j
#
# cached_players = 0
# moves = 0
#
# while True:
#     command = input()
#     if command == "Finish":
#         break
#     s_row, s_col = my_row, my_col
#     if command == "up":
#         s_row -= 1
#     elif command == "down":
#         s_row += 1
#     elif command == "right":
#         s_col += 1
#     elif command == "left":
#         s_col -= 1
#
#     if s_row >= n or s_row < 0 or s_col >= m or s_col < 0:
#         continue
#     if playground[s_row][s_col] == "O":
#         continue
#
#     if playground[s_row][s_col] == "-":
#         my_row, my_col = s_row, s_col
#         moves += 1
#     elif playground[s_row][s_col] == "P":
#         moves += 1
#         cached_players += 1
#         my_row, my_col = s_row, s_col
#         playground[s_row][s_col] = "-"
#         if cached_players == 3:
#             break
#
#
#
# print("Game over!")
# print(f"Touched opponents: {cached_players} Moves made: {moves}")


rows, cols = map(int, input().split())

playground = []
for i in range(rows):
    row = input().split()
    playground.append(row)

print(playground[10][10])

row_my, col_my = 0, 0
row_p, col_p = [], []
for i in range(rows):
    for j in range(cols):
        if playground[i][j] == 'B':
            row_my, col_my = i, j
        elif playground[i][j] == 'P':
            row_p.append(i)
            col_p.append(j)

moves = 0
the_touched_opponents = 0
while True:
    direction = input()
    if direction == "Finish":
        break

    new_row_b, new_col_b = row_my, col_my

    if direction == "up":
        new_row_b -= 1
    elif direction == "down":
        new_row_b += 1
    elif direction == "right":
        new_col_b += 1
    elif direction == "left":
        new_col_b -= 1

    if new_row_b < 0 or new_row_b >= rows or new_col_b < 0 or new_col_b >= cols:
        continue

    if playground[new_row_b][new_col_b] == "O":
        continue

    if playground[new_row_b][new_col_b] == "P":
        the_touched_opponents += 1
        playground[new_row_b][new_col_b] = "-"
        row_p.remove(new_row_b)
        col_p.remove(new_col_b)

    row_my, col_my = new_row_b, new_col_b
    moves += 1

    if the_touched_opponents == 3:
        break

print("Game over!")
print(f"Touched opponents: {the_touched_opponents} Moves made: {moves}")