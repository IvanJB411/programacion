from dado_plano import DadoSimple

if __name__ == "__main__":

    dado1 = DadoSimple()
    dado2 = DadoSimple(valor=4)
    dado3 = DadoSimple(caras=20, valor=8)
    dado4 = DadoSimple()

    print("Estos son los dados:")

    dados = [dado1,dado2,dado3,dado4]
    for i in dados:
        print(f"{i}", end="")
        print()
    print()
    print("Estos son los dados al lanzarlos:")

    for i in dados:
        i.roll()
        for j in dados:
            print(f"{j}", end="")
            print()
        print()


