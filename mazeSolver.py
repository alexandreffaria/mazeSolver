from graphics import Window, Point, Line

def main():
    janela = Window(800, 600)

    ponto1 = Point(10,10)

    ponto2 = Point(600,100)

    linha = Line(ponto1,ponto2)
    janela.draw_line(linha, "salmon")

    janela.wait_for_close()

if __name__ == "__main__":
    main()