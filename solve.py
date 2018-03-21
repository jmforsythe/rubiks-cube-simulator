import facelet_cube
from enums_and_defs import *

solved_fc = facelet_cube.FaceletCube()
solved_fc.string_to_facelet(solved_cube)
solved_cc = solved_fc.facelet_to_cubelet()


def cross_solved(fc):
    cc = fc.facelet_to_cubelet()
    if (cc.edge_positions[4:8] == solved_cc.edge_positions[4:8] and
            cc.edge_orientation[4:8] == solved_cc.edge_orientation[4:8]):
        return True
    return False


def bottom_corners_solved(fc):
    cc = fc.facelet_to_cubelet()
    if (cc.corner_positions[4:8] == solved_cc.corner_positions[4:8] and
            cc.corner_orientation[4:8] == solved_cc.corner_orientation[4:8]):
        return True
    return False


def middle_layer_solved(fc):
    cc = fc.facelet_to_cubelet()
    if (cc.edge_positions[8:12] == solved_cc.edge_positions[8:12] and
        cc.edge_orientation[8:12] == solved_cc.edge_orientation[8:12]):
        return True
    return False


def oll_solved(fc):
    if fc.fc[0:9] == solved_fc.fc[0:9]:
        return True
    return False


def pll_solved(fc):
    cc = fc.facelet_to_cubelet()
    if (cc.corner_positions[0:4] == solved_cc.corner_positions[0:4] and
        cc.corner_orientation[0:4] == solved_cc.corner_orientation[0:4] and
        cc.edge_positions[0:4] == solved_cc.edge_positions[0:4] and
        cc.edge_orientation[0:4] == solved_cc.edge_orientation[0:4]):
        return True
    return False


def solve_cross(fc):
    return ""


def solve_bottom_corners(fc):
    return ""


def solve_middle_layer(fc):
    return ""


def oll_cross(fc):
    move = "FRUR'U'F'"
    if ([fc.fc[1], fc.fc[3:6], fc.fc[7]] ==
            [solved_fc.fc[1], solved_fc.fc[3:6], solved_fc.fc[7]]):  # cross case
        return ""
    elif fc.fc[3:6] == solved_fc.fc[3:6]:  # horizontal line case
        fc.execute_move(fc.sanitise_move(move))
        return move
    elif [fc.fc[1], fc.fc[3]] == [solved_fc.fc[1], solved_fc.fc[3]]:  # LB L shape case
        fc.execute_move(fc.sanitise_move(move))
        return move + oll_cross(fc)
    elif solved_fc.fc[4] not in [fc.fc[1], fc.fc[3:6], fc.fc[7]]:  # dot case
        fc.execute_move(fc.sanitise_move(move))
        return move + oll_cross(fc)
    else:  # other cases
        return "U" + oll_cross(fc)


def oll_corners(fc):
    cc = fc.facelet_to_cubelet()
    if cc.corner_orientation[:4] == [2, 0, 2, 2]:  # sune case
        fc.execute_move(fc.sanitise_move("RUR'URU2R'"))
        return "RUR'URU2R'"
    elif cc.corner_orientation[:4] == [0, 1, 1, 1]:  # anti-sune case
        fc.execute_move(fc.sanitise_move("L'URU'LUR'"))
        return "L'URU'LUR'"
    elif cc.corner_orientation[:4] == [0, 1, 2, 0]:  # chameleon case
        fc.execute_move(fc.sanitise_move("LFR'F'L'FRF'"))
        return "LFR'F'L'FRF'"
    elif cc.corner_orientation[:4] == [0, 2, 0, 1]:  # bow-tie case
        fc.execute_move(fc.sanitise_move("R2D'RU'R'DRUR"))
        return "R2D'RU'R'DRUR"
    elif cc.corner_orientation[:4] == [2, 1, 0, 0]:  # headlights case
        fc.execute_move(fc.sanitise_move("R2DR'U2RD'R'U2R'"))
        return "R2DR'U2RD'R'U2R'"
    elif cc.corner_orientation[:4] == [1, 2, 1, 2]:  # H case
        fc.execute_move(fc.sanitise_move("RUR'URU'R'URU2R'"))
        return "RUR'URU'R'URU2R'"
    elif cc.corner_orientation[:4] == [2, 2, 1, 1]:  # T-shirt case
        fc.execute_move(fc.sanitise_move("RU2R2U'R2U'R2U2R"))
        return "RU2R2U'R2U'R2U2R"
    else:
        fc.execute_move("U")
        return "U" + oll_corners(fc)


def solve_oll(fc):
    return oll_cross(fc) + oll_corners(fc)


def solve_pll(fc):
    return ""


def solve_cube(facelet_string):
    fc = facelet_cube.FaceletCube()
    fc.string_to_facelet(facelet_string)
    solution_string = ""
    if not cross_solved(fc):
        solution_string += solve_cross(fc)
    if not bottom_corners_solved(fc):
        solution_string += solve_bottom_corners(fc)
    if not middle_layer_solved(fc):
        solution_string += solve_middle_layer(fc)
    if not oll_solved(fc):
        solution_string += solve_oll(fc)
    if not pll_solved(fc):
        solution_string += solve_pll(fc)
    return solution_string

