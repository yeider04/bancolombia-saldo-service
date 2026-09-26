# saldo.py

def consultar_saldo(numero_cuenta):
    # Simulacion de logica de negocio
    if not numero_cuenta or len(numero_cuenta) != 10:
        raise ValueError("Numero de cuenta invalido")
    
    if numero_cuenta == "1234567890":
        return 2000.00
    else:
        return 0.00

if __name__ == "__main__":
    saldo = consultar_saldo("1234567890")
    print(f"Su saldo actual es: ${saldo}")