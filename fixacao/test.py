def indicador_triangulo(lista):
    lado_a = lista[0]
    lado_b = lista[1]
    lado_c = lista[2]

    if lado_a < lado_c + lado_b and lado_b < lado_c + lado_a and lado_c < lado_a + lado_b:
        return "Sim"
    else:
        return "Não"