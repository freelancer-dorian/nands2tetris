def Constructor():
	global dict_table
	dict_table = dict()

	dict_table['SP'] = 0
	dict_table['LCL'] = 1
	dict_table['ARG'] = 2
	dict_table['THIS'] = 3
	dict_table['THAT'] = 4
	dict_table['R0'] = 0
	dict_table['R1'] = 1
	dict_table['R2'] = 2
	dict_table['R3'] = 3
	dict_table['R4'] = 4
	dict_table['R5'] = 5
	dict_table['R6'] = 6
	dict_table['R7'] = 7
	dict_table['R8'] = 8
	dict_table['R9'] = 9
	dict_table['R10'] = 10
	dict_table['R11'] = 11
	dict_table['R12'] = 12
	dict_table['R13'] = 13
	dict_table['R14'] = 14
	dict_table['R15'] = 15
	dict_table['SCREEN'] = 16384
	dict_table['KBD'] = 24576

def addEntry(symbol, address):
	dict_table[symbol] = address

def contains(symbol):
	return symbol in dict_table.keys()

def getAddress(symbol):
	return dict_table[symbol]
