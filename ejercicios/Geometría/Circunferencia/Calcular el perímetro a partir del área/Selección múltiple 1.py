{"cantidad_opciones":1, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
r = Racional(randrange(1, 54))
unidad_de_medida = choice(["mm", "cm", "m", "km"])

#================================Aquí va el enunciado================================================================
enunciado = f"El área de una circunferencia es " +Matematica(r**2*PI()+" "+potencia(unidad_de_medida,2, False), arreglar_espacios=True) +". El perímetro de dicha circunferencia es"

#================================Aquí se escriben los contenidos de las alternativas. Pon el correcto en el primero==
contenido_correcto = Matematica(2*r*PI()+" "+unidad_de_medida, arreglar_espacios=True)
contenido_2 = Matematica(r*PI()+" "+unidad_de_medida, arreglar_espacios=True)
contenido_3 = Matematica(r**2+" "+unidad_de_medida, arreglar_espacios=True)
contenido_4 = Matematica(r**2*PI()+" "+unidad_de_medida, arreglar_espacios=True)
contenido_5 = Matematica(r*potencia(PI(),2,False)+" "+unidad_de_medida, arreglar_espacios=True)

enunciado_oculto = r










