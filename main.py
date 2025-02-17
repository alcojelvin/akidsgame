def probabilidade_disparo(capsulas_reais, capsulas_festim):
    chambers = capsulas_reais + capsulas_festim
    return (capsulas_reais / chambers) * 100

def obter_entradas():
    capsulas_reais = int(input("Número de cápsulas reais: "))
    capsulas_festim = int(input("Número de cápsulas de festim: "))
    return capsulas_reais, capsulas_festim

def verificar_capsula_disponivel(resultado, capsulas_reais, capsulas_festim):
    if resultado == "real" and capsulas_reais == 0:
        print ("Não há mais balas reais disponíveis")
        return False
    elif resultado == "festim" and capsulas_festim == 0:
        print ("Não há mais cápsulas de festim disponíveis")
        return False
    return True

def pedir_tipo_capsula(capsulas_reais, capsulas_festim):
    resultado = ""
    while resultado not in ["real", "festim"]:
        resultado = input("A cápsula disparada era real ou de festim? (real/festim): ").strip().lower()
        if not verificar_capsula_disponivel(resultado, capsulas_reais, capsulas_festim):
            resultado = ""
    return resultado

def roleta_russa(capsulas_reais, capsulas_festim):
    while capsulas_reais > 0 or capsulas_festim > 0:
        probabilidade = probabilidade_disparo(capsulas_reais, capsulas_festim)
        print (f"\nProbabilidade do próximo disparo ser uma bala real: {probabilidade:.2f}%")

        resultado = pedir_tipo_capsula(capsulas_reais, capsulas_festim)

        if resultado == "real":
            capsulas_reais -= 1
        elif resultado == "festim":
            capsulas_festim -= 1

        print (f"\nStatus atual: {capsulas_reais} balas e {capsulas_festim} cápsulas de festim restantes")

    print("\nJogo finalizado! Sem balas restantes")

capsulas_reais, capsulas_festim = obter_entradas()
roleta_russa(capsulas_reais, capsulas_festim)