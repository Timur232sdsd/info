print('Изначальная сумма в тысячах: ')
summ = int(input())*1000
print('Ваш ежемесячный заработок в тысячах: ')
income = int(input()) 
print('Какой процент от общей суммы вы хотите откладывать: ')
procent_income = int(input())
print('Какой процент годовых от общей суммы вы планируете получать: ')
procent_summ = int(input())
print('Через сколько лет вы хотите видеть получившуюся сумму: ')
years = int(input())

i = income*120*procent_income
while years:
    summ = summ + summ/100*procent_summ + i
    years -= 1

a = list(str(round(summ)))
res = [ ''.join(a[::-1][i:i+3])[::-1] for i in range(0,len(a),3)]
print(' '.join(res[::-1]))

