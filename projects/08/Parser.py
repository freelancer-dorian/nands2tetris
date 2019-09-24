C_INVALID = -1
C_ARITHMETIC = 0
C_PUSH = 1
C_POP = 2
C_LABEL = 3
C_GOTO = 4
C_IF = 5
C_FUNCTION = 6
C_RETURN = 7
C_CALL = 8

def clean(s):
	ret = s
	if '//' in s:
		ret = s.replace(s[s.find('//'):],'')
	return ret.lstrip().rstrip()	

def cmdType(s):
	if len(s) == 0:
		return C_INVALID
	else:
		if s.startswith('push'): 
			return C_PUSH
		elif s.startswith('pop'): 
			return C_POP
		elif s.startswith('label'): 
			return C_LABEL
		elif s.startswith('goto'): 
			return C_GOTO
		elif s.startswith('if-goto'): 
			return C_IF
		elif s.startswith('function'): 
			return C_FUNCTION
		elif s.startswith('return'): 
			return C_RETURN
		elif s.startswith('call'): 
			return C_CALL
		else:
			return C_ARITHMETIC

def arg1(s):
	ele = s.split(' ')
	return ele[1]
def arg2(s):
	ele = s.split(' ')
	return ele[2]