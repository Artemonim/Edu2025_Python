"""https://stepik.org/course/58852 - course for beginners
https://stepik.org/lesson/284816/step/17
"""
total_minutes = int(input())

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} мин - это {hours} час {minutes} минут.")
