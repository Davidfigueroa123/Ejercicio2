saldo = 1000

while True:
    print("===== MENÚ DEL CAJERO =====")
    print("1. Consultar saldo actual")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa")

    opc = input("\nElige una opcion (1-4): ")

    if opc == "4":
        print("Hasta luego!")
        break