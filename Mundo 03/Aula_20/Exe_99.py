from random import randint
def contador(*num):
    print('\n>>>ANALISADOR DE NÚMEROS<<<')
    print(f'{num} ao todo foram {len(num)} números e o maior foi {max(num)}')
    print('-=' * 30)


contador(randint(0, 10,), randint(0, 10,), randint(0, 10,), randint(0, 10,), randint(0, 10,))
contador(randint(0, 10,),randint(0, 10,),randint(0, 10,))
contador(randint(0, 10,),randint(0, 10,))