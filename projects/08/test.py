f = open('test.asm')

ret = ''
for _ in f:
	if (not _.startswith('//')) and len(_) > 2:
		ret = ret + _[:-1] + '\\n'


print(ret)


# import CodeWriter


# print('-----------------------------add--------------------------------')
# print(CodeWriter.arithmetric_translate('add'))
# print()
# print('-----------------------------sub--------------------------------')
# print(CodeWriter.arithmetric_translate('sub'))
# print()
# print('-----------------------------neg--------------------------------')
# print(CodeWriter.arithmetric_translate('neg'))
# print()
# print('-----------------------------eq--------------------------------')
# print(CodeWriter.arithmetric_translate('eq'))
# print()
# print('-----------------------------gt--------------------------------')
# print(CodeWriter.arithmetric_translate('gt'))
# print()
# print('-----------------------------lt--------------------------------')
# print(CodeWriter.arithmetric_translate('lt'))
# print()
# print('-----------------------------and--------------------------------')
# print(CodeWriter.arithmetric_translate('and'))
# print()
# print('-----------------------------or--------------------------------')
# print(CodeWriter.arithmetric_translate('or'))
# print('-----------------------------not--------------------------------')
# print(CodeWriter.arithmetric_translate('not'))
# print()
