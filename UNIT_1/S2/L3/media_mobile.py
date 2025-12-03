serie = [2,4,6,8,10]
i = 1

while i <= 3:
    somma = sum(serie[0:i])/i
    print(f'la media dei primi {i} numeri e\': {somma}')
    i += 1

while i <= 5:
    somma = sum(serie[i-3:i])/3
    print(f'la media dei numeri dalla posizione {i-2} alla posizione {i} e\': {somma}')
    i += 1
