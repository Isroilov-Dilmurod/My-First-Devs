# Kun qandayligiga qarab ish qilish:

days = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma']
RelaxDays = ['shanba', 'yakshanba']
numbers = list(range(0, 101))

day = input('Bugun qanday kun?: ')
harorat = int(input('Havo harorati qanday?: '))

if day.lower() in days and harorat in numbers and harorat < 30:
    print('Bugun ish kuni, havo sovuq ekan, pechkani yoqing.')
elif day.lower() in days and harorat in numbers and harorat >= 30:
    print('Bugun ish kuni, havo issiq ekan, konditsionerni yoqing.')
elif day.lower() in RelaxDays and harorat in numbers and harorat >= 30:
    print('Bugun dam olish kuni! Havo issiq ekan, cho\'milgani ketdik!')
elif day.lower() in RelaxDays and harorat in numbers and harorat <= 30:
    print('Bugun dam olish kuni! Havo sovuq ekan, uyda dam olamiz!')
elif not day.lower() in days:
    print('Bunday hafta kuni yo\'q.')
if not harorat in numbers:
    print('Bunday harorat bo\'lishi mumkin emas, tekshirib qaytadan kiriting.')

