"""https://stepik.org/course/58852
https://stepik.org/lesson/265079/step/11
"""
screen_price = int(input())
block_price = int(input())
keyboard_price = int(input())
mouse_price = int(input())
QUANITY_OF_COMPUTERS = 3

total_price = QUANITY_OF_COMPUTERS * (screen_price + block_price + keyboard_price + mouse_price)

print(total_price)
