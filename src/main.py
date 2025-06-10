from tkinter import Tk
from ui import MerkleTreeAnimatorUI

def main():
    # Initialize the main application window
    root = Tk()
    root.title("Merkle Tree Animator")
    
    # Create the user interface
    app = MerkleTreeAnimatorUI(root)
    
    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()