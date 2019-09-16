def dest(s):
	if s == '':
		return '000'
	if s == 'M':
			return '001'
	if s == 'D':
			return '010'
	if s == 'MD':
			return '011'
	if s == 'A':
			return '100'
	if s == 'AM':
			return '101'
	if s == 'AD':
			return '110'
	if s == 'AMD':
		return '111'

def comp(s):
	ret = ''
	if 'M' in s:
		ret = '1'
		s = s.replace('M','A')
	else:
		ret = '0'

	if s == '0': 
		ret = ret + '101010'
	if s == '1': 
		ret = ret + '111111'
	if s == '-1': 
		ret = ret + '111010'
	if s == 'D': 
		ret = ret + '001100'
	if s == 'A': 
		ret = ret + '110000'
	if s == '!D': 
		ret = ret + '001101'
	if s == '!A': 
		ret = ret + '110001'
	if s == '-D': 
		ret = ret + '001111'
	if s == '-A': 
		ret = ret + '110011'
	if s == 'D+1': 
		ret = ret + '011111'
	if s == 'A+1': 
		ret = ret + '110111'
	if s == 'D-1': 
		ret = ret + '001110'
	if s == 'A-1': 
		ret = ret + '110010'
	if s == 'D+A': 
		ret = ret + '000010'
	if s == 'D-A': 
		ret = ret + '010011'
	if s == 'A-D': 
		ret = ret + '000111'
	if s == 'D&A': 
		ret = ret + '000000'
	if s == 'D|A': 
		ret = ret + '010101'

	return ret

def jump(s):
	if s == '': 
		return '000'
	if s == 'JGT': 
		return '001'
	if s == 'JEQ': 
		return '010'
	if s == 'JGE': 
		return '011'
	if s == 'JLT': 
		return '100'
	if s == 'JNE': 
		return '101'
	if s == 'JLE': 
		return '110'
	if s == 'JMP': 
		return '111'