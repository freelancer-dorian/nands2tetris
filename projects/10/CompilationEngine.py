CLASS_BODY_INDEX = 1
CLASSVARDEC_SUBRDDEC_INDEX = 2
SUBROUTINE_BODY_INDEX = 3

keywordsConstant = ['true', 'false', 'null', 'this']
op_list = ['+', '-', '*', '/', '&amp;', '|', '&lt;', '&gt;', '=']
unary_op_list = ['-', '~']
converted_symbol = {'<':'&lt;', '>':'&gt;', '&':'&amp;'}


token_elements = []
output_file = ''
final_xml = ''

debug = 0

def xml_tag_string(keyword, indent_level):
	return '%s<%s>\n%s%s</%s>\n' %('\t' * indent_level, keyword, '%s', '\t' * indent_level, keyword)

def pop_till_mark(l, mark, level, mark_required):
	ret = ''
	while get_token(l[0]) != mark:
		ret = ret + '\t' * level + l.pop(0) + '\n'
	if mark_required:
		ret = ret + '\t' * level + l.pop(0) + '\n'
	return ret

def get_flag(element):
	return element[element.find('<')+1:element.find('>')]

def get_token(element):
	return element[element.find('>')+2:element.find('</')-1]

def is_constant(element):
	ret = False
	f = get_flag(element)
	t = get_token(element)

	if (f == 'integerConstant') or (f == 'stringConstant') or (f == 'keyword' and t in keywordsConstant):
		ret = True
	return ret

def Constructor(input_stream, output_stream):
	global token_elements
	global output_file
	token_elements = input_stream.split('\n')[1:-2]
	output_file = output_stream

def compileClass():
	# patern: class className { ... }
	global token_elements
	global final_xml
	class_body_string = ''
	if get_token(token_elements[0]) == 'class':
		final_xml = final_xml + xml_tag_string('class', 0)
		
		# class id { --> class body string
		class_body_string = pop_till_mark(token_elements, '{', CLASS_BODY_INDEX, True)
		
		# parse into class body until all tokens pop out
		while(len(token_elements) > 0):
		# subRoutine or classVarDec
			t = get_token(token_elements[0]) 
			if t == 'constructor' or t == 'method' or t == 'function':
				class_body_string = class_body_string + compileSubroutine()
			if t == 'static' or t == 'field':
				class_body_string = class_body_string + compileClassVarDec()
			if get_token(token_elements[0]) == '}':
				class_body_string = class_body_string + pop_till_mark(token_elements, '}', CLASS_BODY_INDEX, True)

	return final_xml % class_body_string
	
def compileClassVarDec():
	global token_elements
	tag_wrapper = xml_tag_string('classVarDec', CLASS_BODY_INDEX)
	inner_str = pop_till_mark(token_elements, ';', CLASSVARDEC_SUBRDDEC_INDEX, True)
	return tag_wrapper % inner_str

def compileSubroutine():

	global token_elements
	tag_wrapper_1 = xml_tag_string('subroutineDec', CLASS_BODY_INDEX)
	subroutine_inner = ''

	indent_subroutine = '\t' * CLASSVARDEC_SUBRDDEC_INDEX
	
	# part 1 - before_paramList
	before_paramList = pop_till_mark(token_elements, '(', CLASSVARDEC_SUBRDDEC_INDEX, True)
	paramList_inner = pop_till_mark(token_elements, ')', CLASSVARDEC_SUBRDDEC_INDEX + 1, False)
	# part 2 - parameterList whole
	paramList_whole = xml_tag_string('parameterList', CLASSVARDEC_SUBRDDEC_INDEX) % paramList_inner
	# part 3 - )
	right_brace = pop_till_mark(token_elements, ')', CLASSVARDEC_SUBRDDEC_INDEX, True)

	# part 4 - subroutine body
	left_outter_brace = pop_till_mark(token_elements, '{', SUBROUTINE_BODY_INDEX, True)
	sub_routine_body_inner = ''
	while get_token(token_elements[0]) != '}':
		if get_token(token_elements[0]) == 'var':
			sub_routine_body_inner = sub_routine_body_inner + compileVarDec(SUBROUTINE_BODY_INDEX)
		else:
			sub_routine_body_inner = sub_routine_body_inner + compileStatements(SUBROUTINE_BODY_INDEX)
	sub_routine_body_end = '\t' * SUBROUTINE_BODY_INDEX + token_elements.pop(0) + '\n'
	sub_routine_body_wrapper =  xml_tag_string('subroutineBody', CLASSVARDEC_SUBRDDEC_INDEX) % (left_outter_brace + sub_routine_body_inner + sub_routine_body_end)

	subroutine_inner = before_paramList + paramList_whole + right_brace + sub_routine_body_wrapper

	return tag_wrapper_1 % subroutine_inner
	
def compileParameterlist():
	pass

def compileVarDec(current_level):
	global token_elements
	inner_str = pop_till_mark(token_elements,';', current_level + 1, True)
	return xml_tag_string('varDec', current_level) % inner_str
	
def compileStatements(current_level):
	global token_elements
	ret = ''

	while get_token(token_elements[0]) != '}':
		if get_token(token_elements[0]) == 'do': 
			ret = ret + compileDo(current_level + 1)
		if get_token(token_elements[0]) == 'let': 
			ret = ret + compileLet(current_level + 1)
		if get_token(token_elements[0]) == 'while': 
			ret = ret + compileWhile(current_level + 1)
		if get_token(token_elements[0]) == 'if': 
			ret = ret + compileIf(current_level + 1)
		if get_token(token_elements[0]) == 'return': 
			ret = ret + compileReturn(current_level + 1)


	return xml_tag_string('statements', current_level) % ret

def compileDo(current_level):
	# TODO
	global token_elements
	inner_str = ''
	do_statement_raw = pop_till_mark(token_elements,';', current_level + 1, True)
	brace_idx = do_statement_raw.find('(')
	p1_idx = do_statement_raw.find('>',brace_idx) + 1
	brace2_idx = do_statement_raw.find(')')
	p2_idx = do_statement_raw[:brace2_idx].rfind('\n')

	part1 = do_statement_raw[:p1_idx + 1] 			# do var(
	part2 = do_statement_raw[p1_idx + 1:p2_idx + 1]	# exp
	part3 = do_statement_raw[p2_idx +1:]			# );
	exp = compileExpressionList(part2.split('\n')[:-1], current_level + 1)

	return xml_tag_string('doStatement', current_level) % (part1 + exp + part3)
	
def compileLet(current_level):
	global token_elements
	express = ''
	#  let varName ([express])? = express;
	let_statement_raw = pop_till_mark(token_elements,';', current_level + 1, True)
	eq_idx = let_statement_raw.find('=')
	p1_idx = let_statement_raw[:eq_idx].rfind('\n')
	p2_idx = let_statement_raw.find('>',eq_idx) + 1

	part1 = let_statement_raw[:p1_idx + 1]
	part2 = let_statement_raw[p1_idx + 1:p2_idx + 1]
	part3 = let_statement_raw[p2_idx + 1:]
	part4 = part3[part3[:-2].rfind('\n') + 1:]
	part3 = part3.replace(part4, '')

	if '[' in part1:
		p1_1_idx = part1.find('>',part1.find('[')) + 1
		p1_2_idx = part1[:part1.find(']')].rfind('\n')
		part1_1 = part1[:p1_1_idx + 1]
		part1_2 = part1[p1_1_idx + 1:p1_2_idx + 1]
		part1_3 = part1[p1_2_idx + 1:]
	
		express1 = compileExpression(part1_2.split('\n')[:-1], current_level + 1)
		part1 = part1_1 + express1 + part1_3

	express = compileExpression(part3.split('\n')[:-1], current_level + 1)		
	inner_str = part1 + part2 + express + part4

	return xml_tag_string('letStatement', current_level) % inner_str

def compileWhile(current_level):
	global token_elements
	inner_str = pop_till_mark(token_elements, '(', current_level + 1, True)	
	tag_wrapper = xml_tag_string('whileStatement', current_level)
	while_exp_str = pop_till_mark(token_elements, ')', current_level + 1, False)
	exp_list = while_exp_str.split('\n')[:-1]
	expression = compileExpression(exp_list, current_level + 1)
	inner_str2 = pop_till_mark(token_elements, '{', current_level + 1, True)
	inner_statement = compileStatements(current_level + 1)
	inner_str3 = '\t' * (current_level + 1) + token_elements.pop(0) + '\n'

	return tag_wrapper % (inner_str + expression + inner_str2 + inner_statement + inner_str3)

def compileReturn(current_level):
	global token_elements
	inner_str = pop_till_mark(token_elements,'return', current_level + 1, True)
	expression = ''
	if get_token(token_elements[0]) != ';':
		exp_str = pop_till_mark(token_elements, ';', current_level + 1, False)
		expression = compileExpression(exp_str.split('\n')[:-1], current_level + 1)
	inner_str2 = pop_till_mark(token_elements, ';', current_level + 1, True)

	return xml_tag_string('returnStatement', current_level) % (inner_str + expression + inner_str2)

	
def compileIf(current_level):
	global token_elements
	inner_str = pop_till_mark(token_elements, '(', current_level + 1, True)
	tag_wrapper = xml_tag_string('ifStatement', current_level)
	exp_str = pop_till_mark(token_elements, ')', current_level + 1, False)
	expression = compileExpression(exp_str.split('\n')[:-1], current_level + 1)
	inner_str2 = pop_till_mark(token_elements, '{', current_level + 1, True)
	inner_statement = compileStatements(current_level + 1)
	inner_str3 = '\t' * (current_level + 1) + token_elements.pop(0) + '\n'

	inner_str4 = ''
	inner_statement2 = ''
	inner_str5 = ''

	if get_token(token_elements[0]) == 'else':
		inner_str4 = pop_till_mark(token_elements, '{', current_level + 1, True)
		inner_statement2 = compileStatements(current_level + 1)
		inner_str5 =  '\t' * (current_level + 1) + token_elements.pop(0) + '\n'

	return tag_wrapper % (inner_str + expression + inner_str2 + inner_statement + inner_str3 + inner_str4 + inner_statement2 + inner_str5)

# accept a list of xml - tags, not handling global xml list	
def compileExpression(xml_tag_list, current_level):
	return xml_tag_string('expression', current_level) % compileTerm(xml_tag_list, current_level + 1)
	
def compileTerm(xml_tag_list, current_level):

	inner_str = ''
	term2 = []
	op = ''
	while len(xml_tag_list) > 0:		
		cur_e = xml_tag_list.pop(0)
		cur_token = get_token(cur_e)
		if is_constant(cur_e) or get_flag(cur_e) == 'identifier' or cur_token == '.':
			inner_str = inner_str + '\t' * (current_level + 1) + cur_e.replace('\t','') + '\n'
		elif cur_token == '[':
			inner_str = inner_str + '\t' * (current_level + 1) + cur_e.replace('\t','') + '\n'
			newlist = []
			while get_token(xml_tag_list[0]) != ']':
				newlist.append(xml_tag_list.pop(0)) 
			inner_str = inner_str + compileExpression(newlist, current_level + 1) + ( '\t' * (current_level + 1) + xml_tag_list.pop(0).replace('\t','')) + '\n'
		elif cur_token == '(':
			# expression list OR expression
			newlist = []
			while get_token(xml_tag_list[0]) != ')':
				newlist.append(xml_tag_list.pop(0)) 
			if len(inner_str) > 0:
				handled_expression = compileExpressionList(newlist, current_level + 1)				
			else:
				handled_expression = compileExpression(newlist, current_level + 1)				
			inner_str = inner_str + '\t' * (current_level + 1) + cur_e.replace('\t','') + '\n' + handled_expression + ( '\t' * (current_level + 1) + xml_tag_list.pop(0).replace('\t','')) + '\n'
		elif cur_token in unary_op_list or cur_token in op_list :
			op = '\t' * (current_level) + cur_e.replace('\t','') + '\n'
			term2 = xml_tag_list

			xml_tag_list = []
		else:
			pass

	if len(term2) > 0:
		return xml_tag_string('term',current_level) % inner_str + op + compileTerm(term2, current_level)
	else:
		return xml_tag_string('term',current_level) % inner_str + op


def compileExpressionList(xml_tag_list, current_level):
	inner_str = ''
	comma_list_idx = []
	comma_content = []
	exp_content = []
	exp_list = []
	for (idx, tag) in enumerate(xml_tag_list):
		if ',' in tag:
			comma_list_idx.append(idx)

	if len(comma_list_idx) > 0:
		prev = 0
		for idx in comma_list_idx:
			exp_list.append(xml_tag_list[prev:idx])
			comma_content.append('\t' * (current_level + 1) + xml_tag_list[idx].replace('\t','') + '\n')
			prev = idx
		exp_list.append(xml_tag_list[comma_list_idx[-1] + 1:])

		for _ in exp_list:
			exp_content.append(compileExpression(_, current_level + 1))
		inner_str = inner_str + exp_content.pop(0)
		while len(exp_content) > 0:
			inner_str = inner_str + comma_content.pop(0) + exp_content.pop(0)
	elif len(xml_tag_list) == 0:
		inner_str = ''
	else:
		inner_str = compileExpression(xml_tag_list, current_level + 1)

	return xml_tag_string('expressionList', current_level) % inner_str

	
def termType(element):
	pass