dict_addr ={'argument':'ARG',
		'local':'LCL',
		'static':'ARG',
		'this':'THIS',
		'that':'THAT',
		'temp':'R5'}
pointer_addr = ['THIS','THAT']


def push_translate(segment, index):
	
	# fetch value to be pushed
	addr_info = ''
	if segment == 'constant':
		addr_info = '@' + str(index) + '\nD=A\n'
	elif segment =='temp':
		addr_info = '@' + str(int(index,10) + 5) + '\nD=M\n'
	else:
		base_addr = convertBaseAddr(segment, index)
		if segment == 'pointer':
			index = '0'
		addr_info = '@' + base_addr + '\n' + 'D=M\n@' + str(index) + '\nD=D+A\n@addr\nM=D\nA=M\nD=M\n'

	# stack pointer process
	return addr_info + '@SP\nA=M\nM=D\n@SP\nM=M+1\n'


def pop_translate(segment, index):
	if segment == 'temp':
		return '@SP\nM=M-1\nA=M\nD=M\n@' + str(int(index,10) + 5) + '\nM=D\n'
	else:
		base_addr = convertBaseAddr(segment, index)
		if segment == 'pointer':
			index = '0'
		return '@' + base_addr + '\nD=M\n@' + str(index) + '\nD=D+A\n@addr\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@addr\nA=M\nM=D\n'


def convertBaseAddr(segment,index):
	if segment in dict_addr:
		return dict_addr[segment]
	else:
		return pointer_addr[int(index,10)]

def arithmetric_translate(cmd):
	if cmd == 'add':
		return add_translate()
	if cmd == 'sub':
		return sub_translate()
	if cmd == 'neg':
		return neg_translate()
	if cmd == 'eq':
		return logic_translate(cmd)
	if cmd == 'gt':
		return logic_translate(cmd)
	if cmd == 'lt':
		return logic_translate(cmd)
	if cmd == 'and':
		return and_translate()
	if cmd == 'or':
		return or_translate()
	if cmd == 'not':
		return not_translate()

def add_translate():
	return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n'
def sub_translate():
	return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n'
def neg_translate():
	return '@SP\nM=M-1\nA=M\nM=-M\n@SP\nM=M+1\n'
def and_translate():
	return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M&D\n@SP\nM=M+1\n'
def or_translate():
	return '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M|D\n@SP\nM=M+1\n'
def not_translate():
	return '@SP\nM=M-1\nA=M\nM=!M\n@SP\nM=M+1\n'
def logic_translate(l):
	# fetch 2 data, and do minus
	fetch_data = '@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n'
	logic_at = ''
	logic_lable = ''
	if l == 'eq':
		logic_at = '@EQ\nD;JEQ\n'
		logic_lable = '(EQ)\n'
	if l == 'lt':
		logic_at = '@LT\nD;JLT\n'
		logic_lable = '(LT)\n'
	if l == 'gt':
		logic_at = '@GT\nD;JGT\n'
		logic_lable = '(GT)\n'

	false_flag = '@0\nD=A\n@SP_HANDLE\n0;JMP\n'
	true_flag = '@1\nD=A\n@SP_HANDLE\n0;JMP\n'

	sp_handle = '(SP_HANDLE)\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'

	return fetch_data + logic_at + false_flag + logic_lable + true_flag + sp_handle