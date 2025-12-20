import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import rectangle

class magicCube:
    def __init__(self):
        # colours: White, Yellow, Red, Orange, Blue, Green
        # moves: Up, Down, Front, Back, Left, Right

        self.faces = {'U': np.array([['W']*3 for _ in range(3)]),
                    'D': np.array([['Y']*3 for _ in range(3)]),
                    'F': np.array([['R']*3 for _ in range(3)]),
                    'B': np.array([['O']*3 for _ in range(3)]),
                    'L': np.arrray([['G']*3 for _ in range(3)]),
                    'R': np.array([['B']*3 for _ in range(3)])}
        
        self.colours = {'W': '#FFFFFF', 'Y': '#FFFF00', 'R': '#FF0000', 'O': '#FF8800', 'B': '#0000FF', 'G': '#00FF00'}

        self.pastMovements = []

    def rotateFaces_clockwise(self ,face):
        self.faces[face] = np.rot90(self.faces[face], -1) #90 degres rotation

    def rotateFaces_counterclockwise(self, face):
        self.faces[face] = np.rot90(self.faces[face], 1)

    def U(self, inverse = False):
        # rotates upper face
        if not inverse:
            self.rotateFaces_clockwise('U')
            temp = self.faces['F'][0].copy()

            self.faces['F'][0] = self.faces['R'][0]
            self.faces['R'][0] = self.faces['B'][0]
            self.faces['B'][0] = self.faces['L'][0]
            self.faces['L'][0] = temp

            self.pastMovements.append("U")
        else:
            self.rotateFaces_counterclockwise('U')
            temp = self.faces['F'][0].copy()

            self.faces['F'][0] = self.faces['L'][0]
            self.faces['L'][0] = self.faces['B'][0]
            self.faces['B'][0] = self.faces['R'][0]
            self.faces['R'][0] = temp

            self.pastMovements.append("U'")

    def D(self, inverse = False):
        # rotates down face
        if not inverse:
            self.rotateFaces_clockwise('D')
            temp = self.faces['F'][2].copy()

            self.faces['F'][2] = self.faces['L'][2]
            self.faces['L'][2] = self.faces['B'][2]
            self.faces['B'][2] = self.faces['R'][2]
            self.faces['R'][2] = temp

            self.pastMovements.append("D")
        else:
            self.rotateFaces_counterclockwise('D')
            temp = self.faces['F'][2].copy()

            self.faces['F'][2] = self.faces['R'][2]
            self.faces['R'][2] = self.faces['B'][2]
            self.faces['B'][2] = self.faces['L'][2]
            self.faces['L'][2] = temp

            self.pastMovements.append("'D'")

    def R(self, inverse = False):
            # rotates right face
        if not inverse:
            self.rotate_face_clockwise('R')
            temp = np.array([self.faces['F'][i][2] for i in range(3)])

            for i in range(3):
                self.faces['F'][i][2] = self.faces['D'][i][2]
                self.faces['D'][i][2] = self.faces['B'][2-i][0]
                self.faces['B'][2-i][0] = self.faces['U'][i][2]
                self.faces['U'][i][2] = temp[i]

            self.pastMovements.append("R")
        else:
            self.rotateFaces_counterclockwise('R')
            temp = np.array([self.faces['F'][i][2] for i in range(3)])

            for i in range(3):
                self.faces['F'][i][2] = self.faces['U'][i][2]
                self.faces['U'][i][2] = self.faces['B'][2-i][0]
                self.faces['B'][2-i][0] = self.faces['D'][i][2]
                self.faces['D'][i][2] = temp[i]

            self.pastMovements.append("R'")

    def L(self, inverse = False):
        # rotates left face
        if not inverse:
            self.rotateFaces_clockwise('L')
            temp = np.array([self.faces['F'][i][0] for i in range(3)])

            for i in range(3):
                self.faces['F'][i][0] = self.faces['D'][i][0]
                self.faces['D'][i][0] = self.faces['B'][2-i][2]
                self.faces['B'][2-i][2] = self.faces['U'][i][0]
                self.faces['U'][i][0] = temp[i]
            self.pastMovements.append("L")
        else:
            self.rotateFaces_counterclockwise('L')
            temp = np.array([self.faces['F'][i][0] for i in range(3)])

            for i in range(3):
                self.faces['F'][i][0] = self.faces['D'][i][0]
                self.faces['D'][i][0] = self.faces['B'][2-i][2]
                self.faces['B'][2-i][2] = self.faces['U'][i][0]
                self.faces['U'][i][0] = temp[i]
            self.pastMovements.append("L'")