import facelet_cube
from enums_and_defs import *

solved_fc = facelet_cube.FaceletCube()
solved_fc.string_to_facelet(solved_cube)
solved_cc = solved_fc.facelet_to_cubelet()


def cross_solved(facelet_string):
    fc = facelet_cube.FaceletCube()
    fc.string_to_facelet(facelet_string)
    cc = fc.facelet_to_cubelet()
    if (cc.edge_positions[4:8] == solved_cc.edge_positions[4:8] and
        cc.edge_orientation[4:8] == solved_cc.edge_orientation[4:8]):
        return True
    return False


def bottom_corners_solved(facelet_string):
    fc = facelet_cube.FaceletCube()
    fc.string_to_facelet(facelet_string)
    cc = fc.facelet_to_cubelet()
    if (cc.corner_positions[4:8] == solved_cc.corner_positions[4:8] and
        cc.corner_orientation[4:8] == solved_cc.corner_orientation[4:8]):
        return True
    return False


def middle_layer_solved(facelet_string):
    fc = facelet_cube.FaceletCube()
    fc.string_to_facelet(facelet_string)
    cc = fc.facelet_to_cubelet()
    if (cc.edge_positions[8:12] == solved_cc.edge_positions[8:12] and
        cc.edge_orientation[8:12] == solved_cc.edge_orientation[8:12]):
        return True
    return False


def oll_solved(facelet_string):
    if facelet_string[0:9] == solved_cube[0:9]:
        return True
    return False


def pll_solved(facelet_string):
    fc = facelet_cube.FaceletCube()
    fc.string_to_facelet(facelet_string)
    cc = fc.facelet_to_cubelet()
    if (cc.corner_positions[0:4] == solved_cc.corner_positions[0:4] and
        cc.corner_orientation[0:4] == solved_cc.corner_orientation[0:4] and
        cc.edge_positions[0:4] == solved_cc.edge_positions[0:4] and
        cc.edge_orientation[0:4] == solved_cc.edge_orientation[0:4]):
        return True
    return False


def solve_cross(facelet_string):
    return ""


def solve_bottom_corners(facelet_string):
    return ""


def solve_middle_layer(facelet_string):
    return ""


def solve_oll(facelet_string):
    return ""


def solve_pll(facelet_string):
    return ""


def solve_cube(facelet_string):
    solution_string = ""
    if not cross_solved(facelet_string):
        solution_string.append(solve_cross(facelet_string))
    if not bottom_corners_solved(facelet_string):
        solution_string.append(solve_bottom_corners(facelet_string))
    if not middle_layer_solved(facelet_string):
        solution_string.append(solve_middle_layer(facelet_string))
    if not oll_solved(facelet_string):
        solution_string.append(solve_oll(facelet_string))
    if not pll_solved(facelet_string):
        solution_string.append(solve_pll(facelet_string))
    return solution_string

