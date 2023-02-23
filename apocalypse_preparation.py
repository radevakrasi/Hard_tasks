from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]
created_items = {}

healing_items = [
    ("Patch", 30),
    ("Bandage", 40),
    ("MedKit", 100)
]

while textiles and medicaments:
    new_item = False
    curr_textile = textiles.popleft()
    curr_medicament = medicaments.pop()
    summ = curr_medicament + curr_textile

    for item, cost in healing_items:
        if cost == summ:
            if item not in created_items.keys():
                created_items[item] = 0
            created_items[item] += 1
            new_item = True
            break
    if new_item:
        continue
    if summ > healing_items[2][1]:
        if "MedKit" not in created_items.keys():
            created_items["MedKit"] = 0
        created_items["MedKit"] += 1
        last_element = medicaments.pop()
        add_summ = summ - 100
        medicaments.append(last_element + add_summ)
    elif not new_item:
        medicaments.append(curr_medicament + 10)

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
elif not textiles:
    print("Textiles are empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-(x[1]), x[0]))

for item, amount in sorted_items:
    print(f"{item} - {amount}")

if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments])}")

if textiles:

    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
