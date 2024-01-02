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

class Cell():
    def __init__(self, point1, point2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = point1.x
        self.__x2 = point2.x
        self.__y1 = point1.y
        self.__y2 = point2.y
        self.__win = window

    def draw(self):
        x1 = self.__x1
        y1 = self.__y1
        x2 = self.__x2
        y2 = self.__y2

        if self.has_left_wall:
            Line(Point(x1,y1),Point(x1,y2)).draw(self.__win.canvas)
        if self.has_right_wall:
            Line(Point(x2,y1),Point(x2,y2)).draw(self.__win.canvas)
        if self.has_top_wall:
            Line(Point(x1,y1),Point(x2,y1)).draw(self.__win.canvas)
        if self.has_bottom_wall:
            Line(Point(x1,y2),Point(x2,y2)).draw(self.__win.canvas)