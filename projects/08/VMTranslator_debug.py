import Parser
import CodeWriter as cw
from sys import argv

window_path = 'D:\_wanghui\\workspace\nand2tetris\\projects\\08\\FunctionCalls\\NestedCall\Sys.vm'

DEBUG = 0

if DEBUG == 1:
	f = open('ProgramFlow/FibonacciSeries/FibonacciSeries.vm')
elif DEBUG == 2:
	f = open(window_path[window_path[:window_path[:window_path.rfind('\\')].rfind('\\')].rfind('\\')+1:].replace('\\','/'))
else:
	f = open(argv[1])

temp_vm_content = ''
output = ''

lines = f.readlines()


for (idx,l) in enumerate(lines):
	cleaned_cmd = Parser.clean(l)
	
	if DEBUG:
		print('//' + Parser.clean(l), end = '')

	cmd_type = Parser.cmdType(cleaned_cmd)
	if cmd_type == Parser.C_ARITHMETIC:
		c = cw.arithmetric_translate(cleaned_cmd)
		output = output + c

		if DEBUG:
			print('- cmd type: C_ARITHMETIC')
			print(c)

	if cmd_type == Parser.C_PUSH:
		arg1 = Parser.arg1(cleaned_cmd)
		arg2 = Parser.arg2(cleaned_cmd)
		if arg1 == 'static':
			arg1 = argv[1] + arg1
		c = cw.push_translate(arg1, arg2)
		output = output + c

		if DEBUG:
			print('- arg1 ' + arg1, end = '')
			print('- arg2 ' + str(arg2), end = '')
			print('- cmd type: C_PUSH')
			print(c)
	if cmd_type == Parser.C_POP:
		arg1 = Parser.arg1(cleaned_cmd)
		arg2 = Parser.arg2(cleaned_cmd)
		if arg1 == 'static':
			arg1 = argv[1] + arg1
		c = cw.pop_translate(arg1, arg2)
		output = output + c

		if DEBUG:
			print('- arg1 ' + arg1, end = '')
			print('- arg2 ' + str(arg2), end = '')
			print('- cmd type: C_POP')
			print(c)
	if cmd_type == Parser.C_LABEL:
		c = cw.label_translate(cleaned_cmd)
		output = output + c

		if DEBUG:
			print('- cmd type: C_LABEL')
			print(c)
	if cmd_type == Parser.C_GOTO:
		c = cw.goto_translate(cleaned_cmd)
		output = output + c
		if DEBUG:
			print('- cmd type: C_GOTO')
			print(c)
	if cmd_type == Parser.C_IF:
		c = cw.if_goto_translate(cleaned_cmd)
		output = output + c
		if DEBUG:
			print('- cmd type: C_IF')
			print(c)
	if cmd_type == Parser.C_FUNCTION:
		c = cw.func_translate(cleaned_cmd)
		output = output + c
		if DEBUG:
			print('- cmd type: C_FUNCTION')
			print(c)

	if cmd_type == Parser.C_RETURN:
		c = cw.return_translate(cleaned_cmd)
		output = output + c
		if DEBUG:
			print('- cmd type: C_CALL')
			print(c)		
	if cmd_type == Parser.C_CALL:
		c = cw.call_translate(cleaned_cmd, argv[1] , idx)
		output = output + c
		if DEBUG:
			print('- cmd type: C_CALL')
			print(c)		

output = output + '(END)\n@END\n0;JMP\n'
if DEBUG:
	print(output)
else:
	of = open(argv[1].replace('.vm','.asm'), 'w+')
	of.write(output)
	of.close()