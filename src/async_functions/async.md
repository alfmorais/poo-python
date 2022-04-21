# Conceitos Sobre Concorrência e Programação Assíncrona

Ao executar um programa Python, o que ocorre?

- O interpretador Python cria um processo no sistema operacional.
- O processo Python cria uma **thread** (linha de execução) para executar o código.

"O número de transistores em um circuito integrado irá dobrar a cada 18 meses" Gordon E. Moore. **Lei de Moore**.

Beneficios da **Lei de Moore**:

- Mais baratos
- Menores
- Mais potentes
- Eficientes

Desta forma, por exemplo, para uma aplicação que você desenvolve hoje ser executada mais rápido daqui um ano basta trocar o hardware.

Em 2015 a Lei de Moore se deu um fim. Ao invés de termos cada vez mais transistores em um único circuito integrado formando um único **core**, os circuitos integrados passaram a ter mais processadores se tornando então **multi-cores**.

- Mas o que é Concorrência?

Em Ciência da Computação, **concorrência** é a _execução_ de múltiplas **_instruções sequenciais_** ao mesmo tempo.

Existem dois tipos principais de concorrência:
- Programação Paralela
- Programação Assíncrona

Esta **execução** deve se atentar alguns pontos fundamentais:
- Ordem de execução
- Recursos compartilhados

Ordem de Execução:

1. Instrução 1
2. Instrução 2
3. Instrução 3

Independente de qual instrução for executada não pode alterar o resultado final. Ou seja, se a instrução 3 terminar antes da instrução 2 ou 1, devemos ter o mesmo resultado que se a instrução 1, 2, e 3 ocorresem na sequência.

**Recursos Compartilhados**

A execução deve compartilhar o mínimo de recursos possíveis entre as instruções. Quanto mais recursos forem compartilhados entre as execuções concorrentes, mais coordenação entre as execuções será necessária para garantir o resultado final correto, dificultando o processo.

**Tipos de Concorrência**

Terceiro tipo **Programação Distribuida**.

**Programação Paralela**

- Tarefa computacional
- Quebra a tarefa em pequenas partes
- Executa em multi-cores

Sem o uso da programação paralela, mesmo que seu computador tenha múltiplos cores, a tarefa, por padrão, irá ser executada por inteiro em um único processador. Fazendo com que este tenha sua capacidade elevada até 100% enquanto os outros cores ficam sem uso.

A programação paralela tem sua melhor utilização em tarefas que fazem uso excessivo da CPU.

- Operações em strings
- Algoritmos de busca
- Processamento gráfico
- Algoritmos de Processamento numérico

**Programação Assíncrona**

A programação assíncrona é utilizada em operações de leitura ou escria em dispositivos IO - Input/Output. Ou seja, em operações que podem ser lentas e dependem de um retorno de execução, que pode ser sucesso ou falho.

Em programa, podemos ter *partes* que precisem ser executadas de forma assíncrona. Quando a sub-tarefa assíncrona finaliza a execução a **thread principal** é notificada e faz uso dos resultados, isso é chamado de funções de **call-back**.

Em algumas linguagens de programação, ao invés de utlizar funções call-back são utilizados outros objetos com operações incompletas conhecidos como *promisses*, *futures* ou simplesmente *tarefa(task)*.

A programação assíncrona é melhor utilizada em tarefas que exigem uso intensivo de IO como:

- Leitura ou escrita em banco de dados
- Chamadas à Web Services (APIs)
- Cópia, upload ou download de dados


**Concorrência em Python**

Python não nasceu *concorrente*.

**Python 1.5 +**: Com threading permitiu que pudéssemos usar a linguagem Python para criar threads nativas no sistema operacional podendo executar código de forma concorrente. Um detalhe aqui é que na implementação padrão da linguagem Python, conhecida como **Cpyhton**, as threads estão limitadas com um dispositivo chamado **GIL - Global Interpreter Lock**, fazendo com que o código seja executado em séries e não em paralelo.

**Python 2.6 +**: Com multiprocessing permitiu que pudéssemos usar a linguagem Python para criar subprocessos nativos no sistema operacional ao invés de threads, podendo executar o código de forma concorrente e paralela evitando o problema com GIL.

**Python 3.2 +**: Com concurrent.futures passamos a ter uma implementação abstrada de concorrência permitindo de forma fácil fazer uso (ou alternar) de concorrência usando threads ou multiprocessos.

**Python 3.4 +**: Asyncio passamos finalmente a ter suporte à programação assíncrona.

**GIL - Global Interpreter Lock**

O GIL é um recurso de bloqueio que previne que múltiplas threads nativas executem um código Python ao mesmo tempo.

Isso foi necessário para manter a thread de execução segura, ou seja, não permitindo que outras threads fizessem uso do código ainda em execução de desta forma cauzasse efeitos indesejados no resultado final.

Ao mesmo tempo que este recurso faz com que a execução do código Python em uma thread fosse segura (thread safe), fez com que os programas Python ficassem "presos" à execução em uma thread única (simples) e consequentemente 1 processo.

A razão inicial da criação do GIL em Python é que o gerenciamento interno da memória do interpretador Python não é thread-safe.

Thread-safe é um conceito aplicável no contexto de multi-thread. Um código é conseiderado thread-safe se ele apenas manipula estruturas de dados compartilhados de uma forma que garanta uma execução segura atráves de várias threads ao mesmo tempo.

**Como escapar do GIL?**

A implementação padrão do Python é chamada de cPython mas existem outras, inclusive algumas que não possuem recursos de GIL.

Por exemplo:

- jython, uma implementação da linguagem Python escrita em Java
- IronPython, uma implementação da linguagem Python escrita em C#

Podemos também escapar do GIL fazendo uso de multiprocessos, pois cada thread é executada em um processo separado.