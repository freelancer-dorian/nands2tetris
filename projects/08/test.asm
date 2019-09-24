//// call f n
//	// push return-addr
//	@return_after_%s
//	D=A
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push LCL
//	@LCL
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push ARG
//	@ARG
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push THIS
//	@THIS
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// push THAT
//	@THAT
//	D=M
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//	// ARG = SP - n - 5
//	// push SP addr
//	@SP
//	D=M
//	A=M
//	M=D
//	@SP
//	M=M+1
//	//push constant n- arg1 constant- arg2 n- cmd type: C_PUSH
//	@%s
//	D=A
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//
//	//push constant 5- arg1 constant- arg2 5- cmd type: C_PUSH
//	@5
//	D=A
//	@SP
//	A=M
//	M=D
//	@SP
//	M=M+1
//
//	//add- cmd type: C_ARITHMETIC
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@SP
//	M=M-1
//	A=M
//	M=M+D
//	@SP
//	M=M+1
//
//	//sub- cmd type: C_ARITHMETIC
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@SP
//	M=M-1
//	A=M
//	M=M-D
//	@SP
//	M=M+1
//
//	@SP
//	M=M-1
//	A=M
//	D=M
//	@ARG
//	M=D

//	// LCL = SP
//  @SP
//  D=M
//  @LCL
//  M=D

//	// goto f
//	@%s
//	0;JMP
//	// (return-addr after f)
//	(return_after_%s)

// return 

//	FRAME = LCL
@LCL
D=M
@FRAME
M=D

//RET = *(FRAME - 5)
// push FRAME
@SP
A=M
M=D
@SP
M=M+1
// push constatn 5
@5
D=A
@SP
A=M
M=D
@SP
M=M+1

//sub- cmd type: C_ARITHMETIC
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1

// pop RET
@SP
M=M-1
A=M
A=M
D=M
@RET
M=D

//	*ARG = pop()
//pop argument 0- arg1 argument- arg2 0- cmd type: C_POP
@ARG
D=M
@addr_arg
M=D
@SP
M=M-1
A=M
D=M
@addr_arg
A=M
M=D

// SP = LCL
@LCL
D=M
@SP
M=D

//pop pointer 1- arg1 pointer- arg2 1- cmd type: C_POP
@SP
M=M-1
A=M
D=M
@THAT
M=D

//pop pointer 0- arg1 pointer- arg2 0- cmd type: C_POP
@SP
M=M-1
A=M
D=M
@THIS
M=D

// pop to arg
@SP
M=M-1
A=M
D=M
@ARG
M=D
// pop to lcl
@SP
M=M-1
A=M
D=M
@LCL
M=D

@addr_arg
D=M+1
@SP
M=D

@RET
A=M
0;JMP
