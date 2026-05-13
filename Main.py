sald = 1000
opciones = ["1. Consultar saldo actual", "2. Depositar dinero", "3. Retirar dinero", "4. Salir del programa"]



while True:
    print("===== MENÚ DEL CAJERO =====")
    for op in opciones:
        print(op)

    opc = input("\nElige una opcion (1-4): ")

    if opc == "1":
        print("Tu saldo actual es: $", sald)

    elif opc == "2":
        dep = float(input("Cuanto deseas depositar? $"))
        if dep > 0:
            sald = sald + dep
        print("Deposito exitoso. Nuevo saldo: $", sald)

    elif opc == "3":
        ret = float(input("Cuanto deseas retirar? $"))
        if ret > 0 and ret <= sald:
            sald = sald - ret
            print("Retiro exitoso. Nuevo saldo: $", sald)
        elif ret > sald:
            print("No tienes suficiente saldo para ese retiro.")
        else:
            print("Ingresa un monto positivo para retirar.")

    elif opc == "4":
        print("\n--- Opciones disponibles ---")
        for op in opciones:
            print("-", op)
        print("Hasta luego!")
        break

    else:
        print("Opcion no valida.")