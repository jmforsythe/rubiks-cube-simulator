from enum import IntEnum


class Colour(IntEnum):
    # This class defines the data type that is used in the internal representation of the facelets of the cube
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5


class FaceletCube:
    """This class represents the cube as a list of 54 colours

    It also contains methods for:
    1. Performing moves on the cube
    2. Combining cube moves together before execution
    3. Converting between the internal representation and a string that the user can understand
    """
    def __init__(self):
        self.fc = []
        for i in range(9):
            self.fc.append(Colour.U)
        for i in range(9):
            self.fc.append(Colour.R)
        for i in range(9):
            self.fc.append(Colour.F)
        for i in range(9):
            self.fc.append(Colour.D)
        for i in range(9):
            self.fc.append(Colour.L)
        for i in range(9):
            self.fc.append(Colour.B)

    # Converts from the internal representation to a string that the user can read
    def colour_to_string(self):
        output_string = ""
        for i in range(54):
            if self.fc[i] == Colour.U:
                output_string += "U"
            elif self.fc[i] == Colour.R:
                output_string += "R"
            elif self.fc[i] == Colour.F:
                output_string += "F"
            elif self.fc[i] == Colour.D:
                output_string += "D"
            elif self.fc[i] == Colour.L:
                output_string += "L"
            elif self.fc[i] == Colour.B:
                output_string += "B"
            if (i + 1) % 9 == 0 and i > 0:
                output_string += " "
        return output_string

    # Assigns values to each facelet by interpreting an input string
    def string_to_colour(self, string):
        for i in range(len(string)):
            if string[i] == "U":
                self.fc[i] = Colour.U
            elif string[i] == "R":
                self.fc[i] = Colour.R
            elif string[i] == "F":
                self.fc[i] = Colour.F
            elif string[i] == "D":
                self.fc[i] = Colour.D
            elif string[i] == "L":
                self.fc[i] = Colour.L
            elif string[i] == "B":
                self.fc[i] = Colour.B
            else:
                pass

    # This list defines the identity move (no facelets move)
    moveI = [0, 1, 2, 3, 4, 5, 6, 7, 8,
             9, 10, 11, 12, 13, 14, 15, 16, 17,
             18, 19, 20, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 33, 34, 35,
             36, 37, 38, 39, 40, 41, 42, 43, 44,
             45, 46, 47, 48, 49, 50, 51, 52, 53]

    # These lists define the 6 basic moves that can be used to manipulate the cube
    moveU = [6, 3, 0, 7, 4, 1, 8, 5, 2,
             45, 46, 47, 12, 13, 14, 15, 16, 17,
             9, 10, 11, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 33, 34, 35,
             18, 19, 20, 39, 40, 41, 42, 43, 44,
             36, 37, 38, 48, 49, 50, 51, 52, 53]

    moveR = [0, 1, 20, 3, 4, 23, 6, 7, 26,
             15, 12, 9, 16, 13, 10, 17, 14, 11,
             18, 19, 29, 21, 22, 32, 24, 25, 35,
             27, 28, 51, 30, 31, 48, 33, 34, 45,
             36, 37, 38, 39, 40, 41, 42, 43, 44,
             8, 46, 47, 5, 49, 50, 2, 52, 53]

    moveF = [0, 1, 2, 3, 4, 5, 38, 41, 44,
             6, 10, 11, 7, 13, 14, 8, 16, 17,
             24, 21, 18, 25, 22, 19, 26, 23, 20,
             15, 12, 9, 30, 31, 32, 33, 34, 35,
             36, 37, 27, 39, 40, 28, 42, 43, 29,
             45, 46, 47, 48, 49, 50, 51, 52, 53]

    moveD = [0, 1, 2, 3, 4, 5, 6, 7, 8,
             9, 10, 11, 12, 13, 14, 24, 25, 26,
             18, 19, 20, 21, 22, 23, 42, 43, 44,
             33, 30, 27, 34, 31, 28, 35, 32, 29,
             36, 37, 38, 39, 40, 41, 51, 52, 53,
             45, 46, 47, 48, 49, 50, 15, 16, 17]

    moveL = [53, 1, 2, 50, 4, 5, 47, 7, 8,
             9, 10, 11, 12, 13, 14, 15, 16, 17,
             0, 19, 20, 3, 22, 23, 6, 25, 26,
             18, 28, 29, 21, 31, 32, 22, 34, 35,
             42, 39, 36, 43, 40, 37, 44, 41, 38,
             45, 46, 33, 48, 49, 30, 51, 52, 27]

    moveB = [11, 14, 17, 3, 4, 5, 6, 7, 8,
             9, 10, 35, 12, 13, 34, 15, 16, 33,
             18, 19, 20, 21, 22, 23, 24, 25, 26,
             27, 28, 29, 30, 31, 32, 36, 39, 42,
             2, 37, 38, 1, 40, 41, 0, 43, 44,
             51, 48, 45, 52, 49, 46, 53, 50, 47]

    # This function combines any two reordering lists of the same length
    @staticmethod
    def combine_move(move1, move2):
        combined_move = [move1[i] for i in move2]
        return combined_move

    # This function takes a string consisting of some combination of the 6 basic moves, combines them into a single
    # move, and executes them
    def execute_move(self, string):
        current_move = self.moveI
        for character in string:
            if character == "U":
                current_move = self.combine_move(current_move, self.moveU)
            elif character == "R":
                current_move = self.combine_move(current_move, self.moveR)
            elif character == "F":
                current_move = self.combine_move(current_move, self.moveF)
            elif character == "D":
                current_move = self.combine_move(current_move, self.moveD)
            elif character == "L":
                current_move = self.combine_move(current_move, self.moveL)
            elif character == "B":
                current_move = self.combine_move(current_move, self.moveB)
        self.fc = [self.fc[i] for i in current_move]


def main():
    # Creates the object fc, which is of the class FaceletCube
    fc = FaceletCube()

    # This defines the initial state of the cube
    state_string = input("Enter initial cube state: ")
    fc.string_to_colour(state_string)

    # The main program loop
    while True:
        print(fc.colour_to_string())
        move_string = ""
        user_input = input("Enter move string: ")
        for i in range(len(user_input)):
            # Support for 90° clockwise moves
            if user_input[i] in ["U", "R", "F", "D", "L", "B"]:
                move_string += user_input[i]
            # Support for 90° anticlockwise moves
            elif user_input[i] == "\'":
                move_string += user_input[i - 1] * 2
            # Support for 180° moves
            elif user_input[i] == "2":
                move_string += user_input[i - 1]
            # Support for spaces and commas in user input
            elif user_input in [" ", ","]:
                pass
            else:
                return 0
        fc.execute_move(move_string)


if __name__ == "__main__":
    main()
