from graphics import Line, Point


class Cell():
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__x2 = None
        self.__y1 = None
        self.__y2 = None
        self.__win = window
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1 
        self.__y1 = y1 
        self.__x2 = x2 
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x1,y2))
            self.__win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2,y1),Point(x2,y2))
            self.__win.draw_line(line, "black")   
        if self.has_top_wall:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1,y1),Point(x2,y1))
            self.__win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1,y2),Point(x2,y2))
            self.__win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        if not undo:
            color_line = "cyan"
        else:
            color_line = "gray"
        
        x_self = (self.__x1 + self.__x2)/2
        y_self = (self.__y1 + self.__y2)/2

        x_to_cell = (to_cell.__x1 + to_cell.__x2)/2
        y_to_cell = (to_cell.__y1 + to_cell.__y2)/2

       # moving left
        if self.__x1 > to_cell.__x1:
            end_point = Point(to_cell.__x1, y_self)
            line = Line(Point(x_self, y_self), end_point)
            self.__win.draw_line(line, color_line)

        # moving right
        elif self.__x1 < to_cell.__x1:
            end_point = Point(to_cell.__x2, y_self)
            line = Line(Point(x_self, y_self), end_point)
            self.__win.draw_line(line, color_line)

        # moving up
        elif self.__y1 > to_cell.__y1:
            end_point = Point(x_self, to_cell.__y1)
            line = Line(Point(x_self, y_self), end_point)
            self.__win.draw_line(line, color_line)

        # moving down
        elif self.__y1 < to_cell.__y1:
            end_point = Point(x_self, to_cell.__y2)
            line = Line(Point(x_self, y_self), end_point)
            self.__win.draw_line(line, color_line)




