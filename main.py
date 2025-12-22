from function import magicCube

def interactive_mode():
    print("=== RUBIK'S CUBE SIMULATOR 3x3 ===\n")
    
    cube = magicCube()
    print("Starting with solved cube...")
    cube.visualize()
    
    print("\n=== AVAILABLE MOVES ===")
    print("U, D, R, L, F, B  = Clockwise rotation")
    print("U', D', R', L', F', B' = Counterclockwise")
    print("\nSpecial commands:")
    print("show     - Visualize current state")
    print("scramble - Scramble the cube")
    print("reset    - Reset to solved state")
    print("history  - Show move history")
    print("quit  -  Exit program")
    print("\nYou can type multiple moves: R U R' U'")
    print("-" * 10)
    
    while True:
        user_input = input("\nEnter move(s): ").strip().upper()
        
        if not user_input:
            continue
            
        if user_input == "QUIT":
            print("Thanks for playing! See you soon! ")
            break
            
        elif user_input == "SHOW":
            cube.visualize()
            
        elif user_input == "SCRAMBLE":
            num = input("How many moves? (default 20): ").strip()
            num = int(num) if num.isdigit() else 20
            cube.scramble(num)
            cube.visualize()
            
        elif user_input == "RESET":
            cube = magicCube()
            print("Cube reset to solved state!")
            cube.visualize()
            
        elif user_input == "HISTORY":
            if cube.move_history:
                print(f"Moves: {' '.join(cube.move_history)}")
            else:
                print("No moves yet!")
        
        else:
            # Process moves
            moves = user_input.split()
            try:
                for move in moves:
                    if move.endswith("'"):
                        face = move[0]
                        if hasattr(cube, face):
                            getattr(cube, face)(inverse=True)
                        else:
                            print(f" Invalid move: {move}")
                    else:
                        face = move[0]
                        if hasattr(cube, face):
                            getattr(cube, face)(inverse=False)
                        else:
                            print(f" Invalid move: {move}")
                
                print(f" Executed: {' '.join(moves)}")
                cube.visualize()
                
            except Exception as e:
                print(f" Error: {e}")

if __name__ == "__main__":
    interactive_mode()