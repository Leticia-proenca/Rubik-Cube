import matplotlib
matplotlib.use('TkAgg')  # Force graphical backend

import numpy as np
import matplotlib.pyplot as plt
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

    def _draw_tile_surface(self, ax, normal_axis, fixed_val, u_axis, v_axis, u0, v0, colour):
        """Desenha um tile usando plot_surface com borda preta via edgecolor."""
        S = 1.0
        pts = [(u0,v0),(u0+S,v0),(u0+S,v0+S),(u0,v0+S)]
        xs,ys,zs=[],[],[]
        for cu,cv in pts:
            xyz=[0.0,0.0,0.0]; xyz[normal_axis]=float(fixed_val); xyz[u_axis]=cu; xyz[v_axis]=cv
            xs.append(xyz[0]); ys.append(xyz[1]); zs.append(xyz[2])
        ax.plot_surface(
            np.array([[xs[0],xs[1]],[xs[3],xs[2]]]),
            np.array([[ys[0],ys[1]],[ys[3],ys[2]]]),3
            np.array([[zs[0],zs[1]],[zs[4],zs[2]]]),
            color=colour, shade=False,
            edgecolor='#111111', linewidth=2.0,
            antialiased=False
        )

    def _init_figure(self):
        # cria a figura uma única vez e guarda a referência
        self._fig = plt.figure(figsize=(9, 8), facecolor='#1C1C1E')
        self._ax = self._fig.add_subplot(111, projection='3d', facecolor='#1C1C1E')
        plt.show(block=False)

    def visualize(self):
        # cria a figura se ainda não existir ou se o utilizador a fechou
        if not hasattr(self, '_fig') or not plt.fignum_exists(self._fig.number):
            self._init_figure()

        ax = self._ax
        ax.cla()  # limpa só o conteúdo, mantém a janela aberta
        ax.set_facecolor('#1C1C1E')
        ax.set_axis_off()

        N, S = 3, 1.0

        fwd, bwd = [0,1,2], [2,1,0]

        # ordem de trás para frente segundo azim=-45, elev=30
        for face_name, normal_axis, fixed_val, u_axis, v_axis, ro, co in [
            ('B', 1, N*S, 0, 2, bwd, bwd),  # trás
            ('L', 0, 0,   1, 2, bwd, bwd),  # esquerda
            ('D', 2, 0,   0, 1, bwd, fwd),  # baixo
            ('U', 2, N*S, 0, 1, bwd, fwd),  # topo
            ('F', 1, 0,   0, 2, bwd, fwd),  # frente
            ('R', 0, N*S, 1, 2, bwd, fwd),  # direita
        ]:
            for vi, row in enumerate(ro):
                for ui, col in enumerate(co):
                    colour = self.colours[self.faces[face_name][row][col]]
                    self._draw_tile_surface(ax, normal_axis, fixed_val, u_axis, v_axis, ui*S, vi*S, colour)

        ax.set_xlim(0, N*S)
        ax.set_ylim(0, N*S)
        ax.set_zlim(0, N*S)
        ax.set_box_aspect([1, 1, 1])
        ax.view_init(elev=30, azim=-45)

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

        self._fig.canvas.draw()
        self._fig.canvas.flush_events()
        plt.pause(0.001)
