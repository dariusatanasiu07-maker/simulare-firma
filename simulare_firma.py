import random


def simuleaza_firma(incasari_clienti=100, cheltuieli=8000, luni=12):
    clienti_totali = 0
    venit_anual = 0
    profit_anual = 0
    luni_profit = 0
    luni_pierdere = 0
    luni_0 = 0
    max_clienti = 50
    min_clienti = 150
    luna_max = 0
    luna_min = 0

    for luna in range(luni):
        clienti = random.randint(50, 150)
        venit_lunar = incasari_clienti * clienti
        venit_anual += venit_lunar
        clienti_totali += clienti
        profit_lunar = venit_lunar - cheltuieli
        profit_anual += profit_lunar

        if venit_lunar > cheltuieli:
            luni_profit += 1
        elif venit_lunar == cheltuieli:
            luni_0 += 1
        else:
            luni_pierdere += 1

        if max_clienti <= clienti:
            max_clienti = clienti
            luna_max = luna + 1
        if min_clienti >= clienti:
            min_clienti = clienti
            luna_min = luna + 1

    return clienti, clienti_totali, venit_lunar, venit_anual, profit_lunar, profit_anual, luni_profit, luni_pierdere, luni_0, max_clienti, min_clienti, luna_max, luna_min


clienti, clienti_totali, venit_lunar, venit_anual, profit_lunar, profit_anual, luni_profit, luni_pierdere, luni_0, max_clienti, min_clienti, luna_max, luna_min = simuleaza_firma()

print('===== RAPORT ANUAL AL FIRMEI =====')
print(f'Clienti totali: {clienti_totali}')
print(f'Venit anual: {venit_anual} lei')
print(f'Profit anual: {profit_anual} lei')
print()
print(f'Luni pe profit: {luni_profit}')
print(f'Luni pe pierdere: {luni_pierdere}')
print(f'Luni pe zero: {luni_0}')
print()
print(f'Cea mai buna luna: luna {luna_max}, cu {max_clienti} clienti')
print(f'Cea mai slaba luna: luna {luna_min}, cu {min_clienti} clienti')
print()
print(f'Ultima luna: {clienti} clienti, venit {venit_lunar} lei, profit {profit_lunar} lei')

clienti, clienti_totali, venit_lunar, venit_anual, profit_lunar, profit_anual, luni_profit, luni_pierdere, luni_0, max_clienti, min_clienti, luna_max, luna_min = simuleaza_firma(25, 2500, 12)
print()
print('===== CAFENEA =====')
print(f'Clienti totali: {clienti_totali}')
print(f'Venit anual: {venit_anual} lei')
print(f'Profit anual: {profit_anual} lei')
print()
print(f'Luni pe profit: {luni_profit}')
print(f'Luni pe pierdere: {luni_pierdere}')
print(f'Luni pe zero: {luni_0}')
print()
print(f'Cea mai buna luna: luna {luna_max}, cu {max_clienti} clienti')
print(f'Cea mai slaba luna: luna {luna_min}, cu {min_clienti} clienti')
print()
print(f'Ultima luna: {clienti} clienti, venit {venit_lunar} lei, profit {profit_lunar} lei')

