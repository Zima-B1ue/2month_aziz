import random
import time
def Casino(win,lose):
    print("пожалуйста подождите")
    time.sleep(2)
    choise = random.randint(1,31)
    if choise == win:
        print(choise)
        print('Поздравляю вы выиграли!!')
        return lose * 2
    else:
        print(choise)
        print(f'вы проиграли:{lose}')
        print('попробуйте еще раз обязательно получться')
        return 0

