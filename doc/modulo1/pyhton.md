---
layout: default
title: Introdução ao Pyhton
nav_order: 2
---

# Introdução ao Pyhton

**Objetivos:**

- Compreender o que é Python e como ele se destaca entre outras linguagens de
  programação.
- Configurar o ambiente de desenvolvimento para Python.
- Executar scripts básicos em Python.

## História e Evolução do Python

Python é uma linguagem de programação de alto nível que foi criada por Guido van
Rossum no final dos anos 1980 e lançada pela primeira vez em 1991. O nome da
linguagem foi inspirado no grupo de comédia britânico "Monty Python's Flying
Circus", do qual Van Rossum era fã, e não no réptil, como muitos podem imaginar.

### **Origens e Motivação**

A criação do Python surgiu da necessidade de uma linguagem de programação mais
intuitiva, que fosse fácil de aprender e de usar, especialmente para iniciantes,
mas que ainda fosse poderosa o suficiente para desenvolvedores experientes. Guido
van Rossum, enquanto trabalhava no Centrum Wiskunde & Informatica (CWI) em
Amsterdã, estava insatisfeito com as opções disponíveis na época, especialmente
com a linguagem ABC, que, embora fosse fácil de aprender, tinha limitações
significativas. Inspirado por essa experiência, ele decidiu criar uma nova
linguagem que fosse uma combinação da simplicidade do ABC com a versatilidade e
extensibilidade de linguagens como C.

### **Primeira Versão: Python 1.0 (1991)**

Python 1.0 foi lançado em janeiro de 1991. Desde o início, a linguagem foi
projetada para ter uma sintaxe clara e legível, com ênfase na legibilidade do
código. Python incluía recursos avançados para a época, como exceções, funções e
módulos, que permitiam a reutilização de código. Uma das características
marcantes do Python desde o início foi seu uso de indentação para definir blocos
de código, ao contrário de chaves `{}` ou palavras-chave como `end`, usadas em
outras linguagens. Isso forçou os programadores a escreverem código limpo e bem
estruturado, algo que se tornaria uma das marcas registradas da linguagem.

### **Evolução e Crescimento: Python 2.x**

Python 2.0, lançado em 2000, trouxe uma série de melhorias significativas e novos
recursos que ajudaram a consolidar a linguagem como uma ferramenta poderosa e
flexível para o desenvolvimento de software. Entre os novos recursos estavam a
introdução do coletor de lixo (garbage collection) para gerenciamento automático
de memória e as compreensões de listas, que permitiam criar listas de maneira
concisa e eficiente. Python 2.0 também foi a primeira versão a ser desenvolvida de
forma aberta, com contribuições de desenvolvedores de todo o mundo, marcando o
início de Python como um projeto comunitário.

Apesar do sucesso do Python 2.x, a linguagem tinha algumas limitações e
inconsistências que foram herdadas das versões anteriores. Isso levou à decisão
de criar uma versão completamente nova da linguagem, que corrigisse
esses problemas e preparasse o Python para o futuro.

### **A Revolução: Python 3.x**

Python 3.0 foi lançado em dezembro de 2008 e representou uma ruptura significativa
com as versões anteriores, introduzindo mudanças incompatíveis com o Python 2.x. A
principal motivação para o Python 3 foi eliminar redundâncias e corrigir erros de
design da linguagem, mesmo que isso significasse quebrar a compatibilidade com o
código existente. Algumas das principais mudanças incluíram:

- **Print como função**: Em Python 2.x, `print` era uma declaração, mas em Python
  3.x, tornou-se uma função, o que permitiu maior flexibilidade.
- **Strings Unicode**: Em Python 3, todas as strings passaram a ser Unicode por
  padrão, refletindo a importância crescente do suporte a idiomas globais e
  caracteres especiais.
- **Divisão Inteira**: A divisão entre inteiros em Python 3 passou a produzir um
  número de ponto flutuante por padrão, corrigindo uma fonte comum de erros em
  Python 2.

Embora a transição para o Python 3 tenha sido lenta, devido à necessidade de
atualizar uma grande quantidade de código legado, o Python 3.x eventualmente se
tornou o padrão da indústria, com a última versão do Python 2 (Python 2.7) sendo
oficialmente descontinuada em janeiro de 2020.

### **Python Hoje**

Hoje, Python é uma das linguagens de programação mais populares e amplamente
utilizadas no mundo, especialmente nas áreas de ciência de dados, inteligência
artificial, desenvolvimento web, automação, e muito mais. Seu sucesso se deve em
grande parte à sua comunidade vibrante e ativa, que contribui constantemente para
a melhoria e expansão da linguagem, criando uma vasta quantidade de bibliotecas e
_frameworks_ que facilitam o desenvolvimento de praticamente qualquer tipo de
aplicação.

Python continua a evoluir sob a liderança de um comitê de desenvolvedores,
mantendo-se fiel à sua filosofia original de simplicidade e legibilidade, ao mesmo
tempo que incorpora novos recursos para atender às necessidades crescentes da
comunidade de desenvolvedores.

A história do Python é um exemplo fascinante de como uma linguagem de programação
pode crescer e se adaptar ao longo do tempo, permanecendo relevante e útil em um
campo em constante mudança.

## Aplicações do Python em Diferentes Indústrias

Python é uma linguagem de programação extremamente versátil e amplamente adotada
em diversas indústrias devido à sua simplicidade, poder e uma vasta coleção de
bibliotecas e frameworks. Aqui estão algumas das principais indústrias onde o
Python se destaca:

### **1. Ciência de Dados e Análise**

Uma das áreas onde Python é mais proeminente é na ciência de dados e análise.
Com bibliotecas como **Pandas**, **NumPy** e **Matplotlib**, Python permite a
manipulação de grandes volumes de dados, análise estatística e visualização de
dados de forma eficiente. Além disso, **Jupyter Notebooks** são amplamente
utilizados por cientistas de dados para criar relatórios interativos e protótipos
rápidos de análises.

### **2. Inteligência Artificial e Aprendizado de Máquina**

Python é a linguagem preferida para o desenvolvimento de algoritmos de
inteligência artificial (IA) e aprendizado de máquina (ML). Frameworks como
**TensorFlow**, **Keras** e **PyTorch** simplificam a criação de modelos complexos
de IA. Python é usado em aplicações que vão desde reconhecimento de imagem e
processamento de linguagem natural até veículos autônomos e sistemas de
recomendação.

### **3. Desenvolvimento Web**

No desenvolvimento web, Python é altamente valorizado por sua rapidez e eficiência.
Frameworks como **Django** e **Flask** permitem a criação de aplicações Web robustas
e escaláveis. Python é utilizado tanto no desenvolvimento de back-end quanto no
desenvolvimento full-stack, sendo popular em startups e grandes empresas como
**Instagram** e **Spotify**.

### **4. Automação e Scripting**

Python é frequentemente usado para automatizar tarefas repetitivas, como
manipulação de arquivos, scraping de dados da web e automação de processos de TI.
Ferramentas como **Selenium** permitem a automação de testes de software, enquanto
scripts Python podem ser usados para gerenciar servidores, realizar backups
automáticos e muito mais.

### **5. Finanças e Fintech**

No setor financeiro, Python é utilizado para desenvolver sistemas de trading
algorítmico, análise de risco e gestão de portfólios. Sua capacidade de
processamento de grandes volumes de dados e a disponibilidade de bibliotecas como
**QuantLib** tornam Python ideal para aplicações de fintech e análise financeira.

### **6. Saúde e Biotecnologia**

Python também tem uma presença crescente na indústria de saúde e biotecnologia.
É usado em bioinformática para análise de sequências de DNA e RNA, modelagem de
proteínas e simulações de processos biológicos. Ferramentas como **Biopython**
facilitam a manipulação de dados biológicos, enquanto Python é empregado na
desenvolvimento de aplicações médicas e sistemas de diagnóstico.

### **7. Educação**

Python é amplamente utilizado em educação devido à sua simplicidade e fácil
aprendizado. Muitas escolas e universidades usam Python para ensinar programação,
matemática, e ciência da computação. Além disso, plataformas de educação online
como **Coursera** e **edX** oferecem cursos em Python, reforçando sua importância
como uma linguagem de ensino.

## Comparação com Outras Linguagens de Programação (Java, C++, JavaScript)

Python é frequentemente comparado a outras linguagens de programação populares,
como Java, C++, e JavaScript, cada uma com suas próprias características, pontos
fortes e fracos. Aqui está uma análise comparativa:

### **Python vs. C++**

**Complexidade:**
C++ é uma linguagem poderosa, mas sua complexidade e curva de aprendizado são
altas, devido ao gerenciamento manual de memória, ponteiros, e múltiplos paradigmas
de programação. Python abstrai muitas dessas complexidades, oferecendo uma
sintaxe limpa e menos propensa a erros.

**Desempenho:**
C++ supera Python em termos de desempenho bruto, especialmente em aplicações que
exigem processamento intensivo, como jogos e sistemas embutidos. Python, apesar
de ser mais lento, pode ser usado junto com C++ em áreas críticas de performance,
usando bindings como **Cython** ou **Boost.Python**.

**Flexibilidade:**
Python é mais flexível e fácil de usar para desenvolvimento rápido, enquanto C++
é a escolha certa quando o controle detalhado sobre os recursos do sistema é
necessário. C++ é comum em aplicações que exigem alta performance, como motores
de jogos, sistemas operacionais e software de tempo real.

### **Python vs. Java**

**Simplicidade e Sintaxe:**
Python é conhecido por sua sintaxe simples e clara, que permite escrever código
com menos linhas do que em Java. Java, por outro lado, exige mais verbosidade,
especialmente devido à sua natureza fortemente tipada e ao uso extensivo de
declarações de tipos e modificadores de acesso.

**Desempenho:**
Java tende a ser mais rápido em execução do que Python, graças à compilação em
bytecode e à otimização pelo JVM (Java Virtual Machine). Python é interpretado, o
que geralmente o torna mais lento, embora otimizações e o uso de compiladores
como PyPy possam melhorar sua performance.

**Usabilidade:**
Python é excelente para prototipagem rápida e desenvolvimento ágil, enquanto Java
é preferido em aplicações de grande escala, onde a robustez e a manutenção são
cruciais. Java é amplamente usado em sistemas corporativos, bancos, e aplicações
Android, enquanto Python domina em ciência de dados, automação e IA.

### **Python vs. JavaScript**

**Uso Principal:**
Python é uma linguagem de uso geral, com forte presença em _back-end_, ciência de
dados, e automação. JavaScript, em contraste, é a linguagem padrão para
desenvolvimento front-end web, rodando diretamente no navegador. No entanto, com
a chegada do **Node.js**, JavaScript também se tornou uma opção popular para
_back-end_.

**Sintaxe e Paradigmas:**
Python adota uma sintaxe mais tradicional e é multi-paradigma, suportando
programação orientada a objetos, funcional, e procedural. JavaScript,
originalmente uma linguagem de script, evoluiu para suportar também esses
paradigmas, mas sua herança prototípica e algumas peculiaridades de design, como
o manejo de `this`, podem ser confusas para iniciantes.

**Para saber mais - programação funcional:**
A programação funcional é um estilo de programação onde você foca em criar
funções que transformam dados de maneira previsível, sem modificar os dados
originais. Imagine que você está fazendo uma salada de frutas: em vez de cortar
todas as frutas na mesma tigela e misturar, você corta cada fruta separadamente
e as combina no final. Assim, cada passo é independente e não altera as frutas
originais.

Na programação funcional, cada função faz uma tarefa específica, como cortar uma
fruta, e devolve um novo resultado sem mudar o que estava lá antes. Isso torna
o código mais fácil de entender, porque cada função faz exatamente o que foi
programada para fazer, sem surpresas. Linguagens como Haskell, Lisp e Python
suportam esse estilo com ferramentas que permitem transformar e processar dados
de maneira clara e organizada.

**Ecossistema e Ferramentas:**
Python tem um rico ecossistema de bibliotecas para diversas áreas, enquanto
JavaScript domina o desenvolvimento web com frameworks como **React**,
**Angular**, e **Vue.js**. Python é preferido fora do ambiente web, enquanto
JavaScript é indispensável para qualquer desenvolvedor web.

## Instalando Python no Windows, macOS ou Linux

Instalar Python é o primeiro passo para começar a programar. Aqui está um guia
simples para instalação nos três sistemas operacionais mais comuns: Windows,
macOS e Linux.

### **Instalando no Windows**

1. **Baixar o Python**: Acesse o site oficial do Python (python.org) e baixe a
   versão mais recente. Escolha o instalador para Windows.
2. **Executar o Instalador**: Durante a instalação, marque a opção "Add Python to
   PATH" para facilitar o uso do Python no terminal. Clique em "Install Now" e
   siga as instruções na tela.
3. **Verificação**: Abra o Prompt de Comando e digite `python --version` para
   verificar se a instalação foi bem-sucedida.

### **Instalando no macOS**

1. **Usar o Homebrew (opção recomendada)**: Se você tem o Homebrew instalado,
   abra o Terminal e digite `brew install python`. Isso instalará a versão mais
   recente do Python.
2. **Baixar do site**: Alternativamente, você pode baixar o instalador do site
   oficial do Python. Execute o instalador e siga as instruções.
3. **Verificação**: No Terminal, digite `python3 --version` para confirmar a
   instalação.

### **Instalando no Linux**

1. **Usar o Gerenciador de Pacotes**: A maioria das distribuições Linux já vem
   com Python instalado. Para garantir que você tem a versão mais recente, abra o
   terminal e digite `sudo apt-get install python3` (para distribuições baseadas
   em Debian/Ubuntu) ou `sudo yum install python3` (para Red Hat/Fedora).
2. **Verificação**: Após a instalação, verifique com `python3 --version` no
   terminal.

## Configurando o VS Code para Python

O Visual Studio Code (VS Code) é um editor de código leve e poderoso, ideal para
desenvolvimento em Python. A seguir, veja como configurar o VS Code para trabalhar
com Python:

### **1. Instalar o VS Code**

- Baixe o VS Code no [site oficial](https://code.visualstudio.com/) e instale-o em seu
  sistema operacional (Windows, macOS ou Linux). A instalação é simples e direta.

### **2. Instalar a Extensão Python**

- Abra o VS Code e vá para a aba de extensões clicando no ícone de quadrados na
  barra lateral esquerda ou usando o atalho `Ctrl+Shift+X`.
- Na barra de pesquisa, digite "Python" e instale a extensão oficial da Microsoft
  (Python).

### **3. Configurar o Ambiente Python**

- Selecione o ambiente Python que você deseja usar. Pressione `Ctrl+Shift+P` para
  abrir a paleta de comandos, digite "Python: Select Interpreter" e escolha a
  versão do Python instalada em sua máquina.
- Se você usa um ambiente virtual, certifique-se de ativá-lo antes de iniciar o
  VS Code, ou configure o caminho do interpretador no arquivo `.vscode/settings.json`.

### **4. Instalar o Linting e Formatação**

- O VS Code oferece suporte a linting (análise de código) e formatação. Para
  habilitar o linting, certifique-se de que o `pylint` ou outro linter esteja
  instalado (`pip install pylint`).
- Para formatação automática, instale o `autopep8` ou `black` (`pip install black`
  ou `pip install autopep8`) e configure a formatação na extensão Python.

### **5. Configurar o Debugger**

- O VS Code vem com um depurador integrado para Python. Para começar a depurar,
  coloque pontos de interrupção (breakpoints) clicando na margem ao lado do número
  da linha. Pressione `F5` para iniciar a depuração.

### **6. Testar a Configuração**

- Crie um arquivo `hello.py` e adicione `print("Hello, Python!")`. Execute o código
  usando `F5` ou clicando em "Run Python File" na barra superior. Se tudo estiver
  configurado corretamente, você verá a saída no terminal integrado.

## Configurando um Ambiente Virtual com `venv` ou `virtualenv`

Um ambiente virtual é uma maneira de isolar dependências de projetos Python,
evitando conflitos entre pacotes. Isso é especialmente útil quando você trabalha
em vários projetos que requerem diferentes versões de pacotes. Veja como criar e
usar ambientes virtuais com `venv` ou `virtualenv`:

### **1. Usando `venv` (Python 3.x)**

`venv` é uma ferramenta padrão do Python 3.x para criar ambientes virtuais.

1. **Criar um Ambiente Virtual:**
   - Navegue até a pasta do seu projeto no terminal.
   - Digite `python3 -m venv nome_do_ambiente`, onde `nome_do_ambiente` é o nome
     que você quer dar ao ambiente virtual (ex.: `env`).

2. **Ativar o Ambiente Virtual:**
   - No Windows: `.\nome_do_ambiente\Scripts\activate`
   - No macOS/Linux: `source nome_do_ambiente/bin/activate`
   - Após ativar, você verá o nome do ambiente entre parênteses no início da
     linha do terminal.

3. **Instalar Pacotes:**
   - Com o ambiente ativo, use `pip install nome_do_pacote` para instalar pacotes
     que serão isolados nesse ambiente virtual.

4. **Desativar o Ambiente:**
   - Para desativar o ambiente, digite `deactivate` no terminal.

### **2. Usando `virtualenv` (Python 2.x ou 3.x)**

`virtualenv` funciona de maneira semelhante ao `venv`, mas precisa ser instalado
separadamente e oferece compatibilidade com Python 2.x.

1. **Instalar o `virtualenv`:**
   - Instale com `pip install virtualenv`.

2. **Criar um Ambiente Virtual:**
   - Navegue até a pasta do seu projeto e digite `virtualenv nome_do_ambiente`.

3. **Ativar o Ambiente Virtual:**
   - No Windows: `.\nome_do_ambiente\Scripts\activate`
   - No macOS/Linux: `source nome_do_ambiente/bin/activate`

4. **Instalar Pacotes e Desativar:**
   - O processo é o mesmo descrito para `venv`.

## **3. Configuração Adicional**

- **Requisitos de Pacotes:**
  Crie um arquivo `requirements.txt` com `pip freeze > requirements.txt` para
  listar todas as dependências do projeto. Isso facilita a instalação em outro
  ambiente com `pip install -r requirements.txt`.

## Executando o Primeiro Script Python: `print("Hello, World!")`

O primeiro passo para começar a programar em Python é criar e executar um script
simples. Um exemplo clássico é o programa que exibe a mensagem "Hello, World!"
na tela. Vamos ver como fazer isso em diferentes sistemas operacionais.

### **1. Criando o Script**

1. **Abra um editor de texto ou IDE:**
   - Use um editor de texto simples como Notepad (Windows) ou TextEdit (macOS)
     ou, preferencialmente, uma IDE como VS Code ou PyCharm.

2. **Escreva o código:**
   - No VS Code, digite a seguinte linha de código:
     ```python
     print("Hello, World!")
     ```
   - Esse comando `print` exibe a mensagem "Hello, World!" no terminal ou console.

3. **Salve o arquivo:**
   - Salve o arquivo com a extensão `.py`, por exemplo, `hello.py`. Certifique-se
     de escolher uma localização fácil de encontrar, como a pasta de documentos
     ou diretamente na área de trabalho.

### **2. Executando o Script**

**No Windows:**

1. **Abra o Prompt de Comando:**
   - Pressione `Win + R`, digite `cmd`, e pressione `Enter` para abrir o Prompt.

2. **Navegue até o local do arquivo:**
   - Use o comando `cd` para mudar para a pasta onde o arquivo `hello.py` foi
     salvo. Por exemplo:
     ```cmd
     cd Desktop
     ```

3. **Execute o script:**
   - Digite `python hello.py` e pressione `Enter`. Você verá a mensagem:
     ```
     Hello, World!
     ```

**No macOS/Linux:**

1. **Abra o Terminal:**
   - No macOS, você pode abrir o Terminal através do Spotlight (`Cmd + Space` e
     digite `Terminal`). No Linux, use o atalho `Ctrl + Alt + T`.

2. **Navegue até o local do arquivo:**
   - Use o comando `cd` para acessar a pasta onde o arquivo `hello.py` está salvo:
     ```bash
     cd Desktop
     ```

3. **Execute o script:**
   - Digite `python3 hello.py` e pressione `Enter`. A mensagem "Hello, World!"
     aparecerá na tela.

### **3. Entendendo o Código**

- **O que é `print`?**
  `print` é uma função em Python que exibe o texto ou dados passados para ela.
  No nosso exemplo, `print("Hello, World!")` diz ao Python para mostrar a
  mensagem "Hello, World!" no terminal.

- **O que é um script?**
  Um script Python é um arquivo de texto contendo código Python que pode ser
  executado diretamente, realizando as ações especificadas no código.

## Introdução ao Terminal Python e ao Jupyter Notebook

O terminal Python e o Jupyter Notebook são duas ferramentas essenciais para quem
está começando a programar em Python. Ambos permitem que você escreva e execute
código Python de maneira interativa, mas cada um tem suas particularidades e usos
específicos.

### **1. Terminal Python (REPL)**

O terminal Python, também conhecido como REPL (Read-Eval-Print Loop), é um
ambiente interativo onde você pode digitar código Python e ver imediatamente o
resultado.

**Como acessar:**

1. **No Windows:**
   - Abra o Prompt de Comando e digite `python` ou `python3`, dependendo da
     instalação. Pressione `Enter`.

2. **No macOS/Linux:**
   - Abra o Terminal e digite `python3`, depois pressione `Enter`.

**Usando o terminal:**

- No terminal Python, você pode digitar expressões e comandos Python diretamente.
  Por exemplo, se você digitar `2 + 2` e pressionar `Enter`, o terminal exibirá `4`.
- Para sair do terminal Python, digite `exit()` ou pressione `Ctrl + D`.

**Vantagens:**

- **Rápido e simples:** Ótimo para testar pequenos pedaços de código.
- **Interativo:** Permite ver os resultados instantaneamente, facilitando a
  aprendizagem e a experimentação.

### **2. Jupyter Notebook**

O Jupyter Notebook é uma ferramenta poderosa que permite criar e compartilhar
documentos que contêm código, texto, gráficos e muito mais. É amplamente usado em
ciência de dados e ensino, devido à sua capacidade de combinar código e conteúdo
explicativo em um único documento.

**Como instalar:**

- Primeiro, instale o Jupyter usando `pip`:
  ```bash
  pip install notebook
  ```
- Depois, inicie o Jupyter Notebook no terminal com o comando:
  ```bash
  jupyter notebook
  ```

**Usando o Jupyter Notebook:**

- Quando você inicia o Jupyter, ele abre uma interface no navegador, mostrando um
  painel onde você pode criar e gerenciar notebooks.
- Um notebook é composto de células, que podem conter código Python ou texto em
  Markdown. Para executar o código em uma célula, pressione `Shift + Enter`.
- Você pode adicionar gráficos, tabelas e visualizações diretamente no notebook,
  tornando-o ideal para análises de dados e experimentos.

**Vantagens:**

- **Documentação integrada:** Combine código e explicações em um único arquivo.
- **Visualização:** Facilita a criação de gráficos e a análise de dados de forma
  interativa.
- **Reprodutibilidade:** Compartilhe notebooks com outras pessoas, que podem
  executar o código e ver os mesmos resultados.

## Noções Básicas de Sintaxe do Python (Indentação, Comentários, Variáveis)

Python é conhecido por sua sintaxe simples e clara, o que o torna uma excelente
escolha para iniciantes. Aqui estão algumas noções básicas de sintaxe que você
precisa entender ao começar a programar em Python.

### **1. Indentação**

Diferente de muitas outras linguagens, Python usa a indentação para definir blocos
de código. Isso significa que o espaçamento no início de uma linha é importante e
não pode ser ignorado.

**Exemplo:**

```python
if 5 > 2:
    print("Cinco é maior que dois")
```

- No exemplo acima, a linha com `print` está indentada com quatro espaços (ou um
  tab), indicando que pertence ao bloco `if`. Se a indentação estiver incorreta,
  Python retornará um erro de sintaxe.

### **2. Comentários**

Comentários são linhas de texto que o Python ignora durante a execução. Eles são
usados para explicar o código, facilitando a leitura e a manutenção.

**Como usar:**

- **Comentário de linha única:** Começa com o símbolo `#`.

  ```python
  # Este é um comentário em Python
  print("Hello, World!")
  ```

- **Comentário de múltiplas linhas:** Embora Python não tenha um símbolo específico
  para comentários de múltiplas linhas, você pode usar `#` no início de cada linha
  ou usar strings de múltiplas linhas (entre `"""`) para o mesmo efeito:

  ```python
  """
  Este é um comentário de múltiplas linhas
  que também pode ser usado como uma
  docstring para documentar funções.
  """
  ```

### **3. Variáveis**

Variáveis são usadas para armazenar valores que podem ser reutilizados e manipulados
ao longo do código. Em Python, você não precisa declarar o tipo da variável, pois
Python é uma linguagem de tipagem dinâmica.

**Como definir variáveis:**

```python
nome = "João"
idade = 25
altura = 1.75
```

- **Nomeação:** Variáveis podem ter nomes que incluem letras, números e sublinhados,
  mas não podem começar com números. Por exemplo, `idade2` é válido, mas `2idade`
  não é.

- **Atribuição:** Use o símbolo `=` para atribuir um valor a uma variável. No exemplo
  acima, `nome` é uma variável que armazena a string `"João"`.

- **Tipos comuns de variáveis:** Python reconhece automaticamente o tipo de dado com
  base no valor atribuído:
  - **Inteiros:** Números inteiros (`idade = 25`)
  - **Floats:** Números decimais (`altura = 1.75`)
  - **Strings:** Texto (`nome = "João"`)
  - **Booleanos:** Verdadeiro ou falso (`verdadeiro = True`)

**Práticas:**
- Escrever e executar um script Python que imprime "Hello, World!".
- Criar variáveis de diferentes tipos (inteiro, float, string, booleano) e
  exibir seus valores e tipos no terminal.

  <center>
    <a href="https://orion-services.dev" target="blanck">
      <img src="../assets/images/logo.png" alt="Orion Services" width="3%"
      height="3%" border=0 style="border:0; text-decoration:none; outline:none">
    </a>
    <br/>
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">
          CC BY 4.0 DEED
    </a>
  </center>
