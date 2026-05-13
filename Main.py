sald = 1000

while True:
    print("===== MENÚ DEL CAJERO =====")
    print("1. Consultar saldo actual")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir del programa")

    if opc == "1":
        print("Tu saldo actual es: $", sald)

    elif opc == "2":
        dep = float(input("Cuanto deseas depositar? $"))
        if dep > 0:
            sald += dep
            print("Deposito exitoso. Nuevo saldo: $", sald)
        else:
            print("Ingresa un monto positivo para depositar.")

    elif opc == "3":
        ret = float(input("Cuanto deseas retirar? $"))
        if ret > 0 and ret <= sald:
            sald -= ret
            print("Retiro exitoso. Nuevo saldo: $", sald)
        elif ret > sald:
            print("No tienes suficiente saldo para ese retiro.")
        else:
            print("Ingresa un monto positivo para retirar.")

    elif opc == "4":
        print("Hasta luego!")
        break

    else:
        print("Opcion no valida.")    