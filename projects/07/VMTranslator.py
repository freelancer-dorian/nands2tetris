import Parser
import CodeWriter as cw
from sys import argv


DEBUG = True

# f = open(argv[1])
f = open('StackArithmetic/SimpleAdd/SimpleAdd.vm')
lines = f.readlines()
for l in lines:
	cleaned_cmd = Parser.clean(l)
	
	if DEBUG:
		print(Parser.clean(l), end = '')

	cmd_type = Parser.cmdType(cleaned_cmd)
	if cmd_type == Parser.C_ARITHMETIC:
		if DEBUG:
			print('- cmd type: C_ARITHMETIC')

	if cmd_type == Parser.C_PUSH:
		arg1 = Parser.arg1(cleaned_cmd)
		arg2 = Parser.arg2(cleaned_cmd)
		if DEBUG:
			print('- arg1 ' + arg1, end = '')
			print('- arg2 ' + str(arg2), end = '')
			print('- cmd type: C_PUSH')
	if cmd_type == Parser.C_POP:
		arg1 = Parser.arg1(cleaned_cmd)
		arg2 = Parser.arg2(cleaned_cmd)
		if DEBUG:
			print('- arg1 ' + arg1, end = '')
			print('- arg2 ' + str(arg2), end = '')
			print('- cmd type: C_POP')
	if cmd_type == Parser.C_LABEL:
		pass
	if cmd_type == Parser.C_GOTO:
		pass
	if cmd_type == Parser.C_IF:
		pass
	if cmd_type == Parser.C_FUNCTION:
		pass
	if cmd_type == Parser.C_RETURN:
		pass
	if cmd_type == Parser.C_CALL:
		pass



output = ''



# of = open(argv[1].replace('.vm','.asm'), 'w+')
# of.write(output)
print(output)