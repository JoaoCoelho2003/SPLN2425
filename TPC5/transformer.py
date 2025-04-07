from lark import Lark, Transformer

grammar = r"""
start: function+

function: "defr" FUNCTION_NAME ":" NEWLINE statement+

statement: ( lambda_statement | transform_statement) NEWLINE

lambda_statement: BASE _ARROW_EVAL /[^\n]+/

transform_statement: BASE _ARROW FUNCTION_NAME

BASE: FUNCTION_NAME | /[^ ]+/

FUNCTION_NAME.1: /[a-zA-Z_][a-zA-Z_0-9]*/
_ARROW.2: "==>"
_ARROW_EVAL.2: "=e=>"

%import common.NEWLINE
%import common.WS
%ignore WS
"""


class Transformer(Transformer):
    def start(self, items):
        transformed_function = ""
        for function in items:
            transformed_function += function
        return transformed_function

    def function(self, items):
        function_name, _, *statements = items
        code = f"def transform_{function_name}(t):\n"
        for statement in statements:
            code += f"    {statement}\n"
        code += "    return t\n"
        return code

    def statement(self, items):
        return items[0]

    def transform_statement(self, items):
        old_word, new_word = items
        transformation = f"t = re.sub(r'\\b{old_word}\\b', '{new_word}', t)"
        return transformation

    def lambda_statement(self, items):
        regex, transformer = items
        print("regex ", regex)
        print("transformer ", transformer)
        lambda_transformation = f"t = re.sub(r'\\b{regex}\\b', {transformer}, t)"
        return lambda_transformation


parse = Lark(grammar, parser="lalr", transformer=None)

text = """
defr a:
	the ==> o
	cat ==> gato
	(\\w+) =e=> lambda x: dictionary.get(x[1], x[1])
"""

tree = parse.parse(text)
print(tree)

transformer = Transformer()
result = transformer.transform(tree)
print(result)
