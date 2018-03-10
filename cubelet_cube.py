from enums_and_defs import Corners, corner_colours, corner_facelets, Edges, edge_colours, edge_facelets
import facelet_cube


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
        fc = facelet_cube.FaceletCube()
        for corner in Corners:
            position = self.corner_positions[corner]
            orientation = self.corner_orientation[corner]
            for face_of_cubelet in range(3):
                fc.fc[corner_facelets[corner][(face_of_cubelet + orientation) % 3]] = \
                    corner_colours[position][face_of_cubelet]
        for edge in Edges:
            position = self.edge_positions[edge]
            orientation = self.edge_orientation[edge]
            for face_of_cubelet in range(2):
                fc.fc[edge_facelets[edge][(face_of_cubelet + orientation) % 2]] = \
                    edge_colours[position][face_of_cubelet]
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
                return "Error: Not all edges exist."

        # Checks that there is exactly one case of each corner cubelet in the cubelet cube
        corner_count = [0, 0, 0, 0, 0, 0, 0, 0]
        # Counts each occurrence of each corner
        for corner in Corners:
            corner_count[self.corner_positions[corner]] += 1
        # Checks the each corner occurs exactly once
        for corner in Corners:
            if corner_count[corner] != 1:
                return "Error: Not all corners exist."

        edge_twist = 0
        for edge in Edges:
            edge_twist += self.edge_orientation[edge]
        if edge_twist % 2 != 0:
            return "Error: Total edge twist is wrong."

        corner_twist = 0
        for corner in Corners:
            corner_twist += self.corner_orientation[corner]
        if corner_twist % 3 != 0:
            return "Error: Total corner twist is wrong."

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
                if self.corner_positions[test_corner] > self.corner_positions[corner]:
                    corner_parity += 1
        corner_parity = corner_parity % 2

        if edge_parity != corner_parity:
            return 'Error: Wrong edge and corner parity.'

        return "Valid cube."
    