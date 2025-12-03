
citta = input("inserisci il nome della citta\' d\' origine: ")

while not citta.isalpha():
    citta = input("inserisci il nome della citta\' d\' origine: ")

animal = input("inserisci il nome del tuo animale domestico: ")

while not animal.isalpha():
    animal = input("inserisci il nome del tuo animale domestico: ")

band = citta + ' ' + animal

print(f"il nome generato della band e\'{band}")