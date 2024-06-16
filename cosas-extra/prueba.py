def juego_lagartija(juego, jugadores):
    # Escribe tu código aquí!
    pasos_totales = juego[0]
    indicaciones = juego[1]
    # Creamos una copia de jugadores
    jugadores_copia = jugadores[::1]
    pasos_jugadores = [0] * len(jugadores)
    # Lista que contiene a los jugadores que llegaron a la meta
    sobrevivientes = []
    turnos_sobrevivientes = []

    # La lista indiciaciones tiene el mismo largo
    # que la lista de pasos de un jugador por turno

    for i in range(len(indicaciones)):
        for j in range(len(jugadores)):
            jugador_actual = jugadores[j][0]
            pasos_jugador_actual = jugadores[j][1][i]
            if indicaciones[i] == "luz roja":
                if pasos_jugador_actual > 0 and not (jugador_actual in sobrevivientes):
                    jugadores_copia[j] = ""
            else:
                '''
                Si un jugador no esta eliminado y no ha llegado a la meta
                sumamos los pasos que dio en luz verde,
                si el jugador llega a la meta lo
                guardamos una lista de sobrevivientes
                y el turno en el que llego a la meta
                en una lista de turnos_sobrevivientes
                '''
                if jugadores_copia[j] != "" and not (jugador_actual in sobrevivientes):
                    pasos_jugadores[j] += pasos_jugador_actual
                    if pasos_jugadores[j] >= pasos_totales:
                        sobrevivientes.append(jugador_actual)
                        turnos_sobrevivientes.append(i+1)

    for i in range(len(sobrevivientes)):
        # turno en el que el sobreviviente llego a la meta
        turno_actual = turnos_sobrevivientes[i]
        if i == 0:
            turno_maximo = turno_actual
        elif turno_actual <= turno_maximo:
            turno_maximo = turno_actual

    ganadores = []
    for i in range(len(sobrevivientes)):
        if turnos_sobrevivientes[i] == turno_maximo:
            ganadores.append(sobrevivientes[i])

    for i in range(len(sobrevivientes)):
        sobrevivientes[i] = sobrevivientes[i]

    return [sobrevivientes, ganadores]


juego = [12, ['luz verde', 'luz roja', 'luz verde',
              'luz verde', 'luz verde', 'luz verde']]
jugadores = [['Pamela Ferguson', [3, 0, 1, 1, 4, 3]], ['Theresa Chaney', [3, 0, 0, 2, 2, 0]], [
    'Mrs. Cynthia Reynolds MD', [4, 2, 0, 0, 4, 1]], ['Danny Bray', [4, 0, 1, 4, 4, 2]], ['Jesus Barker', [2, 0, 1, 2, 0, 4]]]
resultado = juego_lagartija(juego, jugadores)
print(resultado)
print("Los jugadores que pasaron la meta son: ", sorted(resultado[0]))
print("Los jugadores que ganaron son: ", sorted(resultado[1]))
