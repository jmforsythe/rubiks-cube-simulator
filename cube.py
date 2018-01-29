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


# These lists map each corner cubelet to its corresponding facelet colours, starting with U or D and going clockwise
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
        # We will have a running count for each face colour in order to verify that there are 9 facelets of each colour
        count = [0, 0, 0, 0, 0, 0]
        for facelet in range(len(string)):
            if string[facelet] == "U":
                self.fc[facelet] = Colour.U
                count[Colour.U] += 1
            elif string[facelet] == "R":
                self.fc[facelet] = Colour.R
                count[Colour.R] += 1
            elif string[facelet] == "F":
                self.fc[facelet] = Colour.F
                count[Colour.F] += 1
            elif string[facelet] == "D":
                self.fc[facelet] = Colour.D
                count[Colour.D] += 1
            elif string[facelet] == "L":
                self.fc[facelet] = Colour.L
                count[Colour.L] += 1
            elif string[facelet] == "B":
                self.fc[facelet] = Colour.B
                count[Colour.B] += 1
        # Checks that each of the counts equals 9
        if all(i == 9 for i in count):
            return "Valid cube."
        else:
            return "Cube initial state does not contain 9 of each colour."

    # Converts from the facelet representation to a cubelet representation
    def facelet_to_cubelet(self):
        cc = CubeletCube()

        # When representing the corners, we start with the U or D face and then work clockwise
        # Cycle through each corner of our facelet cube
        for corner in Corners:
            # Loads the three relevant facelets for us to copy over
            faces_of_cubelet = corner_facelets[corner]

            # Finds which side of the cubelet is either the U or D face, which we start assigning from
            for orientation in range(3):
                if self.fc[faces_of_cubelet[orientation]] == Colour.U or self.fc[faces_of_cubelet[orientation]] == Colour.D:
                    break

            # Cycles through the other sides of the cubelet in a clockwise order, in order to identify the cubelet
            clockwise_face = self.fc[faces_of_cubelet[(orientation + 1) % 3]]
            anticlockwise_face = self.fc[faces_of_cubelet[(orientation - 1) % 3]]

            # Cycles through each possible corner and compares it to our actual corner
            for test_corner in Corners:
                test_corner_colours = corner_colours[test_corner]
                # If faces match, assign cubelet in cubelet cube and exit loop
                if clockwise_face == test_corner_colours[1] and anticlockwise_face == test_corner_colours[2]:
                    cc.corner_positions[corner] = test_corner
                    cc.corner_orientation[corner] = orientation
                    break

        # When representing the edges, cycle through each possible edge, comparing each face to the faces on our cube
        # Cycle through each edge of our facelet cube
        for edge in Edges:
            for test_edge in Edges:
                if self.fc[edge_facelets[edge][0]] == edge_colours[test_edge][0] and self.fc[edge_facelets[edge][1]] == edge_colours[test_edge][1]:
                    cc.edge_positions[edge] = test_edge
                    cc.edge_orientation[edge] = 0
                    break
                if self.fc[edge_facelets[edge][0]] == edge_colours[test_edge][1] and self.fc[edge_facelets[edge][1]] == edge_colours[test_edge][0]:
                    cc.edge_positions[edge] = test_edge
                    cc.edge_orientation[edge] = 1
                    break
        return cc

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
        self.corner_positions = [Corners(i) for i in range(0, 8)]
        self.corner_orientation = [0, 0, 0, 0, 0, 0, 0, 0]
        self.edge_positions = [Edges(i) for i in range(0, 12)]
        self.edge_orientation = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Converts from cubelet representation to facelet representation
    def cubelet_to_colour(self):
        fc = FaceletCube()
        for corner in Corners:
            position = self.corner_positions[corner]
            orientation = self.corner_orientation[corner]
            for face_of_cubelet in range(3):
                fc.fc[corner_facelets[corner][(face_of_cubelet + orientation) % 3]] = corner_colours[position][face_of_cubelet]
        for edge in Edges:
            position = self.edge_positions[edge]
            orientation = self.edge_orientation[edge]
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
            output_string += "(" + str(self.edge_positions[edge]) + ',' + str(self.edge_orientation[edge]) + ')'
        output_string += '\n'
        return output_string

    # Checks that the currently stored cubelet cube is in a valid state
    def is_valid_state(self):

        # Checks that there is exactly one case of each edge cubelet in the cubelet cube
        edge_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # Counts each occurrence of each edge
        for edge in Edges:
            edge_count[self.edge_positions[edge]] += 1
        # Checks the each corner occurs exactly once
        for edge in Edges:
            if edge_count[edge] != 1:
                return 'Error: Not all edges exist.'

        # Checks that there is exactly one case of each corner cubelet in the cubelet cube
        corner_count = [0, 0, 0, 0, 0, 0, 0, 0]
        # Counts each occurrence of each corner
        for corner in Corners:
            corner_count[self.corner_positions[corner]] += 1
        # Checks the each corner occurs exactly once
        for corner in Corners:
            if corner_count[corner] != 1:
                return 'Error: Not all corners exist.'

        edge_twist = 0
        for edge in Edges:
            edge_twist += self.edge_orientation[edge]
        if edge_twist % 2 != 0:
            return 'Error: Total edge twist is wrong.'

        corner_twist = 0
        for corner in Corners:
            corner_twist += self.corner_orientation[corner]
        if corner_twist % 3 != 0:
            return 'Error: Total corner twist is wrong.'

        # Parity of a cube refers to whether the swaps required to make that cube from a solved cube is even or odd
        # The total parity must always be even, either from having edge and corner parity be both even or both odd

        # Calculates if the edges of the cubelet cube have even or odd parity
        edge_parity = 0
        for edge in range(Edges.BR, Edges.UR, -1):
            for test_edge in range(edge - 1, Edges.UR - 1, -1):
                if self.edge_positions[test_edge] > self.edge_positions[edge]:
                    edge_parity += 1
        edge_parity = edge_parity % 2

        # Calculates if the corners of the cubelet cube have even or odd parity
        corner_parity = 0
        for corner in range(Corners.DRB, Corners.URF, -1):
            for test_corner in range(corner - 1, Corners.URF - 1, -1):
                if self.corner_positions[test_corner] > self.edge_positions[corner]:
                    corner_parity += 1
        corner_parity = corner_parity % 2

        if edge_parity != corner_parity:
            return 'Error: Wrong edge and corner parity.'

        return "Valid cube."


def main():
    # Creates the object fc, which is of the class FaceletCube
    fc = FaceletCube()

    # This defines the initial state of the cube
    state_string = input("Enter initial cube state (leave blank for solved cube): ")

    # Skips cube verification if state string is empty
    if state_string != "":
        # Checks that the cube is a valid facelet cube
        is_valid = fc.string_to_facelet(state_string)
        if is_valid != "Valid cube.":
            print(is_valid)
            return 0

        # Checks that the cube is a valid cubelet cube
        cc = fc.facelet_to_cubelet()
        is_valid = cc.is_valid_state()
        if is_valid != "Valid cube.":
            print(is_valid)
            return 0

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
