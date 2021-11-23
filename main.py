import random
def humanguess():
    number=random.randrange(0,10)
    print(number)

    numero=-1

    while numero!=number:

        numero=int(input("Introduce un numero"))

        if number==numero:
            print(f"Felicidades ganaste {numero}")
        elif numero>number:
            print(f"El numero que escogio es mayor {numero}")
        else:
            print(f"El numero que escogio es menor {numero}")

humanguess()