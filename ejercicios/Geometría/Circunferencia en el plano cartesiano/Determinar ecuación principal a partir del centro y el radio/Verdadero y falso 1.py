{"cantidad_opciones":2, "cantidad_disponible":50}

#================================Aquí se escriben los números utilizados. Utilizar minúsculas para las letras========
h, k, r = choice([-1,1])*Racional(randrange(1, 7)), choice([-1,1])*Racional(randrange(1, 7)), Racional(randrange(1, 7))

if opcion==1:
    #================================Aquí va el enunciado================================================================
    enunciado_verdadero = f"Sea la circunferencia C cuyo centro es el punto {Matematica(Par(h,k))} y cuyo diámetro mide {2*r} unidades. La ecuación principal de C es "+Matematica(potencia(Pol("x",-h),2)+"+"+potencia(Pol("y",-k),2)+"="+r**2)+"."
    enunciado_falso = f"Sea la circunferencia C cuyo centro es el punto {Matematica(Par(h,k))} y cuyo diámetro mide {2*r} unidades. La ecuación principal de C es "+choice([
        Matematica(potencia(Pol("x",choice([-h,h])),2)+"+"+potencia(Pol("y",choice([-k,k])),2)+"="+choice([r, r**2, 2*r, (2*r)**2, Root(r), Root(2*r)])),
        Matematica("("+Pol("x",choice([-h,h]))+")+("+Pol("y",choice([-k,k]))+")="+choice([r, r**2, 2*r, (2*r)**2, Root(r), Root(2*r)]))
    ])+"."
elif opcion==2:
    enunciado_verdadero = f"Sea la circunferencia C cuyo centro es el punto {Matematica(Par(h,k))} y cuyo radio mide {r} unidades. La ecuación principal de C es "+Matematica(potencia(Pol("x",-h),2)+"+"+potencia(Pol("y",-k),2)+"="+r**2)+"."
    enunciado_falso = f"Sea la circunferencia C cuyo centro es el punto {Matematica(Par(h,k))} y cuyo radio mide {r} unidades. La ecuación principal de C es "+choice([
        Matematica(potencia(Pol("x",choice([-h,h])),2)+"+"+potencia(Pol("y",choice([-k,k])),2)+"="+choice([r, r**2, 2*r, (2*r)**2, Root(r), Root(2*r)])),
        Matematica("("+Pol("x",choice([-h,h]))+")+("+Pol("y",choice([-k,k]))+")="+choice([r, r**2, 2*r, (2*r)**2, Root(r), Root(2*r)]))
    ])+"."


enunciado_oculto = [h,k,r]










