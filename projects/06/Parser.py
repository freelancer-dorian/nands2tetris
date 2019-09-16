A_COMMAND = 0
C_COMMAND = 1
L_COMMAND = 2
INVALID = -1


def hasMoreCommands():
	pass

def clean(s):
	ret = ''
	if '//' in s:
		ret = s.replace(s[s.find('//'):],'')
	else:
		ret = s
	return ''.join(ret.split())

def commandType(s):
	if len(s) == 0:
		return INVALID
	elif s[0] == '@':
		return A_COMMAND
	elif s[0] == '(':
		return L_COMMAND
	else:
		return C_COMMAND

def symbol(s):
	return s[1:]

def dest(s):
	if '=' in s:
		return s[:s.find('=')]
	else:
		return ''

def comp(s):
	begin = 0
	end = len(s)
	if '=' in s:
		begin = s.find('=') + 1

	if ';' in s:
		end = s.find(';')

	return s[begin:end]


def jump(s):
	if ';' in s:
		return s[s.find(';') + 1:]
	else:
		return ''

def grammarCheck():
	return True