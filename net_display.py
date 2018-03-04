import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QFrame
from PyQt5.QtGui import QColor

width = 60


class Example(QWidget):
    def __init__(self, facelet_string):
        super().__init__()

        self.initUI(facelet_string.replace(" ", ""))

    def initUI(self, facelet_string):
        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i, j) for i in range(9) for j in range(12)]
        for position in positions:
            if (position[0] in range(3) or position[0] in range(6, 9)) and position[1] not in range(3, 6):
                continue
            frame = QFrame(self)
            frame.col = QColor(235, 235, 235)
            frame.setStyleSheet("background-color: %s; margin:10px; border:3px solid rgb(20,20,20); " % frame.col.name())
            grid.addWidget(frame, *position)

        frame = grid.itemAt(53).widget()
        frame.col = QColor(255,0,0)
        frame.setStyleSheet("background-color: %s;" % frame.col.name())

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

        self.setGeometry(300, 300, (width + 10) * 12 + 100, (width + 10) * 9 + 100)
        self.show()


def launch(facelet_string):
    app = QApplication(sys.argv)
    ex = Example(facelet_string)
    app.exec_()


if __name__ == '__main__':
    facelet_string = "LBBLURRRU FUDFRRLDR DFLFFDRLD FFFLDRDDB BUFBLUBDU LUUBBLUBR".replace(" ", "")
    app = QApplication(sys.argv)
    ex = Example(facelet_string)
    sys.exit(app.exec_())
