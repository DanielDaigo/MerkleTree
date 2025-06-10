# Merkle Tree Animator

Este projeto é uma ferramenta didática para **visualização animada de Árvores de Merkle** usando Python e Tkinter. Ele permite que você digite palavras (transações) e veja, passo a passo, como os nós e hashes são formados até chegar à raiz da árvore, incluindo a visualização de nós clonados quando necessário.

## Funcionalidades

- Interface gráfica simples e intuitiva (Tkinter)
- Animação da construção da árvore de Merkle, nível a nível
- Exibição dos hashes e das palavras originais nas folhas
- Indicação visual de nós clonados (quando o número de folhas é ímpar)
- Destaque visual para a raiz da árvore

## Como executar

1. **Clone o repositório ou baixe os arquivos.**
2. **Crie um ambiente virtual (recomendado):**
   ```sh
   python -m venv venv
   ```
3. **Ative o ambiente virtual:**
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
4. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Execute o programa:**
   ```sh
   python src/main.py
   ```

## Como usar

1. Digite as palavras (transações) separadas por vírgula no campo de entrada.
2. Clique em **"Iniciar Animação"**.
3. Observe a construção animada da árvore de Merkle, com cada nível sendo desenhado e os hashes sendo exibidos.

## Estrutura dos arquivos principais

- `src/main.py` — Ponto de entrada da aplicação.
- `src/ui.py` — Interface gráfica (Tkinter).
- `src/animator.py` — Lógica de animação da árvore.
- `src/merkle_tree.py` — Implementação da árvore de Merkle.
- `src/utils.py` — Funções utilitárias.
- `requirements.txt` — Dependências do projeto.

## Observações

- O projeto utiliza apenas bibliotecas Python padrão e Tkinter, além de algumas dependências para compatibilidade visual.
- O código é didático e pode ser facilmente adaptado para outros tipos de árvores ou visualizações.

---

**Desenvolvido para fins educacionais na disciplina de Estrutura de Dados — Engenharia de Software.**
