
def napihomerseklet():
    homerseklet = [0,12,13,9,2,7]
    i = 0
    kisebb = 0
    while (i< len(homerseklet)-1):
        kisebb = homerseklet[i +1]
        if ((homerseklet[i]- kisebb) > 3):
            print(f'október {i+2}. -án 3 foknál nagyobbat csökkent a hőmérséklet')
        i +=1
napihomerseklet()