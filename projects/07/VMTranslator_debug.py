import Parser
import CodeWriter as cw
from sys import argv


DEBUG = True

if DEBUG:
	f = open('MemoryAccess/BasicTest/BasicTest.vm')
else:
	f = open(argv[1])
output = ''

lines = f.readlines()
for l in lines:
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
		c = cw.pop_translate(arg1, arg2)
		output = output + c

		if DEBUG:
			print('- arg1 ' + arg1, end = '')
			print('- arg2 ' + str(arg2), end = '')
			print('- cmd type: C_POP')
			print(c)
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






output = output + '(END)\n@END\n0;JMP\n'
if DEBUG:
	print(output)
else:
	of = open(argv[1].replace('.vm','.asm'), 'w+')
	of.write(output)
	of.close()