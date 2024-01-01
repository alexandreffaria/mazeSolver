from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver | Boot.dev | @Alexandreffaria")
        self.canvas = Canvas(height=self.height, width=self.width)
        self.canvas.pack()
        self.isRunning = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

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
    