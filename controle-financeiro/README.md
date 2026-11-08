# Controle Financeiro Pessoal

Mini-projeto desenvolvido em Python para praticar os conceitos de lógica de programação, estruturas de dados, manipulação de arquivos e Programação Orientada a Objetos (POO).

## Sobre o projeto

O Controle Financeiro Pessoal é um programa simples que permite registrar receitas e despesas e acompanhar o saldo disponível.

O projeto busca resolver um problema cotidiano: a dificuldade de organizar e acompanhar movimentações financeiras pessoais.

## Funcionalidades

- Cadastrar receitas e despesas.
- Listar todas as transações cadastradas.
- Calcular o saldo financeiro.
- Salvar e recuperar automaticamente as transações em um arquivo JSON.
- Validar entradas para evitar valores inválidos.

## Tecnologias utilizadas

- Python 3
- Biblioteca `json` (nativa do Python)

## Como executar

1. Tenha o Python 3 instalado.
2. Clone o repositório ou baixe os arquivos do projeto.
3. Abra um terminal na pasta do projeto.
4. Execute o comando `python main.py`.
5. Utilize o menu apresentado no terminal.

Não é necessário instalar bibliotecas externas.

## Estrutura do código

O sistema utiliza duas classes principais:

**Transacao:** representa uma movimentação financeira, armazenando sua descrição, valor e tipo (receita ou despesa).

**ControleFinanceiro:** gerencia as transações, calcula o saldo e realiza o salvamento e carregamento dos dados em JSON.

## Conteúdos aplicados

O projeto utiliza variáveis, condicionais, laços de repetição, funções, listas, dicionários, arquivos, classes, objetos e métodos.

## Observações

As transações são armazenadas localmente no arquivo `transacoes.json`, criado automaticamente durante a utilização do programa.

O sistema funciona pelo terminal e não utiliza banco de dados ou interface gráfica.
