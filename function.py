import matplotlib
matplotlib.use('TkAgg')  # Force graphical backend

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import matplotlib.patches as mpatches

class magicCube:
    def __init__(self):
        # colours: White, Yellow, Red, Orange, Blue, Green
        # moves: Up, Down, Front, Back, Left, Right

        self.faces = {'U': np.array([['W']*3 for _ in range(3)]),
                    'D': np.array([['Y']*3 for _ in range(3)]),
                    'F': np.array([['R']*3 for _ in range(3)]),
                    'B': np.array([['O']*3 for _ in range(3)]),
                    'L': np.array([['G']*3 for _ in range(3)]),
                    'R': np.array([['B']*3 for _ in range(3)])}
        
        self.colours = {'W': '#FFFFFF', 'Y': '#FFFF00', 'R': '#FF0000', 'O': '#FF8800', 'B': '#0000FF', 'G': '#00FF00'}

        self.pastMovements = []

    def rotateFaces_clockwise(self, face):
        self.faces[face] = np.rot90(self.faces[face], -1) #90 degres rotation

    def rotateFaces_counterclockwise(self, face):
        self.faces[face] = np.rot90(self.faces[face], 1)

    def U(self, inverse=False):
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

    def D(self, inverse=False):
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

            self.pastMovements.append("D'")

    def R(self, inverse=False):
        # rotates right face
        if not inverse:
            self.rotateFaces_clockwise('R')
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

    def L(self, inverse=False):
        # rotates left face
        if not inverse:
            self.rotateFaces_clockwise('L')
            temp = np.array([self.faces['F'][i][0] for i in range(3)])

            for i in range(3):
                self.faces['F'][i][0] = self.faces['U'][i][0]
                self.faces['U'][i][0] = self.faces['B'][2-i][2]
                self.faces['B'][2-i][2] = self.faces['D'][i][0]
                self.faces['D'][i][0] = temp[i]
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

    def F(self, inverse=False):
        # rotates front face
        if not inverse:
            self.rotateFaces_clockwise('F')
            temp = self.faces['U'][2].copy()
            self.faces['U'][2] = np.array([self.faces['L'][2-i][2] for i in range(3)])
            for i in range(3):
                self.faces['L'][i][2] = self.faces['D'][0][i]
            self.faces['D'][0] = np.array([self.faces['R'][2-i][0] for i in range(3)])
            for i in range(3):
                self.faces['R'][i][0] = temp[i]
            self.pastMovements.append("F")
        else:
            self.rotateFaces_counterclockwise('F')
            temp = self.faces['U'][2].copy()
            temp_R = np.array([self.faces['R'][i][0] for i in range(3)])
            temp_D = self.faces['D'][0].copy()
            temp_L = np.array([self.faces['L'][i][2] for i in range(3)])
            
            for i in range(3):
                self.faces['U'][2][i] = temp_R[i]
                self.faces['R'][i][0] = temp_D[2-i]
                self.faces['D'][0][i] = temp_L[i]
                self.faces['L'][i][2] = temp[2-i]
            self.pastMovements.append("F'")

    def B(self, inverse=False):
        # rotates back face
        if not inverse:
            self.rotateFaces_clockwise('B')
            temp = self.faces['U'][0].copy()
            
            for i in range(3):
                self.faces['U'][0][i] = self.faces['R'][i][2]
            
            for i in range(3):
                self.faces['R'][i][2] = self.faces['D'][2][2-i]
            
            for i in range(3):
                self.faces['D'][2][i] = self.faces['L'][i][0]
            
            for i in range(3):
                self.faces['L'][i][0] = temp[2-i]
            
            self.pastMovements.append("B")
        else:
            self.rotateFaces_counterclockwise('B')
            temp = self.faces['U'][0].copy()
            
            for i in range(3):
                self.faces['U'][0][i] = self.faces['L'][2-i][0]
            
            for i in range(3):
                self.faces['L'][i][0] = self.faces['D'][2][i]
            
            for i in range(3):
                self.faces['D'][2][i] = self.faces['R'][2-i][2]
            
            for i in range(3):
                self.faces['R'][i][2] = temp[i]
            
            self.pastMovements.append("B'")

    def scramble(self, num_moves=20):
        moves = ['U', 'D', 'R', 'L', 'F', 'B']

        for _ in range(num_moves):
            move = np.random.choice(moves)
            inverse = np.random.choice([True, False])
            getattr(self, move)(inverse)

        print(f"The cube is scrambled with {num_moves} moves!")
        print(f"Sequence: {' '.join(self.pastMovements[-num_moves:])}")

    #visualization

    def _iso(self, x, y, z):
        sx = (x -y)*np.cos(np.radians(30))
        sy = (x + y)*np.sin(np.radians(30)) + z

        return sx, sy
    
    def _draw_tile(self, ax, corners_3d, colour, edge_colour='#1a1a1a', lw = 1.2, zorder = 1):
        pts = np.array ([self._iso(*c) for c in corners_3d])
        poly = Polygon(pts, closed = True,
                    facecolor = colour,
                    edgecolor = edge_colour,
                    linewidth = lw,
                    zorder = zorder)
        ax.add_patch(poly)

    def _draw_face_outline(self, ax, corners_3d, zorder = 2):
        pts = np.array([self.iso(*c) for c in corners_3d])
        poly = Polygon(pts, closed = True,
                    facecolor = 'none',
                    edgecolor = '#111111' ,
                    linewidth = 2.8,
                    zorder = zorder)
        ax.add_patch(poly)

    def visualize(self):
        plt.close('all')

        fig, ax = plt.subplots(figsize =(9, 8), facecolor = '#1C1C1E')

        ax.set_facecolor('#1C1C1E')
        ax.set_aspect('equal')
        ax.axis('off')

        N = 3
        S = 1.0

        for row in range(N):
            for col in range(N):
                # x grows right (R direction), y grows into screen (B direction)
                x0 = col * S
                y0 = (N - 1 - row) * S
                z0 = N * S

                corners = [
                    (x0,       y0,       z0),
                    (x0 + S,   y0,       z0),
                    (x0 + S,   y0 + S,   z0),
                    (x0,       y0 + S,   z0),]
                
                colour_key = self.faces['U'][row][col]
                self._draw_facelet(ax, corners, zorder=3)

            self._draw_face_outline(ax, [
            (0,   0,   N*S),
            (N*S, 0,   N*S),
            (N*S, N*S, N*S),
            (0,   N*S, N*S),],
            zorder=4)

        for row in range(N):
            for col in range(N):
                x0 = col * S
                y0 = 0
                z0 = (N - 1 - row) * S
                corners = [
                    (x0,     y0, z0),
                    (x0 + S, y0, z0),
                    (x0 + S, y0, z0 + S),
                    (x0,     y0, z0 + S),]
                
                colour_key = self.faces['F'][row][col]
                self._draw_facelet(ax, corners, zorder=3)

            self._draw_face_outline(ax, [
                (0,   0, 0),
                (N*S, 0, 0),
                (N*S, 0, N*S),
                (0,   0, N*S),],
                zorder=4)
            
        for row in range(N):
            for col in range(N):
                x0 = N * S
                y0 = col * S
                z0 = (N - 1 - row) * S
                corners = [
                    (x0, y0,     z0),
                    (x0, y0 + S, z0),
                    (x0, y0 + S, z0 + S),
                    (x0, y0,     z0 + S),]
                colour_key = self.faces['R'][row][col]
                self._draw_facelet(ax, corners, zorder=3)

            self._draw_face_outline(ax, [
                (N*S, 0,   0),
                (N*S, N*S, 0),
                (N*S, N*S, N*S),
                (N*S, 0,   N*S),],
                zorder=4)
                

        legend_items = [
        mpatches.Patch(facecolor=v, edgecolor='#555', label=k)
        for k, v in self.colours.items()]
        ax.legend(handles=legend_items, loc='lower left',
        ncol=6, fontsize=9,
        framealpha=0.25, facecolor='#333',
        edgecolor='#555', labelcolor='white',
        handlelength=1.2, handleheight=1.2,
        bbox_to_anchor=(0.0, -0.04))

#past movements
        if self.pastMovements:
            history_str = "  ".join(self.pastMovements[-15:])
            if len(self.pastMovements) > 15:
                history_str = "… " + history_str
                ax.set_xlabel(f"Moves: {history_str}",
                    color='#aaaaaa', fontsize=9, labelpad=12)
    
#title of the game
        ax.set_title("Rubik's Cube 3×3  —  3D view  (U · F · R)",
            color='white', fontsize=14, fontweight='bold', pad=14)
    
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.001)
