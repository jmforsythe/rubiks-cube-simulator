from enums_and_defs import Colour, Corners, corner_colours, corner_facelets, Edges, edge_colours, edge_facelets
import cubelet_cube


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
        cc = cubelet_cube.CubeletCube()

        # When representing the corners, we start with the U or D face and then work clockwise
        # Cycle through each corner of our facelet cube
        for corner in Corners:
            # Loads the three relevant facelets for us to copy over
            faces_of_cubelet = corner_facelets[corner]

            # Finds which side of the cubelet is either the U or D face, which we start assigning from
            for orientation in range(3):
                if (self.fc[faces_of_cubelet[orientation]] == Colour.U or
                        self.fc[faces_of_cubelet[orientation]] == Colour.D):
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
                if (self.fc[edge_facelets[edge][0]] == edge_colours[test_edge][0] and
                        self.fc[edge_facelets[edge][1]] == edge_colours[test_edge][1]):
                    cc.edge_positions[edge] = test_edge
                    cc.edge_orientation[edge] = 0
                    break
                if (self.fc[edge_facelets[edge][0]] == edge_colours[test_edge][1] and
                        self.fc[edge_facelets[edge][1]] == edge_colours[test_edge][0]):
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

    moveF = [0, 1, 2, 3, 4, 5, 44, 41, 38,
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
             18, 28, 29, 21, 31, 32, 24, 34, 35,
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

    # This function combines every move inside of a string containing our 6 basic moves
    def combine_move_string(self, string, initial_move=moveI):
        combined_move = initial_move
        for character in string:
            if character == "U":
                combined_move = self.combine_move(combined_move, self.moveU)
            elif character == "R":
                combined_move = self.combine_move(combined_move, self.moveR)
            elif character == "F":
                combined_move = self.combine_move(combined_move, self.moveF)
            elif character == "D":
                combined_move = self.combine_move(combined_move, self.moveD)
            elif character == "L":
                combined_move = self.combine_move(combined_move, self.moveL)
            elif character == "B":
                combined_move = self.combine_move(combined_move, self.moveB)
        return combined_move

    # This function executes a move sequence on the stored cube
    def execute_move(self, string):
        self.fc = [self.fc[i] for i in self.combine_move_string(string)]

    def calculate_degree(self, string):
        combined_move = self.moveI
        counter = 0
        while True:
            combined_move = self.combine_move_string(string, combined_move)
            counter += 1
            if combined_move == self.moveI:
                return counter
