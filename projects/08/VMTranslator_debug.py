import Parser
import CodeWriter as cw
from sys import argv


DEBUG = 0

if DEBUG == 1:
	f = open('ProgramFlow/FibonacciSeries/FibonacciSeries.vm')
elif DEBUG == 2:
	f = open('test.vm')
else:
	f = open(argv[1])

temp_vm_content = ''
output = ''

lines = f.readlines()

# for l in lines:
# 	cleaned_cmd = Parser.clean(l)
	
# 	if DEBUG:
# 		print('//' + Parser.clean(l), end = '')

# 	cmd_type = Parser.cmdType(cleaned_cmd)
# 	if cmd_type == Parser.C_RETURN:
			
# 	elif cmd_type == Parser.C_CALL:
	
# 	else:
# 		temp_vm_content = temp_vm_content + cleaned_cmd

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
		c = cw.call_translate(cleaned_cmd)
		output = output + c
		if DEBUG:
			print('- cmd type: C_CALL')
			print(c)		
if DEBUG:
	print(output)
else:
	of = open(argv[1].replace('.vm','.asm'), 'w+')
	of.write(output)
	of.close()