import time
from merkle_tree import MerkleTree

class MerkleTreeAnimator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.tree = None

    def animate_merkle_tree(self, words):
        # Cria a árvore de Merkle a partir das palavras fornecidas
        self.tree = MerkleTree(words)
        self.canvas.delete("all")
        node_positions = []

        # Desenha as folhas
        leaf_y = 500
        leaf_x_start = 60
        leaf_x_gap = 120
        leaf_positions = []
        for i, leaf_hash in enumerate(self.tree.get_leaf_hashes()):
            x = leaf_x_start + i * leaf_x_gap
            y = leaf_y
            # Mostra a palavra original ou indica que é um clone
            if i < len(words):
                label = words[i]
            else:
                label = f"clone de: {words[-1]}"
            self._draw_node(x, y, leaf_hash, fill='lightblue', label=label, font_size=10)
            leaf_positions.append((x + 50, y + 15))
            self.canvas.update()
            time.sleep(0.7)
        node_positions.append(leaf_positions)

        # Desenha os níveis intermediários da árvore
        for level_idx, level in enumerate(self.tree.get_levels()[1:]):
            level_positions = []
            y = leaf_y - (level_idx + 1) * 80
            x_gap = leaf_x_gap * (2 ** level_idx)
            for i, node_hash in enumerate(level):
                x = leaf_x_start + i * x_gap
                self._draw_node(x, y, node_hash, fill='lightgreen', font_size=10)
                # Liga aos filhos
                child1_idx = i * 2
                child2_idx = i * 2 + 1
                if child1_idx < len(node_positions[-1]):
                    self._draw_edge(node_positions[-1][child1_idx], (x + 50, y + 15))
                if child2_idx < len(node_positions[-1]):
                    self._draw_edge(node_positions[-1][child2_idx], (x + 50, y + 15))
                level_positions.append((x + 50, y + 15))
                self.canvas.update()
                time.sleep(0.7)
            node_positions.append(level_positions)

        # Destaca a raiz da árvore
        if node_positions and node_positions[-1]:
            x, y = node_positions[-1][0][0] - 50, node_positions[-1][0][1] - 15
            self._draw_node(x, y, self.tree.get_root(), fill='lightcoral', outline='red', width=3, label="Raiz", font_size=12)
            self.canvas.update()

    def _draw_node(self, x, y, hash_value, fill='white', outline='black', width=1, label=None, font_size=10):
        # Desenha um nó (retângulo) com o hash e, se houver, o rótulo
        self.canvas.create_rectangle(x, y, x + 100, y + 30, fill=fill, outline=outline, width=width)
        self.canvas.create_text(x + 50, y + 15, text=hash_value[:8] + "...", font=("Arial", font_size, "bold"))
        if label:
            self.canvas.create_text(x + 50, y - 18, text=label, fill="gray", font=("Arial", font_size, "bold"))

    def _draw_edge(self, child_pos, parent_pos):
        # Desenha uma linha (aresta) entre um nó filho e seu pai
        self.canvas.create_line(child_pos[0], child_pos[1], parent_pos[0], parent_pos[1], arrow="last")