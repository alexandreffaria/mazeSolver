from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver | Boot.dev | @Alexandreffaria")
        self.canvas = Canvas(self.root, bg="black",height=height, width=width)
        self.canvas.pack()
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()
        print("window closed...")

    def close(self):
        self.isRunning = False


class Point():
    def __init__(self):
        self.x = 0
        self.y = 0

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )
        canvas.pack()
