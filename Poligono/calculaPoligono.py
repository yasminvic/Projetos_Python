from ponto import Ponto
from poligono import Poligono

resp = 1
while resp != 0:
    print("\t *** Cálculo de Poligonos ***\n")
    poligono = Poligono()
    poligono.pontos.clear()
    while True:
        print("\nInforme os pontos x e y de seu Poligono: \n")
        x = int(input("Ponto x: (0 - Parar) "))
        if x == 0:
            break
        y = int(input("Ponto y: "))

        ponto = Ponto(x, y)
        poligono.addPontos(ponto.x, ponto.y)
        print(len(poligono.pontos))

    print(len(poligono.pontos))
    if len(poligono.pontos) >= 3:
        print("\n -----------MENU-----------")
        print("| 1 - Calcular Perímetro  |")
        print("| 2 - Calcular Área       |")
        print("| 0 - Sair                |")
        print(" --------------------------")
        resp = int(input("Escolha uma opção do menu: "))
    
        if resp == 1:
            print(f"\nPerímetro é igual a: {poligono.perimetro()}")
            print("-----x---------x----------x----------x-------\n")
        elif resp == 2:
            print(f"\nPerímetro é igual a: {poligono.area()}")
            print("-----x---------x----------x----------x-------\n")
        elif resp == 0:
            print("\nFim do Programa !")
            print("-----x---------x------\n")
            exit()
        else:
            print("Opção inválida !\n")
    else:
        print("Poligono inválido. Informe novamente!\n")
