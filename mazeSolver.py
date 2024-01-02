from graphics import Window, Point, Line
from cell import Cell

def main():
    janela = Window(800, 600)

    ponto1 = Point(10,10)

    ponto2 = Point(600,100)

    linha = Line(ponto1,ponto2)
    janela.draw_line(linha, "salmon")

    celula = Cell(janela)
    celula.draw(10,10,249,100)

    celula2 = Cell(janela)
    celula2.has_bottom_wall = False
    celula2.draw(250,250, 300, 300)

    celula3 = Cell(janela)
    celula3.has_bottom_wall = False
    celula3.has_left_wall = False
    celula3.draw(123, 203, 432, 39)

    celula2.draw_move(celula)
    celula.draw_move(celula3, undo=True)

    janela.wait_for_close()

if __name__ == "__main__":
    main()