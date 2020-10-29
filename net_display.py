import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QFrame
from PyQt5.QtGui import QColor

# Default width of facelet squares (in pixels) for drawing the window
width = 60


# Define the class that will define our program window, inheriting from the QWidget class
class NetDisplay(QWidget):
    def __init__(self, facelet_string):
        # Calls the constructor of the QWidget class
        super().__init__()

        # Initialises window while sanitising the facelet string by removing spaces
        self.init_ui(facelet_string.replace(" ", ""))

    def init_ui(self, facelet_string):
        # Initialises a grid, and sets the layout of the program window to grid
        grid = QGridLayout()
        self.setLayout(grid)

        # Inserts QFrames into the necessary grid positions in order to display the cube as a 2D net
        positions = [(i, j) for i in range(9) for j in range(12)]
        for position in positions:
            if position[0] in range(3, 6) or position[1] in range(3, 6):
                frame = QFrame(self)
                frame.col = QColor(235, 235, 235)
                frame.setStyleSheet("background-color: %s; margin:10px; border:3px solid rgb(20,20,20); "
                                    % frame.col.name())
                grid.addWidget(frame, *position)

        # This array converts the string format generated from the facelet representation into something that
        # can be displayed on the grid, as the grid is numbered row by row, left to right
        string_converter = [0, 1, 2,
                            3, 4, 5,
                            6, 7, 8,
                            36, 37, 38, 18, 19, 20, 9, 10, 11, 45, 46, 47,
                            39, 40, 41, 21, 22, 23, 12, 13, 14, 48, 49, 50,
                            42, 43, 44, 24, 25, 26, 15, 16, 17, 51, 52, 53,
                            27, 28, 29,
                            30, 31, 32,
                            33, 34, 35]
        facelet_string = [facelet_string[i] for i in string_converter]

        # This reads the converted facelet string, and colours in each facelet square accordingly
        for facelet in range(54):
            frame = grid.itemAt(facelet).widget()
            if facelet_string[facelet] == "U":
                frame.col = QColor(255, 255, 255)  # white
            if facelet_string[facelet] == "R":
                frame.col = QColor(0, 0, 255)  # blue
            if facelet_string[facelet] == "F":
                frame.col = QColor(255, 0, 0)  # red
            if facelet_string[facelet] == "D":
                frame.col = QColor(255, 255, 0)  # yellow
            if facelet_string[facelet] == "L":
                frame.col = QColor(0, 255, 0)  # green
            if facelet_string[facelet] == "B":
                frame.col = QColor(255, 165, 0)  # orange
            frame.setStyleSheet("background-color: %s; margin:0px; border:2px solid rgb(20,20,20);" % frame.col.name())

        # Defines the size of the window and displays it
        self.setGeometry(300, 300, width * 12 + 100, width * 9 + 100)
        self.show()


def launch(facelet_string):
    app = QApplication(sys.argv)
    net_display = NetDisplay(facelet_string)
    app.exec_()
