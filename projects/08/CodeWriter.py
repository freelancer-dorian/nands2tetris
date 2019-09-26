dict_addr = {'argument':'ARG',
			'local':'LCL',
			'static':'16',
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
	elif 'static' in segment :
		addr_info = '@%s_%s\nD=M\n' % (segment.replace('/','_'), index)
	else:
		base_addr = convertBaseAddr(segment, index)
		if segment == 'pointer':
			addr_info = '@%s\nD=M\n' % base_addr
		else:

			addr_info = '@' + base_addr + '\n' + 'D=M\n@' + str(index) + '\nD=D+A\n@addr\nM=D\nA=M\nD=M\n'

	# stack pointer process
	return addr_info + '@SP\nA=M\nM=D\n@SP\nM=M+1\n'


def pop_translate(segment, index):
	if segment == 'temp':
		return '@SP\nM=M-1\nA=M\nD=M\n@' + str(int(index,10) + 5) + '\nM=D\n'
	elif 'static' in segment:
		return '@SP\nM=M-1\nA=M\nD=M\n@%s_%s\nM=D\n' % (segment.replace('/','_'), index)
	else:
		base_addr = convertBaseAddr(segment, index)
		if segment == 'pointer':
			return '@SP\nM=M-1\nA=M\nD=M\n@%s\nM=D\n' % base_addr
		else:
			return '@' + base_addr + '\nD=M\n@' + str(index) + '\nD=D+A\n@addr\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@addr\nA=M\nM=D\n'

def label_translate(cmd):
	return '(%s)\n' % cmd.split(' ')[1]

def goto_translate(cmd):
	label = cmd.split(' ')[1]
	return '@%s\n0;JMP\n' % label

def if_goto_translate(cmd):
	label = cmd.split(' ')[1]
	return '@SP\nM=M-1\nA=M\nD=M\n@%s\nD;JGT\n' % label

def func_translate(cmd):
	func_label = cmd.split(' ')[1]
	var_count = cmd.split(' ')[2]
	ret = '(%s)\n' % func_label
	for _ in range(int(var_count,10)):
		ret = ret + '@0\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n'
	return ret

def return_translate(cmd):
	return '@LCL\nD=M\n@FRAME\nM=D\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@5\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n@SP\nM=M-1\nA=M\nA=M\nD=M\n@RET\nM=D\n@ARG\nD=M\n@addr_arg\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@addr_arg\nA=M\nM=D\n@LCL\nD=M\n@SP\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@THAT\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@THIS\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@ARG\nM=D\n@SP\nM=M-1\nA=M\nD=M\n@LCL\nM=D\n@addr_arg\nD=M+1\n@SP\nM=D\n@RET\nA=M\n0;JMP\n'

def call_translate(cmd, file_name, idx):
	func_name = cmd.split(' ')[1]
	ret_name = cmd.split(' ')[1] + file_name.replace('/','_') + str(idx)
	local_count = cmd.split(' ')[2]
	return '@return_after_%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@SP\nD=M\nA=M\nM=D\n@SP\nM=M+1\n@%s\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@5\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n@SP\nM=M-1\nA=M\nD=M\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@%s\n0;JMP\n(return_after_%s)\n' % (ret_name, local_count, func_name, ret_name)

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