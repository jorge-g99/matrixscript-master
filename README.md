<h1 align="center">
  Matrix Script
</h1>

<h4 align="center">Linguagem baseada na biblioteca <a href="https://numpy.org">Numpy</a> e feita com <a href="https://www.python.org/">Python</a>.</h4>

<p align="center">
  <a href="#introdução">Introdução</a> •
  <a href="#como-usar">Como usar</a> •
  <a href="#exemplo">Exemplo</a> •
  <a href="#documentação">Documentação</a> •
  <a href="#produções-e-ações-semânticas">Produções e Ações Semânticas</a> •
  <a href="#créditos">Créditos</a> •
  <a href="#license">License</a>
</p>

[![screenshot]('imagem do vídeo')]('link do vídeo')

## Introdução
O Pandas Script é uma linguagem simples de alto nível que tem como objetivo simplificar e agilizar a visualização e gerenciamento de dados como CSV.

## Como usar

[Video de apresentação]().

Para clonar e rodar essa aplicação, você irá precisar [Git](https://git-scm.com), [Python](https://www.python.org/). Pelo seu terminal:

```bash
# Clone o repositório
git clone https://github.com/jorge-g99/matrixscript

# Entre no repositório
cd matrixscript

# Instale as dependências
pip install numpy

# Rode a aplicação
py main.py
```

## Exemplo
```
a = LOAD "[[1,2],[2,1]]"
b = LOAD "[[2,1],[1,2]]"
c = LOAD "[[3,0],[1,1]]"
d = a + b * c
PRINT d
```

Rodando o exemplo no terminal:
```
py main.py .\example\covid_death.ps
```

Árvore de geração utilizada para o exemplo executado:
![arvore]()

## Documentação

- ``py main.py``
  - Executa o shell
- ``py main.py help``
  - Executa o comando de ajuda
- ``py main.py license``
  - Executa o comando de licensa
- ``py main.py copyright``
  - Executa o comando de copyright
- ``py main.py filePath``
  - Executa o parse de um arquivo

## Produções e Ações Semânticas

Observações:
- Tokens em caixa alta para execução dos comandos
```bnf
Grammar                                         Action
------------------------                        ---------------------------------
statement : PRINT expr                          print(expr.val)
          | ID = expr                           ID.val = expr.val

expr0     : expr1 + expr2                       expr0.val = expr1.val + expr2.val
          | expr1 - expr2                       expr0.val = expr1.val - expr2.val
          | expr1 * expr2                       expr0.val = expr1.val * expr2.val
          | expr1 / expr2                       expr0.val = expr1.val / expr2.val
          | (expr1)                             expr0.val = expr1.val
          | FLOAT                               expr0.val = float(FLOAT.val)
          | INT                                 expr0.val = int(INT.val)
          | STRING                              expr0.val = string(STRING.val)
          | ID                                  self.ids[ID.val]
          | LOAD STRING                         expr0.val = np.array(eval(STRING.val))
```

## Créditos

Essa aplicação utiliza os seguintes projetos de código aberto:

- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [SLY](https://github.com/dabeaz/sly)

Inspiração do README [electron-markdownify](https://github.com/amitmerchant1990/electron-markdownify).

## License

MIT

---
> GitHub [@jorge-g99](https://github.com/jorge-g99) &nbsp;&middot;&nbsp;