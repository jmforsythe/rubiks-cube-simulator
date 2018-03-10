from enum import IntEnum
from PyQt5.QtGui import QColor

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

face_colours = [QColor(255, 255, 255), # white
                QColor(0, 0, 255), # blue,
                QColor(255, 0, 0), # red,
                QColor(255, 255, 0), # yellow,
                QColor(0, 255, 0), # green
                QColor(255, 165, 0) # orange
                ]