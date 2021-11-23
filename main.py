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

def computerGuess():
    max = 1000
    min = 0
    number = random.randrange(min,max) #es el de la computadora
    bandera = False 
    
    while(bandera == False):
        print (number)
        print("Este es tu numero?")
        opc= input("Si | No:  ").lower()
        if( opc == "no"):
            print("Tu numero es mayor o menor al mio?")
            opc2 = input("Mayor | Menor: ").lower()
            if (opc2 == "menor"): #En caso que es menor
                max = number-1
                newNumber = random.randrange(min,max) 
                number = newNumber
            else: #En caso que es mayor
                min = number+1
                newNumber = random.randrange(min,max)
                number = newNumber
        else:
            bandera = True

    
computerGuess()