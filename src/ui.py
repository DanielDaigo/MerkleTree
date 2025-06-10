from tkinter import Tk, Frame, Label, Entry, Button, Canvas, StringVar, messagebox
from animator import MerkleTreeAnimator

class MerkleTreeAnimatorUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Merkle Tree Animator")
        
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        self.label = Label(self.frame, text="Digite as palavras (separadas por vírgula):")
        self.label.pack()

        self.input_var = StringVar()
        self.input_entry = Entry(self.frame, textvariable=self.input_var, width=50)
        self.input_entry.pack(pady=5)

        self.start_button = Button(self.frame, text="Iniciar Animação", command=self.start_animation)
        self.start_button.pack(pady=10)

        self.canvas = Canvas(self.frame, width=900, height=600, bg="white")
        self.canvas.pack()

        self.animator = MerkleTreeAnimator(self.canvas)

    def start_animation(self):
        input_text = self.input_var.get()
        if not input_text:
            messagebox.showwarning("Input Error", "Por favor, digite algumas palavras.")
            return
        
        words = [word.strip() for word in input_text.split(",") if word.strip()]
        if not words:
            messagebox.showwarning("Input Error", "Por favor, digite algumas palavras válidas.")
            return
        self.animator.animate_merkle_tree(words)

if __name__ == "__main__":
    root = Tk()
    app = MerkleTreeAnimatorUI(root)
    root.mainloop()