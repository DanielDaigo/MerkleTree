import hashlib

class MerkleTree:
    def __init__(self, transactions):
        # Salva as transações originais
        self.transactions = transactions
        # Lista de níveis da árvore (cada nível é uma lista de hashes)
        self.levels = []
        # Constrói a árvore ao inicializar
        self.build_tree()

    def hash_data(self, data):
        # Calcula o hash SHA-256 de uma string
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    def build_tree(self):
        # Constrói a árvore de Merkle e armazena os níveis
        if not self.transactions:
            return

        # Primeiro nível: folhas (hash das transações)
        current_level_hashes = [self.hash_data(tx) for tx in self.transactions]
        self.levels.append(current_level_hashes)

        # Constrói os próximos níveis até chegar à raiz
        while len(current_level_hashes) > 1:
            next_level_hashes = []
            # Se o número de nós for ímpar, clona o último nó
            if len(current_level_hashes) % 2 != 0:
                current_level_hashes.append(current_level_hashes[-1])

            # Para cada par de nós, calcula o hash do pai
            for i in range(0, len(current_level_hashes), 2):
                combined_hash_input = current_level_hashes[i] + current_level_hashes[i + 1]
                parent_hash = self.hash_data(combined_hash_input)
                next_level_hashes.append(parent_hash)

            self.levels.append(next_level_hashes)
            current_level_hashes = next_level_hashes

    def get_root(self):
        # Retorna a raiz da árvore de Merkle
        if self.levels:
            return self.levels[-1][0]
        return None

    def get_levels(self):
        # Retorna todos os níveis da árvore de Merkle
        return self.levels

    def get_leaf_hashes(self):
        # Retorna os hashes das folhas da árvore de Merkle
        return self.levels[0] if self.levels else []