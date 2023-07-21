def is_palind(isp):
    return isp.lower() == isp.lower()[::-1]

is_p = is_palind(input('Напишите текст для проверки на палиндром>> '))

if is_p == True:
    print('Это палиндром')

else:
    print('Это не палиндром')


