def hash_data(data):
    """Calcula o hash SHA-256 de uma string."""
    import hashlib
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def format_hash_display(hash_value):
    """Formata o valor do hash para exibição."""
    return f"{hash_value[:8]}..."

def create_leaf_node(data):
    """Cria um nó folha a partir dos dados de entrada."""
    return {
        'data': data,
        'hash': hash_data(data)
    }

def clone_node(node):
    """Cria um clone de um nó fornecido."""
    return {
        'data': node['data'],
        'hash': node['hash']
    }