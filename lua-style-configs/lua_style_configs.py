import ast

TEMPLATE = """
def __func__():
	pass
	{}
"""

def loads(s):
	mod = ast.parse(TEMPLATE)
	user_code = ast.parse(s)
	mod.body[0].body.extend(user_code.body)

	globals = {}
	exec(compile(mod, '<config file>', 'exec'), globals)
	return globals['__func__']()

def load(f):
	return loads(f.read())
