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

Ciclo de vida das Threads

- New
- Ready
- Running
- Blocked
- Terminated

Em programa com múltiplas threads, cada threads tem seu próprio registrador e pilha de execução.
Porém, uma thread pode ler ou modificar os dados de qualquer outra thread que faz parte de um mesmo processo.

**Agendador (Scheduler)**

Sistemas operacionais possuem um módulo que seleciona as próximas tarefas a serem admitidas no sistema e desta forma o próximo processo a ser executado.

Ou seja, quanto um processo é executado, o sistema operacional utiliza um algoritmo* de escalonamento de processos que organiza e gerencia os novos processos. Este algoritmo possui um agendador, chamado de *scheduler* que controla quando um processo ou thread irá executar e por quanto tempo.

Conforme vimos no ciclo de vida das threads, uma thread pode *navegar* pelos estados de *ready, running e blocked* até ser terminada.

*O algoritmo de escalonamento difere de acordo com o sistema operacional utilizado. Desta forma a perfomance de execução de processos e threads é diferente de acordo com o sistema operacional.

Quando o agendador alterna entre uma thread e outra para execução ele faz isso usando um recurso chamado de *context switch* que salva e restaura o estado da thread ou processo.

OBS: Quando o agendador faz uso do *context switch* e o que está sendo alternado é uma thread pertecente a um mesmo processo é gasto menos recursos do processador. Quando o que é alternado é uma thread pertecente a outro processo ou mesmo um outro processo, o processador gasta muito mais recursos.

Isso significa que, teoricamente, criar programas multi-threads deveriam performar melhor se comparado com multi-processos. Porém ao fazer uso de multi-threads podemos nos deparar facilmente com um problema de interferência de threads, conhecida como *race conditions*. Que é um processo de uma thread interferir nos resultados de outras.

Sincronização de Threads

Quando trabalhamos com multi-threads é recomendável que tentemos manter o minimo possivel de recursos compartilhados entre as threads.

Ou seja, evite que uma thread dependa de dados ou recursos que outra thread possa manipular.

Quanto maior o nível de compartilhamento dde recursos/dados/memória através de threads que houver no seu programa, mais complexo será o gerenciamento e resultados inesperados certamente ocorrerão.

Para ajudar a contornar os problemas de interferência em threads (race conditions), existem diversos mecanismos que nos ajudam a controlar o acesso a determinado recurso por uma thread.

**Lock**

O lock, é um recurso de bloqueio. OU seja, usamos para que thread bloqueie o acesso a determinado recurso.

- Unlock
- Lock

Quando uam thread realiza um lock em um recurso ela faz com que nenhuma outra thread tenha acesso a este recurso.

Além disso a única thread que pode realizar um unlock é ela mesma.

Uma thread adquire um lock com o método acquire() e realiza um unlock com o método release()

Um programa que temos aqui é que caso ocorra alguma exceção durante as ações efetuadas com o acquire(), o método release() nunca será executado, e desta forma o recurso continuará bloqueado.

Conseguimos resolver este problema facilmente realizando o tratamento da possivel exceção e executando o método release() na cláusula *finally*.

Podemos ainda fazer uso dos gerenciados re contexto, como o *with*, para que os métodos acquire() e release() sejam executados automaticamente ao entrar no bloco do contexto e ao sair dele.

Lembre-se que se uma thread tentar acessar um recurso que está bloqueado por outra thread não terá acesso e desta forma ficará aguardando o recurso a ser liberado para poder trabalhar.

Você pode não querer ficar aguardando. Por exemplo poderá fazer outra coisa e depois voltar ao recurso para ver se ele já foi liberado.

Utilize sempre o **RLock** que faz as mesmas coisas que o lock mais não bloqueia sua própria thread em caso de tentativa de adquirir lock em um recurso que já está bloqueado pela própria thread.
