from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver | Boot.dev | @Alexandreffaria")
        self.canvas = Canvas(self.__root, bg="black",height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.isRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color="salmon"):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()
        print("window closed...")

    def close(self):
        self.isRunning = False


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color="salmon"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)

