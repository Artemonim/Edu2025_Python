"""https://stepik.org/course/58852 - course for beginners
https://stepik.org/lesson/284816/step/15
"""
students = int(input())
quanitiy_of_tangerines = int(input())

tangerines_per_student = quanitiy_of_tangerines // students
tangerines_rest_in_basket = quanitiy_of_tangerines % students

print(tangerines_per_student, tangerines_rest_in_basket, sep='\n')
