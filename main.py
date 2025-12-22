from function import magicCube

def main():
    print("=== RUBIK'S CUBE SIMULATOR 3x3 ===\n")
    
    cube = magicCube()
    
    print("\nScrambling the cube...")
    cube.scramble(15)
    cube.visualize()

    print("\n=== Sumary of moves ===")
    print("U  = Rotate upper face clockwise")
    print("U' = Rotate upper face counterclockwise")
    print("D  = Rotate down face clockwise")
    print("R  = Rotate right face clockwise")
    print("L  = Rotate left face clockwise")
    print("F  = Rotate front face clockwise")
    print("\nAdd ' after the letter for inverse move (e.g., R')")
    
    print("\n=== layer by layer method ===")
    print("1. White cross (U face)")
    print("2. First layer white corners")
    print("3. Second layer (middle edges)")
    print("4. Yellow cross (D face)")
    print("5. Orient yellow cross")
    print("6. Position yellow corners")
    print("7. Orient yellow corners")
    
    print("\nExample of some moves:")
    print("cube.R()   -->    Rotate right")
    print("cube.U(True)  -->   Rotate up counterclockwise")
    print("cube.F()   -->     Rotate front")
    print("cube.visualize()   -->    Show current state")

if __name__ == "__main__":
    main()