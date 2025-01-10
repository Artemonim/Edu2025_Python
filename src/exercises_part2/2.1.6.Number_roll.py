number = int(input())
number_str = str(number)

if len(number_str) > 5:
    rolled_number = int(number_str[0] + number_str[5:0:-1])
else:
    rolled_number = int(number_str[::-1])

print(rolled_number)