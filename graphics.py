from tkinter import Tk, BOTH, Canvas

class Window(Tk):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.title("Maze Solver | Boot.dev | @Alexandreffaria")
        self.canvas = Canvas(height=self.height, width=self.width)
        self.canvas.pack()
        self.isRunning = False
        self.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.update_idletasks()
        self.update()

    def wait_for_close(self):
        self.isRunning = True
        while self.isRunning:
            self.redraw()
    
    def close(self):
        self.isRunning = False
    