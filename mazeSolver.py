from graphics import Window, Point, Line

def main():
    janela = Window(
    800, 600
    )

    ponto1 = Point()
    ponto1.x = 10
    ponto1.y = 10
    ponto2 = Point()
    ponto2.x = 600
    ponto2.y = 100
    linha = Line(ponto1,ponto2)
    janela.draw_line(linha, "salmon")

    janela.wait_for_close()

if __name__ == "__main__":
    main()