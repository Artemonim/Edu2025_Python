peoples_quanity = int(input())
k_factor = int(input())

peoples = [i for i in range(1, peoples_quanity + 1)]
index = 0

while len(peoples) > 1:
    index = (index + k_factor - 1) % len(peoples)
    peoples.pop(index)

print(peoples[0])

