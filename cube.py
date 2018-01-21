from enum import IntEnum


class Colour(IntEnum):
    # This class assigns numbers to the facelets of the cube for easier representation
    U = 0
    R = 1
    F = 2
    D = 3
    L = 4
    B = 5


class Facelets(IntEnum):
    """""
    The names of the facelet positions of the cube
                  |************|
                  |*U1**U2**U3*|
                  |************|
                  |*U4**U5**U6*|
                  |************|
                  |*U7**U8**U9*|
                  |************|
     |************|************|************|************|
     |*L1**L2**L3*|*F1**F2**F3*|*R1**R2**F3*|*B1**B2**B3*|
     |************|************|************|************|
     |*L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*|
     |************|************|************|************|
     |*L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*|
     |************|************|************|************|
                  |************|
                  |*D1**D2**D3*|
                  |************|
                  |*D4**D5**D6*|
                  |************|
                  |*D7**D8**D9*|
                  |************|

    A cube definition string "UBL..." means for example: In position U1 we have the U-color, in position U2 we have the
    B-color, in position U3 we have the L color etc. according to the order U1, U2, U3, U4, U5, U6, U7, U8, U9, R1, R2,
    R3, R4, R5, R6, R7, R8, R9, F1, F2, F3, F4, F5, F6, F7, F8, F9, D1, D2, D3, D4, D5, D6, D7, D8, D9, L1, L2, L3, L4,
    L5, L6, L7, L8, L9, B1, B2, B3, B4, B5, B6, B7, B8, B9 of the enum constants.
    """
    U1 = 0
    U2 = 1
    U3 = 2
    U4 = 3
    U5 = 4
    U6 = 5
    U7 = 6
    U8 = 7
    U9 = 8
    R1 = 9
    R2 = 10
    R3 = 11
    R4 = 12
    R5 = 13
    R6 = 14
    R7 = 15
    R8 = 16
    R9 = 17
    F1 = 18
    F2 = 19
    F3 = 20
    F4 = 21
    F5 = 22
    F6 = 23
    F7 = 24
    F8 = 25
    F9 = 26
    D1 = 27
    D2 = 28
    D3 = 29
    D4 = 30
    D5 = 31
    D6 = 32
    D7 = 33
    D8 = 34
    D9 = 35
    L1 = 36
    L2 = 37
    L3 = 38
    L4 = 39
    L5 = 40
    L6 = 41
    L7 = 42
    L8 = 43
    L9 = 44
    B1 = 45
    B2 = 46
    B3 = 47
    B4 = 48
    B5 = 49
    B6 = 50
    B7 = 51
    B8 = 52
    B9 = 53


class Corners(IntEnum):
    # This class assigns numbers to the corners of the cube for easier representation
    URF = 0
    UFL = 1
    ULB = 2
    UBR = 3
    DFR = 4
    DLF = 5
    DBL = 6
    DRB = 7


class Edges(IntEnum):
    # This class assigns numbers to the edges of the cube for easier representation
    UR = 0
    UF = 1
    UL = 2
    UB = 3
    DR = 4
    DF = 5
    DL = 6
    DB = 7
    FR = 8
    FL = 9
    BL = 10
    BR = 11


# These lists map each corner cubelet to its corresponding facelet colours
corner_colours = [[Colour.U, Colour.R, Colour.F], [Colour.U, Colour.F, Colour.L],
                 [Colour.U, Colour.L, Colour.B], [Colour.U, Colour.B, Colour.R],
                 [Colour.D, Colour.F, Colour.R], [Colour.D, Colour.L, Colour.F],
                 [Colour.D, Colour.B, Colour.L], [Colour.D, Colour.R, Colour.B]
                 ]
corner_facelets = [[Facelets.U9, Facelets.R1, Facelets.F3], [Facelets.U7, Facelets.F1, Facelets.L3],
                  [Facelets.U1, Facelets.L1, Facelets.B3], [Facelets.U3, Facelets.B1, Facelets.R3],
                  [Facelets.D3, Facelets.F9, Facelets.R7], [Facelets.D1, Facelets.L9, Facelets.F7],
                  [Facelets.D7, Facelets.B9, Facelets.L7], [Facelets.D9, Facelets.R9, Facelets.B7]
                 ]

# These lists map each edge cubelet to its corresponding facelet colours
edge_colours = [[Colour.U, Colour.R], [Colour.U, Colour.F], [Colour.U, Colour.L],
             [Colour.U, Colour.B], [Colour.D, Colour.R], [Colour.D, Colour.F],
             [Colour.D, Colour.L], [Colour.D, Colour.B], [Colour.F, Colour.R],
             [Colour.F, Colour.L], [Colour.B, Colour.L], [Colour.B, Colour.R]
             ]
edge_facelets = [[Facelets.U6, Facelets.R2], [Facelets.U8, Facelets.F2], [Facelets.U4, Facelets.L2],
               [Facelets.U2, Facelets.B2], [Facelets.D6, Facelets.R8], [Facelets.D2, Facelets.F8],
               [Facelets.D4, Facelets.L8], [Facelets.D8, Facelets.B8], [Facelets.F6, Facelets.R4],
               [Facelets.F4, Facelets.L6], [Facelets.B6, Facelets.L4], [Facelets.B4, Facelets.R6]
               ]


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
    def facelet_to_string(self):
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
    def string_to_facelet(self, string):
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


class CubeletCube:
    """This class represents a cubelet cube using 4 lists:
    1. The positions of the corners
    2. The orientation of the corners
    3. The positions of the edges
    4. The orientations of the edges

    It also includes methods that:
    1. Convert the cube to a facelet representation
    2. Convert the cube to a string representation that can be read by the user
    """
    def __init__(self):
        self.corner_positions = [Corners[i] for i in range(0, 8)]
        self.corner_orientation = [0, 0, 0, 0, 0, 0, 0, 0]
        self.edge_positions = [Edges[i] for i in range(0, 12)]
        self.edge_orientation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Converts from cubelet representation to facelet representation
    def cubelet_to_colour(self):
        fc = FaceletCube()
        for corner in Corners:
            position = self.corner_positions[i]
            orientation = self.corner_orientation[i]
            for face_of_cubelet in range(3):
                fc.fc[corner_facelets[corner][(face_of_cubelet + orientation) % 3]] = corner_colours[position][face_of_cubelet]
        for edge in Edges:
            position = self.edge_positions[i]
            orientation = self.edge_orientation[i]
            for face_of_cubelet in range(2):
                fc.fc[edge_facelets[edge][(face_of_cubelet + orientation) % 2]] = edge_colours[position][face_of_cubelet]
        return fc

    # Converts from cubelet representation to a string that the user can understand
    def cubelet_to_string(self):
        output_string = ""
        for corner in Corners:
            output_string += "(" + str(self.corner_positions[corner]) + ',' + str(self.corner_orientation[corner]) + ')'
        output_string += '\n'
        for edge in Edges:
            output_string += "(" + str(self.edge_positions[corner]) + ',' + str(self.edge_orientation[corner]) + ')'
        output_string += '\n'
        return output_string


def main():
    # Creates the object fc, which is of the class FaceletCube
    fc = FaceletCube()

    # This defines the initial state of the cube
    state_string = input("Enter initial cube state: ")
    fc.string_to_facelet(state_string)

    # The main program loop
    while True:
        print(fc.facelet_to_string())
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
