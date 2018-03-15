import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QGridLayout, QPushButton, QButtonGroup,
                             QSizePolicy, QTextEdit)
from PyQt5.QtGui import QColor, QIcon
from facelet_cube import FaceletCube
from enums_and_defs import face_colours_rgb, solved_cube

# Default width of facelet squares (in pixels) for drawing the window
width = 60
window_icon = "pexels-photo.jpg"


# Define the class that will define our program window, inheriting from the QWidget class
class NetDisplay(QWidget):
    def __init__(self):
        self.fc = FaceletCube()
        self.facelet_string = self.fc.facelet_to_string()

        # Calls the constructor of the QWidget class
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Initialises a grid, and sets the layout of the program window to grid
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        string_converter = [0, 1, 2,
                            3, 4, 5,
                            6, 7, 8,
                            36, 37, 38, 18, 19, 20, 9, 10, 11, 45, 46, 47,
                            39, 40, 41, 21, 22, 23, 12, 13, 14, 48, 49, 50,
                            42, 43, 44, 24, 25, 26, 15, 16, 17, 51, 52, 53,
                            27, 28, 29,
                            30, 31, 32,
                            33, 34, 35]
        # Inserts QFrames into the necessary grid positions in order to display the cube as a 2D net
        positions = [(i, j) for i in range(9) for j in range(12)]
        for position in positions:
            if position[0] in range(3, 6) or position[1] in range(3, 6):
                facelet = QPushButton(str(string_converter.pop(0)), self)
                facelet.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                facelet.col = QColor(235, 235, 235)
                facelet.clicked.connect(self.change_facelet)
                facelet.name = position
                self.grid.addWidget(facelet, *position)

        move_list = ("U", "R", "F", "D", "L", "B")
        move_button_positions = ((0, 8), (1, 9), (1, 8), (2, 8), (1, 7), (1, 10))
        for i in range(6):
            move_button = QPushButton(move_list[i])
            move_button.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            move_button.clicked.connect(self.execute_move)
            self.grid.addWidget(move_button, *move_button_positions[i])

        self.current_colour = ""
        colour_picker_positions = ((7, 9), (7, 10), (7, 11), (8, 9), (8, 10), (8, 11))
        colour_picker_group = QButtonGroup(self)
        for i in range(6):
            colour_picker = QPushButton(move_list[i])
            colour_picker.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
            colour_picker.setCheckable(True)
            colour_picker.setStyleSheet("QPushButton { background-color: %s; border: 1px solid black}"
                                        "QPushButton:checked { border: 3px solid black }" % face_colours_rgb[i])
            colour_picker.clicked.connect(self.assign_colour)
            colour_picker_group.addButton(colour_picker)
            self.grid.addWidget(colour_picker, *colour_picker_positions[i])

        self.move_entry = QTextEdit(self)
        self.move_entry.setPlaceholderText("Enter move string here")
        self.move_entry.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(self.move_entry, 0, 0, 2, 3)

        execute_move = QPushButton("Execute")
        execute_move.clicked.connect(self.execute_move)
        execute_move.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(execute_move, 2, 0, 1, 1)

        calculate_degree = QPushButton("Calculate Degree")
        calculate_degree.clicked.connect(self.calculate_degree)
        calculate_degree.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(calculate_degree, 2, 1, 1, 2)

        reset_cube = QPushButton("Reset")
        reset_cube.clicked.connect(self.reset)
        reset_cube.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(reset_cube, 7, 7, 1, 1)

        verify_cube = QPushButton("Verify")
        verify_cube.clicked.connect(self.verify)
        verify_cube.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(verify_cube, 7, 8, 1, 1)

        solve_cube = QPushButton("Solve")
        solve_cube.clicked.connect(self.solve)
        solve_cube.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(solve_cube, 8, 7, 1, 2)

        self.output_textbox = QTextEdit(self)
        self.output_textbox.setReadOnly(True)
        self.output_textbox.setPlaceholderText("Program Output")
        self.output_textbox.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.grid.addWidget(self.output_textbox, 6, 0, 3, 3)

        # Sets the initial cube to be a solved cube
        self.modify(self.facelet_string)

        # Defines the size of the window and displays it
        self.setWindowTitle("Rubik's Cube Simulator")
        self.setWindowIcon(QIcon(window_icon))
        self.setGeometry(300, 300, width * 12 + 100, width * 9 + 100)
        self.show()

    def modify(self, facelet_string):
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
        facelet_string = [facelet_string.replace(" ", "")[i] for i in string_converter]

        # This reads the converted facelet string, and colours in each facelet square accordingly
        for facelet in range(54):
            frame = self.grid.itemAt(facelet).widget()
            if facelet_string[facelet] == "U":
                frame.col = face_colours_rgb[0]
            if facelet_string[facelet] == "R":
                frame.col = face_colours_rgb[1]
            if facelet_string[facelet] == "F":
                frame.col = face_colours_rgb[2]
            if facelet_string[facelet] == "D":
                frame.col = face_colours_rgb[3]
            if facelet_string[facelet] == "L":
                frame.col = face_colours_rgb[4]
            if facelet_string[facelet] == "B":
                frame.col = face_colours_rgb[5]
            frame.setStyleSheet("background-color: %s; color: %s; margin:0px; border:2px solid rgb(20,20,20);"
                                % (frame.col, frame.col))

    @staticmethod
    def sanitise_move(string):
        move_string = ""
        for i in range(len(string)):
            # Support for 90° clockwise moves
            if string[i] in ["U", "R", "F", "D", "L", "B"]:
                move_string += string[i]
            # Support for 90° anticlockwise moves
            elif string[i] == "\'":
                move_string += string[i - 1] * 2
            # Support for 180° moves
            elif string[i] == "2":
                move_string += string[i - 1]
        return move_string

    def execute_move(self):
        if self.sender().text() in ("U", "R", "F", "D", "L", "B"):
            self.fc.execute_move(self.sender().text())
        else:
            text_box = self.move_entry.toPlainText()
            self.fc.execute_move(self.sanitise_move(text_box))
        self.modify(self.fc.facelet_to_string())

    def calculate_degree(self):
        text_box = self.move_entry.toPlainText()
        degree = self.fc.calculate_degree(self.sanitise_move(text_box))
        self.output_textbox.append(
            "Degree of algorithm <font color=\"red\">%s</font> is <b>%s</b>" % (text_box, degree))

    def reset(self):
        self.fc.string_to_facelet(solved_cube)
        self.modify(self.fc.facelet_to_string())

    def verify(self):
        output_text = "Valid Cube."
        # Checks that the cube is a valid facelet cube
        is_valid = self.fc.verify()
        if is_valid != "Valid cube.":
            output_text = is_valid
        else:
            # Checks that the cube is a valid cubelet cube
            cc = self.fc.facelet_to_cubelet()
            is_valid = cc.is_valid_state()
            if is_valid != "Valid cube.":
                output_text = is_valid
        self.output_textbox.append(output_text)

    def assign_colour(self):
        self.current_colour = self.sender().text()

    def change_facelet(self):
        index = int(self.sender().text())
        if self.current_colour != "" and index not in (4, 13, 22, 31, 40, 49):
            facelet_string = self.fc.facelet_to_string().replace(" ", "")
            facelet_string = facelet_string[:index] + self.current_colour + facelet_string[index+1:]
            self.fc.string_to_facelet(facelet_string)
            self.modify(self.fc.facelet_to_string())

    def solve(self):
        if self.fc.verify() != self.fc.facelet_to_cubelet().is_valid_state():
            self.output_textbox.append("Cannot solve cube:")
            self.verify()
        else:
            self.output_textbox.append("Solved.")


def main():
    app = QApplication(sys.argv)
    net_display = NetDisplay()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
