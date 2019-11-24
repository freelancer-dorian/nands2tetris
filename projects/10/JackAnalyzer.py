from sys import argv
import JackTokenizer as jt
import CompilationEngine as ce

debug = 0
if debug == 1:
	jack_file_name = 'ArrayTest/Main.jack'
else:
	jack_file_name = 'ArrayTest/Main.jack'

token_xml_file_name = jack_file_name.replace('.jack','T_gen.xml')

# part 1, tokenize
jt.Constructor(jack_file_name)
token_xml = '<tokens>\n'

while jt.hasMoreTokens():
	jt.advance()
	token_type = jt.tokenType()
	token = jt.func_list[token_type]()
	token_xml = token_xml + token

token_xml = token_xml + '</tokens>\n'
elements = token_xml.split('\n')

if debug:
	# print(token_xml)
	pass
else:
	of = open(token_xml_file_name, 'w+')
	of.write(token_xml)
	of.close()

output_file_name = token_xml_file_name.replace('T_','_')

# part 2, compile
ce.Constructor(token_xml, output_file_name)
f = ce.compileClass()

if debug:
	print(f)
else:
	of = open(output_file_name,'w')
	of.write(f)
	of.close()

