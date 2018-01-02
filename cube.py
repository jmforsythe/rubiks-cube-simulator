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
    #This class represents the cube as a list of 54 colours
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

    #Converts from the internal representation to a string that the user can read
    def colourToString(self):
        outputString = ''
        for i in range(54):
            if self.fc[i] == Colour.U:
                outputString += 'U'
            elif self.fc[i] == Colour.R:
                outputString += 'R'
            elif self.fc[i] == Colour.F:
                outputString += 'F'
            elif self.fc[i] == Colour.D:
                outputString += 'D'
            elif self.fc[i] == Colour.L:
                outputString += 'L'
            elif self.fc[i] == Colour.B:
                outputString += 'B'
            if (i+1) % 9 == 0 and i > 0: outputString += ' '
        return outputString

    #Assigns values to each facelet by interpreting an input string
    def stringToColour(self, string):
        for i in range(54):
            if string[i] == 'U':
                self.fc[i] = Colour.U
            elif string[i] == 'R':
                self.fc[i] = Colour.R
            elif string[i] == 'F':
                self.fc[i] = Colour.F
            elif string[i] == 'D':
                self.fc[i] = Colour.D
            elif string[i] == 'L':
                self.fc[i] = Colour.L
            elif string[i] == 'B':
                self.fc[i] = Colour.B

    # These functions define the 6 basic moves that can be used to manipulate the cube
    def U(self):
        newOrder = [6,3,0,7,4,1,8,5,2,
                    45,46,47,12,13,14,15,16,17,
                    9,10,11,21,22,23,24,25,26,
                    27,28,29,30,31,32,33,34,35,
                    18,19,20,39,40,41,42,43,44,
                    36,37,38,48,49,50,51,52,53]
        self.fc = [self.fc[i] for i in newOrder]

    def R(self):
        newOrder = [0,1,20,3,4,23,6,7,26,
                    15,12,9,16,13,10,17,14,11,
                    18,19,29,21,22,32,24,25,35,
                    27,28,51,30,31,48,33,34,45,
                    36,37,38,39,40,41,42,43,44,
                    8,46,47,5,49,50,2,52,53]
        self.fc = [self.fc[i] for i in newOrder]

    def F(self):
        newOrder = [0, 1, 2, 3, 4, 5, 38, 41, 44,
                    6, 10, 11, 7, 13, 14, 8, 16, 17,
                    24, 21, 18, 25, 22, 19, 26, 23, 20,
                    15, 12, 9, 30, 31, 32, 33, 34, 35,
                    36, 37, 27, 39, 40, 28, 42, 43, 29,
                    45, 46, 47, 48, 49, 50, 51, 52, 53]
        self.fc = [self.fc[i] for i in newOrder]

    def D(self):
        newOrder = [0, 1, 2, 3, 4, 5, 6, 7, 8,
                    9, 10, 11, 12, 13, 14, 24, 25, 26,
                    18, 19, 20, 21, 22, 23, 42, 43, 44,
                    33, 30, 27, 34, 31, 28, 35, 32, 29,
                    36, 37, 38, 39, 40, 41, 51, 52, 53,
                    45, 46, 47, 48, 49, 50, 15, 16, 17]
        self.fc = [self.fc[i] for i in newOrder]

    def L(self):
        newOrder = [53, 1, 2, 50, 4, 5, 47, 7, 8,
                    9, 10, 11, 12, 13, 14, 15, 16, 17,
                    0, 19, 20, 3, 22, 23, 6, 25, 26,
                    18, 28, 29, 21, 31, 32, 22, 34, 35,
                    42, 39, 36, 43, 40, 37, 44, 41, 38,
                    45, 46, 33, 48, 49, 30, 51, 52, 27]
        self.fc = [self.fc[i] for i in newOrder]

    def B(self):
        newOrder = [11, 14, 17, 3, 4, 5, 6, 7, 8,
                    9, 10, 35, 12, 13, 34, 15, 16, 33,
                    18, 19, 20, 21, 22, 23, 24, 25, 26,
                    27, 28, 29, 30, 31, 32, 36, 39, 42,
                    2, 37, 38, 1, 40, 41, 0, 43, 44,
                    51, 48, 45, 52, 49, 46, 53, 50, 47]
        self.fc = [self.fc[i] for i in newOrder]


#Creates the object fc, which is of the class FaceletCube
fc = FaceletCube()

while True:
    print(fc.colourToString())
    userMove = input("Enter next move: ")
    if userMove == 'U': fc.U()
    elif userMove == 'R': fc.R()
    elif userMove == 'F': fc.F()
    elif userMove == 'D': fc.D()
    elif userMove == 'L': fc.L()
    elif userMove == 'B': fc.B()
    else: break
