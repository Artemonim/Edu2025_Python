a = float(input())
b = float(input())

thin = 18.5
bold = 25
IMT = a / (b * b)

if IMT < thin:
    print('Недостаточная масса')
elif IMT > bold:
    print('Избыточная масса')
else:
    print('Оптимальная масса')
    