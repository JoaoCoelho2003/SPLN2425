# TPC4 - Processamento de Texto com Razões de Frequência

## Descrição

Este trabalho implementa um pipeline de processamento de texto que calcula as razões de frequência das palavras num texto dado. As razões são calculadas comparando a frequência absoluta das palavras no texto com os valores correspondentes num dicionário pré-definido.

## Uso

A função principal é `main_razoes`, que processa o texto de entrada e calcula as razões de frequência. Suporta as seguintes opções:

### Opções

- `-l LANG`: Especifica o identificador de idioma a ser usado para o dicionário. O padrão é `'pt'` para Português.

### Exemplo

```bash
python script.py -l pt < input.txt
```

## Pipeline

O programa utiliza um pipeline com as seguintes etapas:

1. **Redução de Texto**: Converte o texto em probabilidades usando o `Convert2ProbabilityStage`.
2. **Cálculo de Frequências**: Compara as frequências absolutas das palavras com os valores do dicionário para calcular as razões.

## Instruções

Para executar o código, siga os passos abaixo:

```shell
$ cd ftk
```

```shell
$ pip install . --break-system-packages
```