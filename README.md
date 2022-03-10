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
  <a href="#créditos">Créditos</a>
</p>

[![screenshot]('')](https://youtu.be/isLWZqVmVV0)

## Introdução
O Matrix Script é uma linguagem simples de alto nível que tem como objetivo executar cálculos e visualização de matrizes.

## Como usar

[Video de apresentação](https://youtu.be/isLWZqVmVV0).

Antes de clonar e rodar essa aplicação, você irá precisar do [Git](https://git-scm.com) e do [Python](https://www.python.org/) instalado em sua máquina. 

Para clocar o projeto, execute pelo seu terminal:

```bash
# Clone o repositório
git clone https://github.com/jorge-g99/matrixscript-master

# Entre no repositório
cd matrixscript-master

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

Para rodar o exemplo no terminal, execute:
```
py main.py .\examples\simple_matrix.mx
```

Árvore de geração utilizada para o exemplo executado:
![arvore](https://raw.githubusercontent.com/jorge-g99/matrixscript-master/master/img/simple_matrix.png)

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
- Tokens em caixa alta para execução dos comandos por convenção da linguagem
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

Projetos de código aberto utilizados:

- [Python](https://www.python.org/)
- [Numpy](https://numpy.org/)
- [SLY](https://github.com/dabeaz/sly)

---
> GitHub [@jorge-g99](https://github.com/jorge-g99) &nbsp;&middot;&nbsp;