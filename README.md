# TING (Trybe Is Not a Google!) com Python

## Funcionalidades

Pilhas, Filas, Deques, Listas ligadas e Listas duplamente ligadas.

Para realizar o projeto, dessa forma reforçaremos vários conceitos e habilidades, como por exemplo, manipulação de arquivos TXT. 🚀

Estas estruturas de dados são de grande importância para a computação, estão presente em quase todas as operações que são realizadas, seja armazenamento em memória de informações, à transição de recursos entre programas ou diversas aplicações.

List em específico é uma das classes mais difundidas no desenvolvimento de software. Compreender o funcionamento da mesma nos dá liberdade para usufruir cada vez mais de suas características.


O que foi avaliado?

A organização e a aderência do código à especificação;

A classe implementada deve estar bem modularizada;

Legibilidade, bons nomes de variáveis, por exemplo;

Análise assintótica das principais operações.


## Requisitos

<img src="https://raw.githubusercontent.com/willianAD/Project-TING/main/image/Projeto%20TING.png">

# Requisitos Obrigatórios

### 1 - Implemente uma fila para armazenar os arquivos que serão lidos.

- Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- A fila (Queue) deve ser uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila deve implementar os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila deverá ser exposto utilizando o método `__len__` que permitirá, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` com a seguinte mensagem: `"Índice Inválido ou Inexistente"` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 1.1 - Será validado que o método `enqueue` deve adicionar um elemento à fila, modificando seu tamanho;

- 1.2 - Será validado que o método `dequeue` deve remover o elemento a mais tempo na fila, modificando seu tamanho;

- 1.3 - Será validado que o método `search` deve retornar um valor da fila a partir de um índice válido e;

- 1.4 - Será validado que o método `search` deve lançar a exceção `IndexError` com a mensagem correspondente quando o índice passado for inválido.

</details>

### 2 - Implemente uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

- Caso o arquivo TXT não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

<details>
<summary><b>Exemplo simples de um arquivo txt a ser importado</b></summary>

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 2.1 - Será validado que o método `txt_importer` deve retornar uma lista contendo as linhas do arquivo;

- 2.2 - Será validado que ao executar o método `txt_importer` com um arquivo TXT que não exista, deve ser exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo e;

- 2.3 - Será validado que ao executar o método `txt_importer` com uma extensão diferente de `.txt`, deve ser exibida a mensagem `Formato inválido` na `stderr`.

</details>

### 3 - Implemente a função `process` no módulo `file_process`. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função `txt_importer` em um dicionário que será armazenado dentro da `Queue`.

- A função irá receber como parâmetro um objeto instanciado da fila implementada no requisito 1 e o caminho para um arquivo;

- A instância da fila recebida por parâmetro **deve** ser utilizada para registrar o processamento dos arquivos;

- A função deve processar o arquivo passado por parâmetro (ou seja, gerar um dicionário com o formato e informações especificadas abaixo);

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, arquivos com o mesmo nome e caminho (`nome_do_arquivo`) não devem ser readicionados a fila);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

<details>
<summary><b>Exemplo da estrutura de saída:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```

</details>


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 3.1 - Será validado que ao executar a função `process` com um arquivo já existente na fila a execução deverá ignorá-lo e;

- 3.2 - Será validado que ao executar a função `process` com sucesso deverá mostrar dados via `stdout`.

</details>

### 4 - Implemente uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função irá receber como parâmetro a fila implementada no requisito 1.

- Caso não existam arquivos na fila, a função deve apenas emitir a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, deve ser emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 4.1 - Será validado que ao executar a função `remove` com sucesso deverá exibir mensagem correta via `stdout` e;

- 4.2 - Será validado que ao executar a função `remove` um arquivo inexistente deverá exibir a mensagem correta via `stdout`.

</details>

### 5 - Implemente uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.


- A função irá receber como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

<details>
<summary><b>Exemplo da estrutura de saída em caso de sucesso:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 5.1 - Será validado que ao executar a função `file_metadata` com sucesso deverá exibir a mensagem correta via `stdout` e;

- 5.2 - Será validado que ao executar a função `file_metadata` com posição inválida deverá exibir a mensagem correta via `stderr`.

</details>

### 6 - Implemente os testes para a classe `PriorityQueue` capaz de armazenar arquivos pequenos de forma prioritária

> Implemente em: tests/priority_queue/test_priority_queue.py

A classe `PriorityQueue` utiliza a implementação da classe `Queue` do requisito `1` para armazenar arquivos pequenos com prioridade. Utilizando a classe `PriorityQueue`, arquivos com menos de 5 linhas são armazenados de forma prioritária na fila, o que impacta no resultado dos métodos `dequeue` e `search`.

Você deve implementar testes para a classe `PriorityQueue`, garantindo que a lógica de prioridades é respeitada pelos métodos `enqueue`, `dequeue` e `search`.

<details>
  <summary>
    <b>🧠 Entenda a lógica da fila de prioridades</b>
  </summary>

Quando um arquivo prioritário (_com menos de 5 linhas_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos prioritários já inseridos, mas ficará "antes" de todos os arquivos não-prioritários já inseridos.

Quando um arquivo não-prioritário (_com 5 linhas ou mais_) é adicionado à fila de prioridades, este arquivo ficará "após" todos os arquivos já inseridos.

Exemplo:

```python
# Tamanhos dos arquivos, em ordem de inserção na fila: 
[9, 4, 2, 5, 7, 11, 3]

# Tamanhos dos arquivos, em ordem de remoção da fila:
[4, 2, 3, 9, 5, 7, 11]
```

</details>

<details>
  <summary>

#### **📌 Como seu teste é avaliado**
  </summary>

  O **teste da Trybe** irá avaliar se o **seu teste** está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendido quando a resposta do Pytest for `XFAIL(Expected Fail)` ao invés de `PASS` ou `FAIL`.
</details>

<details>
  <summary>
    
#### **🤖 O que será verificado pelo avaliador**
  </summary>

- O teste rejeita implementações que não validam a funcionalidade de cada método;
- O teste rejeita implementações que tratam todos os elementos com a mesma prioridade;
- O teste rejeita implementações que não levantam exceção ao acessar índices inválidos para Filas;
- O teste aprova implementações corretas.

</details>

## Pacote `ting_word_searches`

### 7 - Implemente uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

- A função irá receber como parâmetros a palavra a ser buscada e a fila implementada no requisito 1;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- A busca deve ser _case insensitive_ (não diferenciar maiúsculas e minúsculas);

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 2
    },
    {
      "linha": 7
    }
  ]
}]
```

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 7.1 - Será validado que ao executar a função `exists_word` com sucesso deverá retornar a estrutura correta;

- 7.2 - Será validado que ao executar a função `exists_word` com palavra inexistente deverá retornar uma lista vazia e;

- 7.3 - Será validado que ao executar a função `exists_word` a fila original não deverá ser alterada.

</details>

### 8 - Implemente uma função `search_by_word` dentro do módulo `word_search`, que busque uma palavra em todos os arquivos processados.

- Esta função deverá seguir os mesmos critérios do requisito seis, mas deverá incluir na saída o conteúdo das linhas encontradas, conforme exemplo da estrutura de retorno.

:eyes: **De olho na dica:** este requisito é uma ótima oportunidade para reforçar a prática de código limpo!

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 3,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 4,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
```

</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

- 8.1 - Será validado que ao executar a função `search_by_word` com sucesso deverá retornar a estrutura correta;

- 8.2 - Será validado que ao executar a função `search_by_word` com palavra inexistente deverá retornar uma lista vazia e;

- 8.3 - Será validado que ao executar a função `search_by_word` a fila original não deverá ser alterada.

</details>


## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [Trybe](https://www.betrybe.com/).
