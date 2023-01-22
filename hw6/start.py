from logica import Casino
from decouple import config
MY_MONEY = 1000
while True:
    print('Ваш баланс ' + str(MY_MONEY))
    print('Запустит казино?(да или нет)')
    balans = input('')
    if balans == 'нет':
        print('Вы успешно вышли')
        break
    elif balans == 'да':
        chisla = int(input('Загадайте число от 1 до 30: '))
        stavka = int(input('Сколько хотите поставить?: '))
        MY_MONEY -= stavka
        MY_MONEY += Casino(chisla,stavka)

    else:
        print('Вы где то допустили ошибку')
