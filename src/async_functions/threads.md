# Threads

Threads (Linha de execução) foram os primeiros recursos criados para realizar **programação concorrente**, fazendo uso então de **multi-threads**.

Para que possamos entender melhor o que são **threads**, precisamos antes compreender o que são **processos**.

*O que são processos?*

O contexto de execução de um programa sendo executado é considerado um processo.

Ou seja, um processo nada mais é do que a instância de um programa de computador sendo executado.

Além disso, cada processo sendo executado tem um conjunto de recursos, como por exemplo memória, segurança e etc, que são atribuídos a este processo.

Por fim, um processo é composto por uma ou mais threads (linhas de execução).

*O que são threads?*

Uma thread, ou linha de execução, é a menor sequência de instruções que pode ser gerenciada pelo sistema operacional.

Um programa pode ser executado por uma simples thread ou por múltiplas threads.

Quando o computador/servidor dispõe de múltiplos cores, cada thread pose ser executado em paralelo. Caso contrário, mesmo que haja múltiplas threads elas serão executadas de forma sequencial.

pacote threading.

```python
import threading

def some_function(param):
    print("Running...")
    print(f"The param is: {param}")

    return param * param


th = threading.Thread(target=some_function, args=(42,))

th.start()
th.join()
```

(Python GIL)[https://realpython.com/python-gil/]