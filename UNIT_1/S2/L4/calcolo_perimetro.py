import math

print("In questo programma puoi calcolare il perimetro di 3 figure\n\nPremi 1 per quadrato\nPremi 2 per cerchio\nPremi 3 per rettangolo ")

while True:
    risp = input("\nscelta: ")

    if risp == '1':
        lato = input("qual'e' la misura del lato del quadrato?: ")
        perim = int(lato) * 4

        print(f"il perimetro del quadrato e': {perim}")
        break
    elif risp == '2':
        r = input("qual'e' la misura del raggio del cerchio?: ")

        circ =  math.pi * 2 * int(r)
        print(f"La circonferenza del cerchio in questione e': {circ:.2f}")
        break
    elif risp == '3':
        b = input("dammi la base del rettangolo: ")
        h = input("dammi l'altezza del rettangolo: ")

        perim = int(b) * 2 + int(h) * 2
        print(f"il perimetro del rettangolo e': {perim}")
        break
    else:
        print("devi inserire un numero di quelli presenti nell'elenco")
 
