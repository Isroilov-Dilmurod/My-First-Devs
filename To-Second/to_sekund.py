print('Men sizga sutka, soat va daqiqalar necha sekundligini aniqlab beraman')

sutka1 = 86400 #sekund
hour1 = 3600 #sekund
minut1 = 60 #sekund

# write = int(input('Kerakligini tanlang: sutka uchun 1 ni, soat uchun 2 ni va daqiqa uchun 3 ni yozing: '))
# if write == 1:
#     a = int(input('Sutkani kiriting: '))
#     print(f"{a} sutka {a * sutka1} sekundga teng")
# elif write == 2:
#     b = int(input('Soatni kiriting: '))
#     print(f"{b} soat {b * hour1} sekundga teng")
# elif write == 3:
#     c = int(input('Daqiqani kiriting: '))
#     print(f"{c} daqiqa {c * minut1} sekundga teng")
# else:
#     print('Qaytadan RUN qilib, 1 yoki 2 yoki 3 sonlardan birini tanlang, keyin dastur ishlaydi!')
    

number = int(input('Sutkani kiriting: '))
number1 = int(input('Soatni kiriting: '))
number2 = int(input('Daqiqani kiriting: '))

abd = (number * sutka1) + (number1 * hour1) + (number2 * minut1)
print(abd)