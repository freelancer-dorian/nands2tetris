import Parser
import Code
import SymbolTable as st
from sys import argv

st.Constructor()

f = open(argv[1])
lines = f.readlines()

symbol_count = 0
cmd_count = 0
bin_output = ''

# loop 1, check and build jump table
for l in lines:
	cleaned_str = Parser.clean(l)
	cmd_type = Parser.commandType(cleaned_str)

	if cmd_type == Parser.A_COMMAND:
		cmd_count = cmd_count + 1
	if cmd_type == Parser.C_COMMAND:
		cmd_count = cmd_count + 1
	if cmd_type == Parser.L_COMMAND:
		symbol = cleaned_str[1:-1]
		st.addEntry(symbol, cmd_count)

for l in lines:
	cleaned_str = Parser.clean(l)
	cmd_type = Parser.commandType(cleaned_str)
	# A command 
	if cmd_type == Parser.A_COMMAND:
		bin_addr = ''
		if cleaned_str[1:].isdigit():
			bin_addr = bin(int(cleaned_str[1:], 10))[2:]
		else:
			symbol = Parser.symbol(cleaned_str)
			if not st.contains(symbol):
				st.addEntry(symbol, 16 + symbol_count)
				symbol_count = symbol_count + 1
		
			addr = st.getAddress(symbol);
			bin_addr = bin(addr)[2:]
		newline = (16 - len(bin_addr)) * '0' + bin_addr + '\n'
		bin_output = bin_output + newline

	# C command
	if cmd_type == Parser.C_COMMAND:
		comp = Parser.comp(cleaned_str)
		dest = Parser.dest(cleaned_str)
		jump = Parser.jump(cleaned_str)

		comp_code = Code.comp(comp)
		dest_code = Code.dest(dest)
		jump_code = Code.jump(jump)

		newline = '111' + comp_code + dest_code + jump_code + '\n'
		bin_output = bin_output + newline

of = open(argv[1].replace('.asm','.hack'), 'w+')
of.write(bin_output)