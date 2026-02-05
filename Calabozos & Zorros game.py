llaves = 0
vida = 100
llave_room_1 = False
cofre_room_2 = False
llave_escaleras = False
antorcha_grande = False
llave_pasillo_curveado = False
llave_UG_room_3 = False
llave_princesa = False
zombie_derrotado = False
print("------------------------------")
print("------------------------------")
print("Bienvenido a Calabozos & Zorros!")
print("------------------------------")
print("------------------------------")
print()
print("------------------------------")
input("(presione enter para iniciar)")
print("------------------------------")
print()
print("------------------------------")
print("eres un caballero zorro enviado por el rey de los zorros para salvar a Alice, la princesa zorro, que fue secuestrada por los gatos y la encerraron en un calabozo")
print("------------------------------")
print("")

def incio():
    print()
    print("------------------------------")
    print("te encuentras en un pasillo con dos caminos, uno a la derecha y otro adelante")
    print("------------------------------")
    eleccion = input("a donde vas? (derecha/adelante): ").lower()
    if eleccion == "derecha":
        room_1()
    elif eleccion == "adelante":
        room_2()
    else:
        print("opción no válida, intenta de nuevo.")
        incio()

def room_1():
    global llave_room_1, llaves
    print()
    if not llave_room_1:
        print("------------------------------")
        print("entras a un pasillo largo y curveado, hay una habitación oscura al final, a la izquierda logras ver el reflejo de una llave")
        print("------------------------------")
        eleccion = input("tomas la llave, que harás? (cuarto oscuro/inicio): ").lower()
        llave_room_1 = True
        llaves += 1
    else:
        print("------------------------------")
        print("entras a un pasillo largo y curveado, hay una habitación oscura al final")
        print("------------------------------")
        eleccion = input("que harás? (cuarto oscuro/inicio): ").lower()

    if eleccion == "cuarto oscuro":
        cuarto_oscuro()
    elif eleccion == "inicio":
        incio()
    else:
        print("opción no válida, intenta de nuevo.")
        room_1()

def room_2():
    global vida, cofre_room_2
    print()
    if not cofre_room_2:
        print("------------------------------")
        print("entras a una habitación con un cofre en el centro, hay una puerta hacia la izquierda")
        print("------------------------------")
        eleccion = input("que harás? (abrir cofre/izquierda/inicio): ").lower()
        if eleccion == "abrir cofre":
            print("encuentras un slime que se comió un pan duro que estaba en el cofre, el slime te ataca y lo cierras, pierdes 10 de vida")
            vida -= 10
            cofre_room_2 = True
            room_2()
        elif eleccion == "izquierda":
            room_3()
        elif eleccion == "inicio":
            incio()
        else:
            print("opción no válida, intenta de nuevo.")
            room_2()
    else:
        print("------------------------------")
        print("entras en una habitación vacía con un cofre con un slime agresivo al centro y una puerta a la izquierda")
        print("------------------------------")
        eleccion = input("que harás? (izquierda/inicio): ").lower()
        if eleccion == "izquierda":
            room_3()
        elif eleccion == "inicio":
            incio()
        else:
            print("opción no válida, intenta de nuevo.")
            room_2()

def cuarto_oscuro():
    print()
    print("------------------------------")
    print("entras en la habitación oscura, tomas tu antorcha y encuentras un esqueleto sentado en un trono y sosteniendo un bastón")
    print("------------------------------")
    eleccion = input("que harás? (bastón/volver): ").lower()
    if eleccion == "bastón":
        print("al tomar el bastón, el esqueleto se mueve y te dice 'todo aquel que toque este bastón quedará maldito por siempre'")
        print("quedas maldito, no puedes moverte, el esqueleto se desvanece y tomas su lugar")
        print("GAME OVER")
        game_over()
    elif eleccion == "volver":
        room_1()
    else:
        print("opción no válida, intenta de nuevo.")
        cuarto_oscuro()

def room_3():
    global llaves, llave_escaleras
    print()
    if not llave_escaleras:
        print("------------------------------")
        print("entras por la puerta pero encuentras unas escaleras, al bajar, encuentras una puerta doble cerrada con llave")
        print("------------------------------")
        if llaves > 0:
            eleccion = input("usas la llave para abrir la puerta? (si/no): ").lower()
            if eleccion == "si":
                llave_escaleras = True
                llaves -= 1
                room_UG_1()
            elif eleccion == "no":
                room_2()
            else:
                print("opción no válida, intenta de nuevo.")
                room_3()
        else:
            print("------------------------------")
            print("no tienes ninguna llave, vuelves por tu camino")
            print("------------------------------")
            room_2()
    else:
        print("estás en las escaleras")
        eleccion = input("que harás? (subir/bajar): ").lower()
        if eleccion == "subir":
            room_2()
        elif eleccion == "bajar":
            room_UG_1()

def room_UG_1():
    print()
    print("------------------------------")
    print("bajas las escaleras, puedes continuar por un pasillo oscuro o volver")
    print("------------------------------")
    eleccion = input("que harás? (pasillo/escaleras): ").lower()
    if eleccion == "pasillo":
        UG_pasillo()
    elif eleccion == "escaleras":
        room_3()
    else:
        print("opción no válida, intenta de nuevo.")
        room_UG_1()

def UG_pasillo():
    global llave_princesa, llaves, antorcha_grande, llave_pasillo_curveado
    print()
    if not antorcha_grande:
        print("------------------------------")
        print("caminas por el pasillo, está demasiado oscuro pero logras ver una puerta al final")
        print("------------------------------")
        eleccion = input("que harás? (escaleras/puerta): ").lower()
        if eleccion == "escaleras":
            room_UG_1()
        elif eleccion == "puerta":
            UG_room_2()
    else:
        if not llave_pasillo_curveado:
            print("------------------------------")
            print("enciendes tu antorcha grande y encuentras una llave de oro, tiene un corazón de cristal en el centro")
            print("------------------------------")
            llave_pasillo_curveado = True
            llave_princesa = True
            llaves += 1
        eleccion = input("que harás? (escaleras/puerta): ").lower()
        if eleccion == "escaleras":
            room_UG_1()
        elif eleccion == "puerta":
            UG_room_2()

def UG_room_2():
    print()
    print("entras a una habitación vacía, hay una puerta a la derecha y otra al frente")
    eleccion = input("que harás? (derecha/frente/pasillo): ").lower()
    if eleccion == "derecha":
        UG_room_3()
    elif eleccion == "frente":
        UG_room_4()
    elif eleccion == "pasillo":
        UG_pasillo()
    else:
        print("opción no válida, intenta de nuevo.")
        UG_room_2()

def UG_room_3():
    global llaves, llave_UG_room_3
    print()
    if not llave_UG_room_3:
        print("------------------------------")
        print("entras en una habitación con una puerta cerrada con llave a la izquierda")
        print("------------------------------")
        if llaves > 0:
            eleccion = input("usas una llave para abrir la puerta? (si/no/pasillo): ").lower()
            if eleccion == "si":
                llave_UG_room_3 = True
                llaves -= 1
                UG_room_3_1()
            elif eleccion == "no":
                UG_room_3_1()
            elif eleccion == "pasillo":
                UG_room_2()
            else:
                print("opción no válida, intenta de nuevo.")
                UG_room_3()
        else:
            print("------------------------------")
            print("no tienes ninguna llave, vuelves al pasillo")
            print("------------------------------")
            UG_room_2()
    else:
        eleccion = input("que harás? (entrar/pasillo): ").lower()
        if eleccion == "entrar":
            UG_room_3_1()
        elif eleccion == "pasillo":
            UG_room_2()

def UG_room_3_1():
    global antorcha_grande
    print()
    if not antorcha_grande:
        print("------------------------------")
        print("entras en una habitación con un cofre en el medio")
        print("------------------------------")
        eleccion = input("que harás? (abrir cofre/volver): ").lower()
        if eleccion == "abrir cofre":
            print("obtienes una antorcha grande")
            antorcha_grande = True
            UG_room_3_1()
        elif eleccion == "volver":
            UG_room_3()
        else:
            print("opción no válida.")
            UG_room_3_1()
    else:
        print("------------------------------")
        print("entras en una habitación con un cofre vacío")
        print("------------------------------")
        eleccion = input("que harás? (volver): ").lower()
        if eleccion == "volver":
            UG_room_3()

def UG_room_4():
    print()
    print("------------------------------")
    print("estás en una sala de estar con puertas en todas direcciones")
    print("------------------------------")
    eleccion = input("que harás? (izquierda/derecha/frente/atrás): ").lower()
    if eleccion == "izquierda":
        UG_room_5()
    elif eleccion == "derecha":
        UG_room_6()
    elif eleccion == "frente":
        UG_room_7()
    elif eleccion == "atrás":
        UG_room_2()
    else:
        print("opción no válida.")
        UG_room_4()

def UG_room_5():
    global zombie_derrotado, llaves
    print()
    if not zombie_derrotado:
        print("------------------------------")
        print("entras en una habitación con un zombie! tiene un llave en las manos")
        print("------------------------------")
        eleccion = input("que harás? (atacar/huir): ").lower()
        if eleccion == "atacar":
            print("derrotas al zombie y obtienes la llave que llevaba")
            zombie_derrotado = True
            llaves += 1
            UG_room_5()
        elif eleccion == "huir":
            UG_room_4()
        else:
            print("opción no válida.")
            UG_room_5()
    else:
        print("------------------------------")
        print("estás en la habitación del zombie, este yace derrotado en el suelo")
        print("------------------------------")
        eleccion = input("que harás? (volver): ").lower()
        if eleccion == "volver":
            UG_room_4()

def UG_room_6():
    print()
    print("------------------------------")
    print("entras en una especie de baño, está completamente sucio, pero en el medio, ves un cofre de plata con bordes de oro")
    print("------------------------------")
    elección = input("que harás? (cofre/volver)")
    if elección.lower() == "cofre":
        print("abres el cofre, resultó ser un mímico, este te ataca y te acaba")
        print("GAME OVER")
        game_over()
    elif elección.lower() == "volver":
        UG_room_4()
    else:
        print("elección no válida, intentalo de nuevo")
        UG_room_6()

def UG_room_7():
    global antorcha_grande
    print()
    if antorcha_grande == False:
        print("------------------------------")
        print("entras en un pasillo, está completamente oscuro, no puedes ver nada, no puedes avanzar")
        print("------------------------------")
        elección = input("que harás? (volver): ")
        if elección.lower() == "volver":
            UG_room_4()
        else:
            print("elección no válida, intentalo de nuevo")
            UG_room_7()
    elif antorcha_grande == True:
        print("------------------------------")
        print("entras a un pasillo oscuro, enciendes tu antorcha grande y puedes ver claramente, al final del pasillo hay una puerta de madera")
        print("------------------------------")
        elección = input("que harás? (puerta/volver): ")
        if elección.lower() == "puerta":
            UG_room_8()
        elif elección.lower() == "volver":
            UG_room_4()
        else:
            print("elección no válida, intentalo de nuevo")
            UG_room_7()

def UG_room_8():
    global llave_princesa
    print()
    if llave_princesa == False:
        print("------------------------------")
        print("entás en una habitación completamente vacía, al frente ves una puerta de plata con bordes dorados, está cerrada con llave, la cerradura es de oro, entre tus llaves ninguna sirve")
        print("------------------------------")
        elección = input("que harás? (volver): ")
        if elección.lower() == "volver":
            UG_room_7()
        else:
            print("elección no válida, intentalo de nuevo")
            UG_room_8()
    elif llave_princesa == True:
        print("------------------------------")
        print("estás en una habitación completamente vacía, al frente ves una puerta de plata con bordes dorados, está cerrada con llave, la cerradura es de oro, entre tus llaves ves una de oro")
        print("------------------------------")
        elección = input("que harás? (puerta/volver): ")
        if elección.lower() == "puerta":
            sala_princesa()
        elif elección.lower() == "volver":
            UG_room_7()
        else:
            print("elección no válida, intentalo de nuevo")
            UG_room_8()

def sala_princesa():
    print()
    print("------------------------------")
    print("------------------------------")
    print("usas la llave de oro para abrir la puerta, adentro ves a la princesa Alice, está atada y amordazada")
    print("la liberas y ella te agradece mucho por salvarla")
    print("------------------------------")
    print("------------------------------")
    print()
    print("------------------------------")
    print("FELICIDADES! HAS COMPLETADO EL JUEGO!")
    print("------------------------------")
    game_over()


def game_over():
    print()
    print("------------------------------")
    input("Presiona Enter para salir")
    print("------------------------------")
    exit()

incio()