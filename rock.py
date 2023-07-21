def is_pal(isp):
    return isp.lower() == isp.lower()[::-1]
is_p = is_pal(input('Напишите текст для проверки:'))
if is_p == True:
    print('Палиндром')
else:
    print('Не палиндром')


