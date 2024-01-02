from graphics import Window, Point, Line, Cell

def main():
    janela = Window(800, 600)

    ponto1 = Point(10,10)

    ponto2 = Point(600,100)

    linha = Line(ponto1,ponto2)
    janela.draw_line(linha, "salmon")

    celula = Cell(ponto1, ponto2, janela)
    celula.draw()

    celula2 = Cell(Point(400,300), Point(500,400), janela)
    celula2.has_bottom_wall = False
    celula2.draw()

    celula3 = Cell(Point(125,125), Point(700,700), janela)
    celula3.has_bottom_wall = False
    celula3.has_left_wall = False
    celula3.draw()



    janela.wait_for_close()

if __name__ == "__main__":
    main()