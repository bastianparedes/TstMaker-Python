{"cantidad_opciones":5, "cantidad_disponible":50}

if opcion==1:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    diccionario_tiempo_cantidad = {"mes":12, "bimestre":6, "trimestre":4, "cuatrimestre":3, "semestre":2}
    diccionario_agrupaciones = {"mes":"mensual", "bimestre":"bimestral", "trimestre":"trimestral", "cuatrimestre":"cuatrimestral", "semestre":"semestral"}
    tipo_de_agrupacion = choice(["mes", "bimestre", "trimestre", "cuatrimestre", "semestre"])
    cantidad_inicial = Racional(randrange(2,10))
    porcentaje = Racional(choice([5, 10, 20, 25, 40, 50, 75, 80]))
    tiempo_en_años = randrange(1, 5)

    n = tiempo_en_años*diccionario_tiempo_cantidad[tipo_de_agrupacion]

    cantidad_final = cantidad_inicial+por()+potencia(Racional(1+porcentaje/100,1,True),n)
    ganancia = Pol(cantidad_final,-cantidad_inicial)

    ganancia_simple = Racional(cantidad_inicial *  n  *  porcentaje/100, 1, True)
    cantidad_final_simple = Racional(cantidad_inicial + ganancia_simple, 1, True)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Una persona hace un depósito de {cantidad_inicial} millones de pesos en una cuenta de ahorro que genera ganancias con un interés compuesto del {porcentaje}\% {diccionario_agrupaciones[tipo_de_agrupacion]}. La cantidad de dinero que habrá en la cuenta al cabo de {tiempo_en_años} años es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(cantidad_final)   +" millones de pesos"
    contenido_2 =        Matematica(cantidad_final_simple)   +" millones de pesos"
    contenido_3 =        Matematica(ganancia)   +" millones de pesos"
    contenido_4 =        Matematica(ganancia_simple)   +" millones de pesos"
    contenido_5 =        Matematica(n)      +" millones de pesos"
    enunciado_oculto = [opcion, cantidad_inicial, porcentaje, tiempo_en_años]




elif opcion==2:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    diccionario_tiempo_cantidad = {"mes":12, "bimestre":6, "trimestre":4, "cuatrimestre":3, "semestre":2}
    diccionario_agrupaciones = {"mes":"mensual", "bimestre":"bimestral", "trimestre":"trimestral", "cuatrimestre":"cuatrimestral", "semestre":"semestral"}
    tipo_de_agrupacion = choice(["mes", "bimestre", "trimestre", "cuatrimestre", "semestre"])
    cantidad_inicial = Racional(randrange(2,10))
    porcentaje = Racional(choice([5, 10, 20, 25, 40, 50, 75, 80]))
    tiempo_en_años = randrange(1, 5)

    n = tiempo_en_años*diccionario_tiempo_cantidad[tipo_de_agrupacion]

    cantidad_final = cantidad_inicial+por()+potencia(Racional(1+porcentaje/100,1,True),n)
    ganancia = Pol(cantidad_final,-cantidad_inicial)

    ganancia_simple = Racional(cantidad_inicial *  n  *  porcentaje/100, 1, True)
    cantidad_final_simple = Racional(cantidad_inicial + ganancia_simple, 1, True)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Una persona hace un depósito de en una cuenta de ahorro que genera ganancias con un interés compuesto del {porcentaje}\% {diccionario_agrupaciones[tipo_de_agrupacion]}. Al cabo de {tiempo_en_años} años hay {Matematica(cantidad_final)} millones de pesos en la cuenta. La cantidad depositada fue de"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(cantidad_inicial)   +" millones de pesos"
    contenido_2 =        Matematica(cantidad_final_simple)   +" millones de pesos"
    contenido_3 =        Matematica(ganancia)   +" millones de pesos"
    contenido_4 =        Matematica(ganancia_simple)   +" millones de pesos"
    contenido_5 =        Matematica(n)      +" millones de pesos"
    enunciado_oculto = [opcion, cantidad_inicial, porcentaje, tiempo_en_años]




elif opcion==3:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    diccionario_tiempo_cantidad = {"mes":12, "bimestre":6, "trimestre":4, "cuatrimestre":3, "semestre":2}
    diccionario_agrupaciones = {"mes":"mensual", "bimestre":"bimestral", "trimestre":"trimestral", "cuatrimestre":"cuatrimestral", "semestre":"semestral"}
    tipo_de_agrupacion = choice(["mes", "bimestre", "trimestre", "cuatrimestre", "semestre"])
    cantidad_inicial = Racional(randrange(2,10))
    porcentaje = Racional(choice([5, 10, 20, 25, 40, 50, 75, 80]))
    tiempo_en_años = randrange(1, 5)

    n = tiempo_en_años*diccionario_tiempo_cantidad[tipo_de_agrupacion]

    cantidad_final = cantidad_inicial+por()+potencia(Racional(1+porcentaje/100,1,True),n)
    ganancia = Pol(cantidad_final,-cantidad_inicial)

    ganancia_simple = Racional(cantidad_inicial *  n  *  porcentaje/100, 1, True)
    cantidad_final_simple = Racional(cantidad_inicial + ganancia_simple, 1, True)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Una persona hace un depósito de {cantidad_inicial} millones de pesos en una cuenta de ahorro que genera ganancias con un interés compuesto del {porcentaje}\% {diccionario_agrupaciones[tipo_de_agrupacion]}. La ganancia que tendrá el depositante al cabo de {tiempo_en_años} años es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(ganancia)   +" millones de pesos"
    contenido_2 =        Matematica(cantidad_final_simple)   +" millones de pesos"
    contenido_3 =        Matematica(cantidad_final)   +" millones de pesos"
    contenido_4 =        Matematica(ganancia_simple)   +" millones de pesos"
    contenido_5 =        Matematica(n)      +" millones de pesos"
    enunciado_oculto = [opcion, cantidad_inicial, porcentaje, tiempo_en_años]




elif opcion==4:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    diccionario_tiempo_cantidad = {"mes":12, "bimestre":6, "trimestre":4, "cuatrimestre":3, "semestre":2}
    diccionario_agrupaciones = {"mes":"mensual", "bimestre":"bimestral", "trimestre":"trimestral", "cuatrimestre":"cuatrimestral", "semestre":"semestral"}
    tipo_de_agrupacion = choice(["mes", "bimestre", "trimestre", "cuatrimestre", "semestre"])
    cantidad_inicial = Racional(randrange(2,10))
    porcentaje = Racional(choice([5, 10, 20, 25, 40, 50, 75, 80]))
    tiempo_en_años = randrange(1, 5)

    n = tiempo_en_años*diccionario_tiempo_cantidad[tipo_de_agrupacion]

    cantidad_final = cantidad_inicial+por()+potencia(Racional(1+porcentaje/100,1,True),n)
    ganancia = Pol(cantidad_final,-cantidad_inicial)

    ganancia_simple = Racional(cantidad_inicial *  n  *  porcentaje/100, 1, True)
    cantidad_final_simple = Racional(cantidad_inicial + ganancia_simple, 1, True)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Una persona hace un depósito de {cantidad_inicial} millones de pesos en una cuenta de ahorro que genera ganancias con un interés compuesto del {porcentaje}\% {diccionario_agrupaciones[tipo_de_agrupacion]}. La cantidad de tiempo que tiene que pasar para que haya {Matematica(cantidad_final)} millones de pesos en la cuenta es"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(tiempo_en_años)   +" años"
    contenido_2 =        Matematica(n)   +" años"
    contenido_3 =        Matematica(cantidad_final)   +" años"
    contenido_4 =        Matematica(cantidad_final_simple)   +" años"
    contenido_5 =        Matematica(n+tiempo_en_años)   +" años"
    enunciado_oculto = [opcion, cantidad_inicial, porcentaje, tiempo_en_años]





elif opcion==5:
    #================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
    diccionario_tiempo_cantidad = {"mes":12, "bimestre":6, "trimestre":4, "cuatrimestre":3, "semestre":2}
    diccionario_agrupaciones = {"mes":"mensual", "bimestre":"bimestral", "trimestre":"trimestral", "cuatrimestre":"cuatrimestral", "semestre":"semestral"}
    tipo_de_agrupacion = choice(["mes", "bimestre", "trimestre", "cuatrimestre", "semestre"])
    cantidad_inicial = Racional(randrange(2,10))
    porcentaje = Racional(choice([5, 10, 20, 25, 40, 50, 75, 80]))
    tiempo_en_años = randrange(1, 5)

    n = tiempo_en_años*diccionario_tiempo_cantidad[tipo_de_agrupacion]

    cantidad_final = cantidad_inicial+por()+potencia(Racional(1+porcentaje/100,1,True),n)
    ganancia = Pol(cantidad_final,-cantidad_inicial)

    ganancia_simple = Racional(cantidad_inicial *  n  *  porcentaje/100, 1, True)
    cantidad_final_simple = Racional(cantidad_inicial + ganancia_simple, 1, True)
    #================================Aquí va el enunciado================================================================
    enunciado = fr"Una persona hace un depósito de {cantidad_inicial} millones de pesos en una cuenta de ahorro que genera ganancias con un interés compuesto {diccionario_agrupaciones[tipo_de_agrupacion]}. Al cabo de {tiempo_en_años} años hay {Matematica(cantidad_final)} millones de pesos en la cuenta. El porcentaje aplicado fue"

    #================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
    contenido_correcto = Matematica(porcentaje)   +r"\%"
    contenido_2 =        Matematica(Racional(porcentaje,100,True))   +r"\%"
    contenido_3 =        Matematica(n)   +r"\%"
    contenido_4 =        Matematica(Racional(n,100,True))   +r"\%"
    contenido_5 =        Matematica(ganancia_simple)   +r"\%"
    enunciado_oculto = [opcion, cantidad_inicial, porcentaje, tiempo_en_años]











