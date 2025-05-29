# 🧠 Exercício com Funções `map`, `filter` e `reduce` em Python

Este projeto demonstra o uso de funções funcionais em Python com o módulo `functools`, aplicando conceitos de **programação funcional** usando `map`, `filter` e `reduce` sobre uma lista de números inteiros.

---

## 📁 Arquivo

- `modulo_functools.py`: Contém a lógica principal com os exemplos de uso de funções funcionais para manipulação de listas.

---

## 🧠 Conhecimentos Abordados

### 🔹 Python
- **Função `map()`** para aplicar uma transformação a todos os elementos de uma lista.
- **Função `filter()`** para selecionar elementos com base em uma condição.
- **Função `reduce()`** (importada de `functools`) para reduzir uma lista a um único valor.
- **Funções com `lambda`** para expressar operações simples.
- Criação de **funções nomeadas** para maior legibilidade e reutilização.

---

## 🔢 O que o código faz?

1. **Eleva ao quadrado** todos os números de 1 a 10 usando `map()`.
2. **Filtra** apenas os números pares da mesma lista com `filter()`.
3. **Soma** todos os elementos da lista com `reduce()`.

---

## 📌 Exemplos de Saída

```python
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]  # Resultado do map
[2, 4, 6, 8, 10]                        # Resultado do filter
55                                     # Resultado do reduce
