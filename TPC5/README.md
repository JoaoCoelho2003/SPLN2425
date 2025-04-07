# TPC5 - Transformação de Texto

## Definição da Gramática (Usando Lark)

A variável `grammar` especifica uma gramática personalizada para a DSL, possibilitando a definição de funções que realizam transformações de texto. Os principais componentes da gramática são:

- `start` → Ponto de entrada, que aceita múltiplas funções (`function+`).
- `function` → Representa uma função, que começa sempre com `defr FUNCTION_NAME :`, seguido por múltiplos `statement+`.
- `statement` → Define o conteúdo de uma função. Pode ser:
  - `transform_statement`: Substitui palavras diretamente (`BASE ==> FUNCTION_NAME`).
  - `lambda_statement`: Aplica uma transformação dinâmica usando uma função (`BASE =e=> lambda ...`).

Para além disso, a gramática possui os seguintes componentes adicionais:

- `FUNCTION_NAME` → Nome válido para uma função definida na DSL.
- `_ARROW ("==>")` → Indica uma substituição direta, onde `BASE` será substituído por `FUNCTION_NAME`.
- `_ARROW_EVAL ("=e=>")` → Indica uma transformação dinâmica, onde `BASE` será processado por uma função lambda.

## Implementação da Transformação

A classe `Transformer` transforma a árvore sintática gerada pelo Lark em código Python executável. Os métodos principais incluem:

- `start` → Combina todas as funções transformadas num único bloco de código.
- `function` → Gera uma função Python para cada `defr ...:` definido na DSL.
- `statement` → Processa cada regra dentro de uma função.
- `transform_statement` → Converte `BASE ==> FUNCTION_NAME` em código Python que utiliza `re.sub()` para substituir palavras.
- `lambda_statement` → Converte `BASE =e=> lambda x: ...` em código Python que aplica uma função lambda a cada correspondência.

## Input

```
defr a:
		the ==> o
		cat ==> gato
		(\w+) =e=> lambda x: dictionary.get(x[1], x[1])
```

## Output

```
def transform_a(t):
		t = re.sub(r'\bthe\b', 'o', t)
		t = re.sub(r'\bcat\b', 'gato', t)
		t = re.sub(r'\b(\w+)\b', lambda x: dictionary.get(x[1], x[1]), t)
		return t
```
