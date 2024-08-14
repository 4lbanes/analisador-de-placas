# Projeto de Identificação de Placas de Veículos

## Descrição do Projeto

Este projeto em Python tem como objetivo identificar a origem de veículos a partir de suas placas no padrão Mercosul. O programa utiliza um banco de dados SQLite para armazenar faixas de letras iniciais e seus estados correspondentes. Além de identificar o estado de origem de uma placa específica, o programa oferece funcionalidades para análise combinatória do número de placas registradas entre os estados de Minas Gerais (MG), Mato Grosso (MT) e Distrito Federal (DF).

## Funcionalidades Principais

1. **Identificação de Placa:**
   - Permite ao usuário inserir uma placa de veículo e retorna o estado de origem baseado nas letras iniciais.

2. **Análise Combinatória:**
   - Calcula e exibe o número total de placas registradas entre os estados de MG, MT e DF.

3. **Banco de Dados SQLite:**
   - Um banco de dados SQLite (`placas.db`) é utilizado para armazenar e consultar as faixas de letras iniciais das placas associadas aos seus estados.

## Requisitos

- Python 3.x
- Biblioteca SQLite3 (inclusa por padrão no Python)

## Como Executar o Projeto

1. **Clone o Repositório:**
   - Clone o repositório para o seu ambiente local.

2. **Configurar o Banco de Dados:**
   - Execute a função `criar_banco_de_dados()` para criar e popular o banco de dados SQLite com as faixas de placas e estados correspondentes.

3. **Executar o Programa:**
   - Execute o programa e siga as instruções no terminal para interagir com o sistema.

## Estrutura do Projeto

- `placas.db`: Banco de dados SQLite contendo as faixas de letras iniciais das placas e seus estados correspondentes.
- `script.py`: Código-fonte principal do programa.

## Exemplos de Uso

- **Identificação de Placa:**
   - O usuário insere uma placa de veículo e o sistema retorna o estado correspondente, ex: "A placa AAA1234 é de: Paraná".

- **Análise Combinatória:**
   - O sistema calcula e exibe o número total de placas entre os estados de MG, MT e DF, ex: "Minas Gerais (MG) tem 25 placas registradas. Total de placas: 75".

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

---

**Autor:** João Arthur Veras Barros Dias
