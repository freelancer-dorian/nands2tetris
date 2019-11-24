# DEFINITIONS
INVALID = -1
KEYWORD = 0
SYMBOL = 1
IDENTIFIER = 2
INT_CONST = 3
STRING_CONST = 4

STRING_TYPE = ['INVALID' ,'KEYWORD', 'SYMBOL', 'IDENTIFIER', 'INT_CONST', 'STRING_CONST']

keyword_list = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return']
symbol_list = ['{', '}', '(', ')', '[', ']', '.', ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
special_symbol = '<>&'
converted_symbol = {'<':'&lt;', '>':'&gt;', '&':'&amp;'}

# global variables
token_stream = []
current_token = ''

def extract_string_list(l):
	new_list = []
	new_char = ''

	for element in l:
		# for each char in element
		for c in element:
			if c in symbol_list:
				if new_char != '':
					new_list.append(new_char)
				new_list.append(c)
				new_char = ''
			else:
				new_char = new_char + c
		if new_char != '':
			new_list.append(new_char)
			new_char = ''

	return new_list

def Constructor(file_name):
	global token_stream
	token_stream = []
	f = open(file_name)
	lines = f.readlines()
	f.close()
	for _ in lines:
		# skip comments
		if _.find('//') != -1:
			_ = _.replace(_[_.find('//'):],'')
		if _.find('/*') != -1:
			_ = _.replace(_[_.find('/*'):],'')
		if len(_) >= 2:
			for __ in extract_string_list(_.strip().split()):
				token_stream.append(__)


def hasMoreTokens():
	return len(token_stream)

def advance():
	global current_token
	current_token = token_stream.pop(0)

def tokenType():
	global current_token
	if current_token in keyword_list:
		return KEYWORD
	elif current_token in symbol_list:
		return SYMBOL
	elif current_token.isdigit():
		return INT_CONST
	elif current_token.startswith('"'):
		temp_list = [] 
		temp_list.append(current_token)
		advance()
		while (not current_token.endswith('"')) and hasMoreTokens():
			temp_list.append(current_token)
			advance()
		temp_list.append(current_token)

		current_token = ' '.join(temp_list)
		return STRING_CONST
	else:
		return IDENTIFIER

def keyword():
	return '<keyword> %s </keyword>\n' % current_token


def symbol():
	global current_token
	if current_token in converted_symbol.keys():
		current_token = converted_symbol[current_token]
	return '<symbol> %s </symbol>\n' % current_token

def identifier():
	return '<identifier> %s </identifier>\n' % current_token

def intVal():
	return '<integerConstant> %s </integerConstant>\n' % current_token


def stringVal():
	return '<stringConstant> %s </stringConstant>\n' % current_token[1:-1]

def tokeTypeTest():
	Constructor('ArrayTest/Main.jack')
	while hasMoreTokens():
		advance()
		t = tokenType()
		print(func_list[t]())

func_list = [keyword, symbol, identifier, intVal, stringVal]
