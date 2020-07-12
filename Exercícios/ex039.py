# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar
# -Se é a hora de se alistar
# -Se já passou do tempo do alistameto
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
birth = int(input('Informe seu ano de nascimento: '))
age = date.today().year - birth
dage = abs(18 - age)

a = 'ano' if dage == 1 else 'anos'
f = 'falta' if dage == 1 else 'faltam'

if age > 18:
    print('Você passou {} {} do tempo de se alistar.'.format(dage, a))
elif age < 18:
    print('Ainda {} {} {} para você se alistar.'.format(f, dage, a))
else:
    print('Você está na idade para se alistar')

